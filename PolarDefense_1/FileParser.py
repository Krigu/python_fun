import sys

# reads input from stdin
# expects n on the first line
# and the remaining n numbers on the second line
def process():
    n = int(input())
    line = input()
    found = False
    squadron_numbers = line.split(" ")
    parsed_numbers = {}
    for amount in squadron_numbers:
        if amount in parsed_numbers:
            found = True
            break

        parsed_numbers[amount] = 1
    print("YES" if found else "NO")


if __name__ == '__main__':
    old = sys.stdin
    for x in range(1, 26):
        file_name = "%02d" % x
        with open(file_name + ".in", 'r') as f:
            # dirty hack to simulate stdin
            sys.stdin = f
            process()
        output_file = open(file_name + ".out")
        should_be = output_file.readlines()[0]
        print("Should be: " + should_be)
    sys.stdin = old
