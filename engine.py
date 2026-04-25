from typing import Callable
from termcolor import colored
import time

class Engine:
    def runner(self, func_name: Callable, *args) -> None:
        self.func_name = func_name
        avg = 0

        for i in range(len(args)):
            start = time.perf_counter()
            res = self.call_func(*args[i])
            end = time.perf_counter() - start
            
            print(colored(f"┌────────────────────────{i+1}────────────────────────", 'green'), end=colored("┐\n|", 'green'))
            print(f"    Arg: {args[i]}                       ", end=colored("\n|", 'green'))
            print(f"    Return Value: {res}                  ", end=colored("\n|", 'green'))
            print(f"    Time: {end}s                         ", end=colored("\n└", 'green'))
            print(colored("─────────────────────────────────────────────────┘", 'green'))
            print()
            avg += end
        
        print(f"Avg Time: {avg / len(args)}s")

    def call_func(self, *args):
        return self.func_name(*args)
        

run = Engine().runner