def find_occ(inp: list, slope: list, char="#"):
    COLUMNS = len(inp[0])
    count = 0
    x = 0
    for i in range(0, len(inp), slope[1]):
        if inp[i][x] == char:
            count += 1
        x += slope[0]
        if x >= COLUMNS:
            x -= COLUMNS
    return count


def part_1_solve(inp):
    return find_occ(inp, [3, 1])


def part_2_solve(inp):
    import math

    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]
    return math.prod([find_occ(inp, slope) for slope in slopes])


if __name__ == "__main__":
    lines = [
        line.rstrip("\n")
        for line in open(
            "/home/el/dev/advent_of_code/2020/days/day_3/input", "r"
        ).readlines()
    ]
    result_1 = part_1_solve(lines)
    print(result_1)
    result_2 = part_2_solve(lines)
    print(result_2)
