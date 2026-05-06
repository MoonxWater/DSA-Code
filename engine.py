from __future__ import annotations
from typing import Callable, Optional
from termcolor import colored
import time, copy, tracemalloc, math


class Engine:
    """
    DSA testing engine.

    Test case format
    ────────────────
    Each test case is a tuple of (args, expected_dict) where expected_dict
    is optional and can have keys "ret" and/or "mod":

        ([1, 2, 3], {"ret": 5})              # check return value only
        ([1, 2, 3], {"mod": [1, 2, 3]})      # check mutated args only (in-place)
        ([1, 2, 3], {"ret": 3, "mod": [...]}) # check both
        ([1, 2, 3],)                          # no check, just run

    Basic usage
    ───────────
    test_cases = [
        ([[1,2,3], 3], {"ret": 5}),
        ([[0,1,2,0]],  {"mod": [0,0,1,2]}),
    ]
    e = Engine(test_cases)
    e.v8(func)

    With defaults (avoids repeating ret/mod in every case)
    ──────────────────────────────────────────────────────
    e = Engine(test_cases, default_ret=0)
    e.set_defaults(ret=-1)

    Methods
    ───────
    .v8(func)                        run one function
    .compare(func1, func2, ...)      run multiple functions side-by-side
    .scale(func, generator, sizes)   measure time/space across input sizes
    .set_cases(test_cases)           replace all test cases
    .add_case(case)                  append a single test case
    .set_defaults(ret=..., mod=...)  change default expected values
    """

    def __init__(
        self,
        test_cases: list,
        default_ret=None,
        default_mod=None,
    ):
        self.test_cases   = test_cases
        self.default_ret  = default_ret
        self.default_mod  = default_mod

    # ── case management ──────────────────────────────────────────────────────

    def set_cases(self, test_cases: list) -> None:
        """Replace all test cases."""
        self.test_cases = test_cases

    def add_case(self, case: tuple) -> None:
        """Append a single test case."""
        self.test_cases.append(case)

    def set_defaults(self, ret=None, mod=None) -> None:
        """Change default expected values used when a test case omits ret/mod."""
        self.default_ret = ret
        self.default_mod = mod

    # ── public API ───────────────────────────────────────────────────────────

    def v8(self, func: Callable, repeat: int = 100) -> None:
        """Run func against all test cases."""
        if not self.test_cases:
            print(colored("  Engine: no test cases provided.", "yellow"))
            return
        results = self._run_all(func, repeat)
        self._print_results(func.__name__, results, repeat)

    def compare(self, *funcs: Callable, repeat: int = 100) -> None:
        """
        Run multiple functions on the same test cases and print a
        side-by-side comparison table.

        Example
        ───────
        Engine(test_cases).compare(brute_force, optimized)
        """
        if not self.test_cases:
            print(colored("  Engine: no test cases provided.", "yellow"))
            return
        if len(funcs) < 2:
            print(colored("  compare() needs at least 2 functions.", "yellow"))
            return
        all_results = {f.__name__: self._run_all(f, repeat) for f in funcs}
        self._print_compare(all_results, repeat)

    def scale(
        self,
        func: Callable,
        generator: Callable,
        sizes: Optional[list] = None,
        repeat: int = 20,
    ) -> None:
        """
        Measure time and space as input size grows, then guess complexity.

        Parameters
        ──────────
        func       : function to profile
        generator  : callable(n) -> args_list  (e.g. lambda n: [[...n items...], k])
        sizes      : list of n values  (default: [10, 100, 500, 1000, 5000])
        repeat     : runs per size for stable timing

        Example
        ───────
        Engine([]).scale(
            longest_subarray,
            lambda n: [[random.randint(-10, 10) for _ in range(n)], 5],
        )
        """
        sizes = sizes or [10, 100, 500, 1000, 5000]
        rows  = []

        for n in sizes:
            args  = generator(n)
            times = []

            for _ in range(repeat):
                dup = copy.deepcopy(args)
                t0  = time.perf_counter()
                try:
                    func(*dup)
                except Exception:
                    pass
                times.append(time.perf_counter() - t0)

            peak = 0
            dup  = copy.deepcopy(args)
            try:
                tracemalloc.start()
                func(*dup)
                _, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
            except Exception:
                tracemalloc.stop()

            rows.append({
                "n":    n,
                "time": sum(times) / len(times),
                "mem":  peak,
            })

        complexity = self._guess_complexity(
            [r["n"] for r in rows], [r["time"] for r in rows]
        )
        self._print_scale(func.__name__, rows, complexity)

    # ── core runner ──────────────────────────────────────────────────────────

    def _run_all(self, func: Callable, repeat: int) -> list:
        results = []

        for i, case in enumerate(self.test_cases):
            # unpack args and optional expected dict
            args        = case[0]
            expected    = case[1] if len(case) == 2 else {}
            exp_ret     = expected.get("ret", self.default_ret)
            exp_mod     = expected.get("mod", self.default_mod)

            # snapshot original input before any mutation
            original    = copy.deepcopy(args)

            times  = []
            ret    = None
            output = copy.deepcopy(args)   # will hold post-call args
            error  = None
            peak   = 0

            for _ in range(repeat):
                dup = copy.deepcopy(args)
                try:
                    t0  = time.perf_counter()
                    ret = func(*dup)
                    times.append(time.perf_counter() - t0)
                    output = dup            # capture mutated copy
                except Exception as e:
                    error = e
                    break

            if not error:
                dup = copy.deepcopy(args)
                try:
                    tracemalloc.start()
                    func(*dup)
                    _, peak = tracemalloc.get_traced_memory()
                    tracemalloc.stop()
                except Exception:
                    tracemalloc.stop()

            avg_t = sum(times) / len(times) if times else 0

            # for display: unwrap single-element arg lists
            # for mod comparison: always compare only the first (mutable) arg
            mod_args         = output[0] if len(output) == 1 else output
            mod_args_compare = output[0] if isinstance(output[0], (list, dict, set)) else mod_args

            # determine pass/fail
            if error:
                status = "error"
            elif exp_ret is None and exp_mod is None:
                status = "nocheck"
            else:
                ret_ok = (exp_ret is None) or (ret == exp_ret)
                mod_ok = (exp_mod is None) or (mod_args_compare == exp_mod)
                status = "pass" if (ret_ok and mod_ok) else "fail"

            # build diff string on failure
            diff = None
            if status == "fail":
                parts = []
                if exp_ret is not None and ret != exp_ret:
                    parts.append(f"ret: {self._diff(ret, exp_ret)}")
                if exp_mod is not None and mod_args_compare != exp_mod:
                    parts.append(f"mod: {self._diff(mod_args_compare, exp_mod)}")
                diff = "  |  ".join(parts)

            results.append({
                "idx":      i + 1,
                "input":    original,
                "ret":      ret,
                "mod":      mod_args,
                "exp_ret":  exp_ret,
                "exp_mod":  exp_mod,
                "diff":     diff,
                "time":     avg_t,
                "peak_mem": peak,
                "status":   status,
                "error":    error,
            })

        return results

    # ── diff ─────────────────────────────────────────────────────────────────

    @staticmethod
    def _diff(actual, expected) -> str:
        if isinstance(actual, list) and isinstance(expected, list):
            if len(actual) != len(expected):
                return f"length {len(actual)} ≠ {len(expected)}"
            for i, (a, e) in enumerate(zip(actual, expected)):
                if a != e:
                    return f"index {i}: got {a!r}, expected {e!r}"
            return "values differ"
        return f"got {actual!r}, expected {expected!r}"

    # ── complexity guesser ───────────────────────────────────────────────────

    @staticmethod
    def _guess_complexity(sizes: list, times: list) -> str:
        if len(sizes) < 3:
            return "?"

        def slog(x):
            return math.log(x) if x > 0 else 0

        t0 = times[0] if times[0] > 0 else 1e-9
        n0 = sizes[0]
        y  = [t / t0 for t in times]

        candidates = {
            "O(1)":       [1.0                                  for n in sizes],
            "O(log n)":   [slog(n / n0) + 1                     for n in sizes],
            "O(n)":       [n / n0                                for n in sizes],
            "O(n log n)": [(n / n0) * (slog(n / n0) + 1)        for n in sizes],
            "O(n²)":      [(n / n0) ** 2                         for n in sizes],
            "O(n³)":      [(n / n0) ** 3                         for n in sizes],
        }

        best_label, best_err = "?", float("inf")
        for label, pred in candidates.items():
            mag   = sum(b * b for b in pred)
            scale = sum(a * b for a, b in zip(y, pred)) / mag if mag > 0 else 1
            err   = sum((a - scale * b) ** 2 for a, b in zip(y, pred))
            if err < best_err:
                best_err, best_label = err, label

        return best_label

    # ── rendering helpers ────────────────────────────────────────────────────

    _STATUS_COLOR = {"pass": "green", "fail": "red", "error": "yellow", "nocheck": "cyan"}
    _STATUS_ICON  = {"pass": "✓",     "fail": "✗",   "error": "⚠",      "nocheck": "~"}
    _W = 60

    def _line(self, label: str, value: object, colour: str, value_colour: Optional[str] = None) -> None:
        label_str = f"  {label:<18}"
        value_str = str(value)
        max_val   = self._W - len(label_str) - 2
        if len(value_str) > max_val:
            value_str = value_str[:max_val - 3] + "..."
        content = label_str + (colored(value_str, value_colour) if value_colour else value_str)
        pad = self._W - len(label_str) - len(value_str)
        print(colored("│", colour) + content + " " * max(pad, 1) + colored("│", colour))

    @staticmethod
    def _fmt_mem(b: int) -> str:
        if b < 1024:      return f"{b} B"
        elif b < 1024**2: return f"{b/1024:.2f} KB"
        else:             return f"{b/1024**2:.2f} MB"

    @staticmethod
    def _fmt_time(s: float) -> str:
        return f"{s * 1000:.4f} ms"

    # ── v8 printer ───────────────────────────────────────────────────────────

    def _print_results(self, fname: str, results: list, repeat: int) -> None:
        times    = [r["time"] for r in results if r["time"] > 0]
        mems     = [r["peak_mem"] for r in results if r["peak_mem"] > 0]
        worst_t  = max(results, key=lambda r: r["time"])    if len(results) > 1 else None
        worst_m  = max(results, key=lambda r: r["peak_mem"]) if len(results) > 1 else None

        for r in results:
            colour = self._STATUS_COLOR[r["status"]]
            icon   = self._STATUS_ICON[r["status"]]

            print(colored(f"┌{'─'*self._W}┐", colour))
            header = f"  {icon} #{r['idx']}  {fname}"
            print(colored("│", colour) + header +
                  " " * max(self._W - len(header), 1) + colored("│", colour))
            print(colored(f"├{'─'*self._W}┤", colour))

            # always show original input
            self._line("input",       r["input"],   colour)

            # return value
            self._line("returned",    r["ret"],     colour)

            # modified args — only show if they differ from original input
            orig_unwrapped = r["input"][0] if len(r["input"]) == 1 else r["input"]
            if r["mod"] != orig_unwrapped:
                self._line("after call",  r["mod"],     colour)

            # expected values
            if r["exp_ret"] is not None:
                self._line("expected ret", r["exp_ret"], colour)
            if r["exp_mod"] is not None:
                self._line("expected mod", r["exp_mod"], colour)

            if r["diff"]:
                self._line("diff",        r["diff"],    colour, "red")
            if r["error"]:
                self._line("error",       r["error"],   colour, "red")

            slow_tag    = "  ← slowest" if worst_t and r is worst_t else ""
            big_tag     = "  ← largest" if worst_m and r is worst_m else ""
            slow_colour = "yellow" if slow_tag else None
            big_colour  = "yellow" if big_tag  else None

            self._line("time",
                       f"{self._fmt_time(r['time'])}  (avg ×{repeat}){slow_tag}",
                       colour, slow_colour)
            self._line("space (peak)",
                       f"{self._fmt_mem(r['peak_mem'])}{big_tag}",
                       colour, big_colour)

            print(colored(f"└{'─'*self._W}┘", colour))
            print()

        passed = sum(1 for r in results if r["status"] == "pass")
        failed = sum(1 for r in results if r["status"] == "fail")
        errors = sum(1 for r in results if r["status"] == "error")
        avg_ms  = sum(times)/len(times)*1000 if times else 0
        min_ms  = min(times)*1000            if times else 0
        max_ms  = max(times)*1000            if times else 0
        avg_mem = sum(mems)/len(mems)        if mems  else 0

        print(
            f"  {fname}  │  "
            f"{colored(f'{passed}✓','green')}  "
            f"{colored(f'{failed}✗','red')}  "
            f"{colored(f'{errors}⚠','yellow')}  │  "
            f"avg {avg_ms:.4f}ms  min {min_ms:.4f}ms  max {max_ms:.4f}ms  │  "
            f"avg space {self._fmt_mem(int(avg_mem))}"
        )
        print()

    # ── compare printer ──────────────────────────────────────────────────────

    def _print_compare(self, all_results: dict, repeat: int) -> None:
        fnames = list(all_results.keys())
        print(colored(f"\n  ┌─ COMPARE {'─'*42}", "cyan"))
        print()

        for i in range(len(self.test_cases)):
            case   = self.test_cases[i]
            args   = case[0]
            rows   = [(fn, all_results[fn][i]) for fn in fnames]

            times_i = [r["time"] for _, r in rows if r["time"] > 0]
            mems_i  = [r["peak_mem"] for _, r in rows]
            min_t   = min(times_i) if times_i else 0
            min_m   = min(mems_i)  if mems_i  else 0

            print(colored(f"  case #{i+1}  input: {str(args)[:60]}", "cyan"))
            print(colored(f"  {'─'*60}", "cyan"))

            for fname, r in rows:
                colour   = self._STATUS_COLOR[r["status"]]
                icon     = colored(self._STATUS_ICON[r["status"]], colour)
                fast_tag = colored(" ⚡", "green") if r["time"] == min_t and len(rows) > 1 else "  "
                lean_tag = colored(" 🪶", "green") if r["peak_mem"] == min_m and len(rows) > 1 else "  "

                ret_str  = str(r["ret"])
                if len(ret_str) > 12: ret_str = ret_str[:9] + "..."

                orig_unwrapped = r["input"][0] if len(r["input"]) == 1 else r["input"]
                mod_str  = ""
                if r["mod"] != orig_unwrapped:
                    m = str(r["mod"])
                    mod_str = "  mod=" + (m[:12] + "..." if len(m) > 12 else m)

                diff_str = colored(f"  ✗ {r['diff']}", "red")    if r["diff"]  else ""
                err_str  = colored(f"  ⚠ {r['error']}", "yellow") if r["error"] else ""

                print(
                    f"    {icon} {fname:<26}  "
                    f"ret={ret_str:<14}{mod_str:<18}  "
                    f"t={self._fmt_time(r['time'])}{fast_tag} "
                    f"mem={self._fmt_mem(r['peak_mem'])}{lean_tag}"
                    f"{diff_str}{err_str}"
                )
            print()

        print(colored(f"  ┌─ OVERALL {'─'*42}", "cyan"))
        print()
        for fname in fnames:
            results = all_results[fname]
            passed  = sum(1 for r in results if r["status"] == "pass")
            failed  = sum(1 for r in results if r["status"] == "fail")
            errors  = sum(1 for r in results if r["status"] == "error")
            times   = [r["time"] for r in results if r["time"] > 0]
            mems    = [r["peak_mem"] for r in results]
            avg_t   = sum(times)/len(times)*1000 if times else 0
            avg_m   = sum(mems)/len(mems)        if mems  else 0
            print(
                f"  {fname:<28}  "
                f"{colored(f'{passed}✓','green')} "
                f"{colored(f'{failed}✗','red')} "
                f"{colored(f'{errors}⚠','yellow')}  │  "
                f"avg {avg_t:.4f}ms  │  "
                f"avg space {self._fmt_mem(int(avg_m))}"
            )
        print()

    # ── scale printer ────────────────────────────────────────────────────────

    def _print_scale(self, fname: str, rows: list, complexity: str) -> None:
        print(colored(f"\n  ┌─ SCALE  {fname}  {'─'*37}", "magenta"))
        print()
        cw = 14
        print(colored(f"  {'n':>8}   {'time (ms)':>{cw}}   {'space':>{cw}}   ratio", "magenta"))
        print(colored(f"  {'─'*8}   {'─'*cw}   {'─'*cw}   {'─'*8}", "magenta"))

        base_t = rows[0]["time"] if rows[0]["time"] > 0 else 1e-12
        for r in rows:
            ratio = f"×{r['time']/base_t:.1f}" if r["time"] > 0 else "—"
            print(
                f"  {r['n']:>8}   "
                f"{r['time']*1000:>{cw}.4f}   "
                f"{self._fmt_mem(r['mem']):>{cw}}   "
                f"{ratio}"
            )

        print()
        print(colored(f"  complexity guess:  {complexity}", "magenta"))
        print()