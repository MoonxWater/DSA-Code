from __future__ import annotations
from typing import Callable, Optional
from termcolor import colored
import time, copy, tracemalloc, math


class Engine:
    """
    DSA testing engine.

    Basic usage
    ───────────
    test_cases = [
        (([0, 1, 2, 0],), [0, 0, 1, 2]),   # in-place  → (args_tuple, expected)
        (([1, 2, 3], 3),  5),               # return    → (args_tuple, expected)
        (([0, 2, 1],),),                    # no check  → (args_tuple,)
    ]
    run = Engine(test_cases).v8

    Methods
    ───────
    .v8(func)                        run one function
    .compare(func1, func2, ...)      run multiple functions side-by-side
    .scale(func, generator, sizes)   measure time/space across input sizes
    """

    def __init__(self, test_cases: list):
        self.test_cases = test_cases

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
        generator  : callable(n) -> args_tuple  (e.g. lambda n: ([...n items...], k))
        sizes      : list of n values  (default: [10, 100, 500, 1000, 5000])
        repeat     : runs per size for stable timing

        Example
        ───────
        Engine([]).scale(
            longest_subarray,
            lambda n: ([random.randint(-10, 10) for _ in range(n)], 5),
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
            args     = case[0]
            expected = case[1] if len(case) == 2 else None

            args_display = copy.deepcopy(args)
            times  = []
            res    = None
            output = copy.deepcopy(args)
            error  = None
            peak   = 0

            for _ in range(repeat):
                dup = copy.deepcopy(args)
                try:
                    t0  = time.perf_counter()
                    res = func(*dup)
                    times.append(time.perf_counter() - t0)
                    output = dup
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

            avg_t  = sum(times) / len(times) if times else 0
            actual = (output[0] if len(output) == 1 else output) if res is None else res

            if error:
                status = "error"
            elif expected is None:
                status = "nocheck"
            else:
                status = "pass" if actual == expected else "fail"

            diff = self._diff(actual, expected) if status == "fail" else None

            results.append({
                "idx":      i + 1,
                "args":     args_display,
                "actual":   actual,
                "expected": expected,
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
    _W = 56

    def _line(self, label: str, value: object, colour: str, value_colour: Optional[str] = None) -> None:
        label_str = f"  {label:<16}"
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
        times = [r["time"] for r in results if r["time"] > 0]
        mems  = [r["peak_mem"] for r in results if r["peak_mem"] > 0]
        worst_t: Optional[dict] = max(results, key=lambda r: r["time"])   if len(results) > 1 else None
        worst_m: Optional[dict] = max(results, key=lambda r: r["peak_mem"]) if len(results) > 1 else None

        for r in results:
            colour = self._STATUS_COLOR[r["status"]]
            icon   = self._STATUS_ICON[r["status"]]

            print(colored(f"┌{'─'*self._W}┐", colour))
            header = f"  {icon} #{r['idx']}  {fname}"
            print(colored("│", colour) + header +
                  " " * max(self._W - len(header), 1) + colored("│", colour))
            print(colored(f"├{'─'*self._W}┤", colour))

            self._line("input",    r["args"],   colour)
            self._line("output",   r["actual"], colour)
            if r["expected"] is not None:
                self._line("expected", r["expected"], colour)
            if r["diff"]:
                self._line("diff", r["diff"], colour, "red")
            if r["error"]:
                self._line("error", r["error"], colour, "red")

            slow_tag  = "  ← slowest" if worst_t and r is worst_t else ""
            big_tag   = "  ← largest" if worst_m and r is worst_m else ""
            slow_colour: Optional[str] = "yellow" if slow_tag else None
            big_colour:  Optional[str] = "yellow" if big_tag  else None
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
            case     = self.test_cases[i]
            args     = case[0]
            rows     = [(fn, all_results[fn][i]) for fn in fnames]

            times_i  = [r["time"] for _, r in rows if r["time"] > 0]
            mems_i   = [r["peak_mem"] for _, r in rows]
            min_t    = min(times_i) if times_i else 0
            min_m    = min(mems_i)  if mems_i  else 0

            print(colored(f"  case #{i+1}  input: {str(args)[:60]}", "cyan"))
            print(colored(f"  {'─'*56}", "cyan"))

            for fname, r in rows:
                colour    = self._STATUS_COLOR[r["status"]]
                icon      = colored(self._STATUS_ICON[r["status"]], colour)
                fast_tag  = colored(" ⚡", "green") if r["time"] == min_t and len(rows) > 1 else "  "
                lean_tag  = colored(" 🪶", "green") if r["peak_mem"] == min_m and len(rows) > 1 else "  "
                out_str   = str(r["actual"])
                if len(out_str) > 18: out_str = out_str[:15] + "..."
                diff_str  = colored(f"  ✗ {r['diff']}", "red")  if r["diff"]  else ""
                err_str   = colored(f"  ⚠ {r['error']}", "yellow") if r["error"] else ""

                print(
                    f"    {icon} {fname:<26}  "
                    f"out={out_str:<20}  "
                    f"t={self._fmt_time(r['time'])}{fast_tag} "
                    f"mem={self._fmt_mem(r['peak_mem'])}{lean_tag}"
                    f"{diff_str}{err_str}"
                )
            print()

        # overall summary
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