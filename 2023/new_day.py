import sys, os
# import requests

def writeDayPythonFile(day):
    path = f"days/day{day}.py"
    if (os.path.exists(path)):
        print(f"The path '{path}' already exists. Not overwriting it.")
        return

    with open(path, 'w') as f:
        f.write(f"""

from days.day import Day
from time import sleep

class Day{day}(Day):

    day = {day}
    reuse_a_input_for_b = True

    # def solve_a(self):

    # def solve_b(self):

""".strip())
    print(f"Created new day file '{path}'")

# Requires session cookie or auth. Not worth it.
# def fetchDayInput(day):
#     path = f"inputs/{day}a.txt"
#     if (os.path.exists(path)):
#         print(f"The path '{path}' already exists. Not overwriting it.")
#         return
#     url = f"https://adventofcode.com/2023/day/{day}/input"
#     response = requests.get(url)
#     with open(path, 'wb') as f:
#         f.write(response.content)
#     print(f"Downloaded input file to '{path}'")

def createEmptyTestInputFile(day):
    path = f"test_inputs/{day}a.txt"
    if (os.path.exists(path)):
        print(f"The path '{path}' already exists. Not overwriting it.")
        return
    with open(path, 'w') as f:
        f.write('')
    print(f"Created empty test input file '{path}'")

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 1:
        print("Please provide the day number.")
        exit()

    day = args[0]
    writeDayPythonFile(day)
    # fetchDayInput(day)
    createEmptyTestInputFile(day)
