from re import compile


def read_file(handle: str):
    with open(handle, "r") as f:
        return f.readlines()


replacers = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
]


def part_one(contents: list[str]):
    sum = 0
    pattern = compile("[\D]+")
    for line in contents:
        nums = pattern.sub("", line)
        sum += int(f"{nums[0]}{nums[-1]}")
    print(f"Part 1: {sum}")


def part_two(contents: list[str]):
    sum = 0
    for line in contents:
        character_digits = []
        tmp = ""
        # Have to do this bullshit because of stuff like "oneightnine"
        # which is "19" not "189"
        for char in line:
            tmp += char
            for word, digit in replacers:
                if word in tmp:
                    character_digits.append(str(digit))
                    tmp = char
                if char.isdigit():
                    character_digits.append(char)
                    tmp = ""

        sum += int(f"{character_digits[0]}{character_digits[-1]}")
    print(f"Part 2: {sum}")


def main():
    contents = read_file("one.input.txt")
    part_one(contents)
    part_two(contents)


if __name__ == "__main__":
    main()
