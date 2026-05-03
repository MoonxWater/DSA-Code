from typing import Callable
from termcolor import colored
import time, copy

class Engine:
    def __init__(self, *args):
        self.args = args

    def v8(self, func_name: Callable) -> None:
        self.func_name = func_name
        avg = 0

        for i in range(len(self.args)):
            dup = copy.deepcopy(self.args[i])
            start = time.perf_counter()
            res = self.func_name(*dup)
            end = time.perf_counter() - start
            
            self.wrapper(self.args[i], res, end, 'green')
            
            avg += end
        
        print(f"Avg Time: {avg / len(self.args)}s")
    
    def wrapper(self, arg, res, end, colour):
        print(colored("┌─────────────────────────────────────────────────", colour), end=colored("┐\n|", colour))
        print(f"         Function: {self.func_name.__name__}                    ", end=colored("\n|", colour))
        print(f"         Arg: {arg}                                    ", end=colored("\n|", colour))
        print(f"         Return Value: {res}                           ", end=colored("\n|", colour))
        print(f"         Time: {end}s                                  ", end=colored("\n└", colour))
        print(colored("─────────────────────────────────────────────────┘", colour))
        print()