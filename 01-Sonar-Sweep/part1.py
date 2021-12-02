"""
AOC 2021 Day 1 Part 1 - https://adventofcode.com/2021/day/1

Number of times an increase occurs between measurements.
"""

def load_input():
    """Load the input file."""
    with open('input.txt', 'r') as fp:
        return [int(line.strip()) for line in fp]


def main():
    vals = load_input()
    last_val = None
    increase_count = 0

    for val in vals:
        if last_val and val > last_val:
            increase_count += 1
        
        last_val = val

    print(increase_count)


if __name__ == '__main__':
    main()
