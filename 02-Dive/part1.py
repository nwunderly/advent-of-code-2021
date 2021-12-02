"""
AOC Day 2 Part 1 - https://adventofcode.com/2021/day/2

Tracking submarine position based on instructions.
"""

def load_input():
    """Load the input file."""
    with open('input.txt', 'r') as fp:
        return [line.strip() for line in fp]


def main():
    commands = load_input()

    state_dist = 0
    state_depth = 0

    for line in commands:
        direction, distance = line.split()
        distance = int(distance)

        if direction == 'forward':
            state_dist += distance
        elif direction == 'up':
            state_depth -= distance
        else:
            state_depth += distance

    print(f"Final state: distance={state_dist}, depth={state_depth}")
    print(f"Solution: {state_dist*state_depth}")


if __name__ == '__main__':
    main()
