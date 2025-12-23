import argparse
import importlib
import os
import sys
from time import perf_counter

def load_input(day: int, use_test: bool) -> 'list[str]':
    folder = f"day_{day}"
    filename = "test.txt" if use_test else "input.txt"
    path = os.path.join(folder, filename)

    if not os.path.exists(path):
        print(f"Error: file not found: {path}")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        
        
        return [line.rstrip("\n") for line in f.readlines()]

    
def main():
    os.system("cls" if os.name == "nt" else "clear")

    parser = argparse.ArgumentParser(description="Advent of Code runner")
    parser.add_argument("-day", "--day", type=int, required=True, help="Day number")
    parser.add_argument("-part", "--part", type=int, required=True, help="Part number")
    parser.add_argument(  "-t",  "--test", action="store_true", help="Use test input")

    args = parser.parse_args ()

    day = args.day
    part = args.part
    use_test = args.test

    # Check if the folder day_X exists
    folder = f"day_{day}"
    if not os.path.isdir(folder):
        print(f"Error: Day {day} is not available (missing folder '{folder}')")
        sys.exit(1)

    # Dynamic import: day_1.solution, day_2.solution, etc.
    module_name = f"{folder}.solution"

    try:
        solution = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Error: Could not find solution module for day {day}")
        sys.exit(1)

    # Get correct function part1 / part2
    func_name = f"part{part}"
    if not hasattr(solution, func_name):
        print(f"Error: '{module_name}' does not contain function '{func_name}'")
        sys.exit(1)

    func = getattr(solution, func_name)

    # Load input
    lines = load_input(day, use_test)

    # Execute solution
    start = perf_counter()
    result = func(lines)
    end = perf_counter()

    print(f"{result}, {end - start:.6f}s")


if __name__ == "__main__":
    main()