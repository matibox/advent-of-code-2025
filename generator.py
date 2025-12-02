import os

NUM_DAYS = 12

SOLUTION_TEMPLATE = """def part1(lines: list[str]):

    return None


def part2(lines: list[str]):

    return None
"""
      

def main():
    for day in range(1, NUM_DAYS + 1):
        folder = f"day_{day}"

        # Create folder if needed
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")
        else:
            print(f"Folder already exists: {folder}")

        # Create solution.py
        sol_path = os.path.join(folder, "solution.py")
        if not os.path.exists(sol_path):
            with open(sol_path, "w", encoding="utf-8") as f:
                f.write(SOLUTION_TEMPLATE)
            print(f"  Created: {sol_path}")
        else:
            print(f"  solution.py already exists")

        # Create input.txt
        input_path = os.path.join(folder, "input.txt")
        if not os.path.exists(input_path):
            open(input_path, "w").close()
            print(f"  Created: {input_path}")
        else:
            print(f"  input.txt already exists")

        # Create test.txt
        test_path = os.path.join(folder, "test.txt")
        if not os.path.exists(test_path):
            open(test_path, "w").close()
            print(f"  Created: {test_path}")
        else:
            print(f"  test.txt already exists")

    print("\nAll done!")


if __name__ == "__main__":
    main()