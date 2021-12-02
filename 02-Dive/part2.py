"""
AOC Day 2 Part 1 - https://adventofcode.com/2021/day/2
"""

from part1 import load_input


def main():
    commands = load_input()

    state_dist = 0
    state_depth = 0
    state_aim = 0

    for line in commands:
        direction, distance = line.split()
        distance = int(distance)

        if direction == 'forward':
            state_dist += distance
            state_depth += distance*state_aim
        elif direction == 'up':
            state_aim -= distance
        else:
            state_aim += distance

    print(f"Final state: distance={state_dist}, depth={state_depth}, aim={state_aim}")
    print(f"Solution: {state_dist*state_depth}")


if __name__ == '__main__':
    main()
