import sys, os

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 1:
        print("Please provide the day number.")
        exit()

    day = args[0]
    path = f"days/day{day}.py"
    if (os.path.exists(path)):
        print(f"The path '{path}' already exists. Not overwriting it.")
        exit()

    with open(path, 'w') as f:
        f.write(f"""
                


from days.day import Day

class Day{day}(Day):

    day = {day}
    # reuse_a_input_for_b = True

    # def solve_a(self):

    # def solve_b(self):

    


""".strip())

    print(f"Created new day file '{path}'")