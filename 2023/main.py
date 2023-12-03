import sys
from importlib import import_module
if __name__ == "__main__":
    args = sys.argv[1:]
    if (len(args) < 1 or len(args[0]) < 2):
        print("""
        HOW TO USE:
            Put the input file in the inputs folder, and name if like 3a.txt (for part 1 of day 3).
            Then run this script with a single argument like "3a".

            You can include "test" as a second argument to run on test input instead.
            """)
        exit()

    test = len(args) > 1 and args[1].lower() == "test"

    (day, ab) = args[0]
    day_mod = import_module(f"days.day{day}")
    day = getattr(day_mod, f"Day{day}")(ab, test)
    day.solve()
    