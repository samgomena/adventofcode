from collections import defaultdict
import math


def read_file(handle: str):
    with open(handle, "r") as f:
        return f.readlines()


limits = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def _parse_line_part_one(line: str):
    # Lines in the form of:
    # Game <game id>: <num> red, <num> green, <num> blue; <num> green, <num> red, <num> blue; <num> blue, <num> green, <num> red; <num> blue, <num> green, <num> red
    game_id = int(line.split(":")[0].split(" ")[1])
    for game in line.split(":")[1].split(";"):
        sets = game.strip().split(", ")
        for set in sets:
            count, color = set.split(" ")
            if int(count) > limits[color]:
                return (False, game_id)
    return (True, game_id)


def _parse_line_part_two(line: str):
    minimum_cubes_reqd = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for game in line.split(":")[1].split(";"):
        sets = game.strip().split(", ")
        for set in sets:
            count, color = set.split(" ")
            if int(count) > minimum_cubes_reqd[color]:
                minimum_cubes_reqd[color] = int(count)
    return minimum_cubes_reqd


def part_one(contents: list[str]):
    sum = 0
    for line in contents:
        allowed, game_id = _parse_line_part_one(line)
        if allowed:
            sum += game_id
    print(sum)


def part_two(contents: list[str]):
    sum = 0
    for line in contents:
        minimums = _parse_line_part_two(line)
        sum += minimums["red"] * minimums["green"] * minimums["blue"]
    print(sum)


def main():
    contents = read_file("two.input.txt")
    part_one(contents)
    part_two(contents)


if __name__ == "__main__":
    main()
