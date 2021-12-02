"""
AOC 2021 Day 1 Part 2 - https://adventofcode.com/2021/day/1#part2

Number of times an increase occurs between 3-measurement groups.
"""

from part1 import load_input


def main():
    vals = load_input()
    last_val = None
    increase_count = 0

    groups_of = 3

    for i in range(len(vals)-(groups_of-1)):
        group = vals[i:i+groups_of]
        val = sum(group)
        
        if last_val and val > last_val:
            increase_count += 1
        
        last_val = val

    print(increase_count)


if __name__ == '__main__':
    main()
