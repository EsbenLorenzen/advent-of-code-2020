import re


def part_1_solve():
    count = 0
    lines = [
        line
        for line in open(
            "/home/el/dev/advent_of_code/2020/days/day_2/input", "r"
        ).readlines()
    ]
    for line in lines:
        split = re.split(r"[-\s:]\s*", line)
        occ = split[3].count(split[2])
        if occ >= int(split[0]) and occ <= int(split[1]):
            count += 1
    return count


def part_2_solve():
    count = 0
    lines = [
        line
        for line in open(
            "/home/el/dev/advent_of_code/2020/days/day_2/input", "r"
        ).readlines()
    ]
    for line in lines:
        split = re.split(r"[-\s:]\s*", line)
        try:
            if (
                split[3][int(split[0]) - 1] == split[2]
                and split[3][int(split[1]) - 1] != split[2]
            ) or (
                split[3][int(split[0]) - 1] != split[2]
                and split[3][int(split[1]) - 1] == split[2]
            ):
                count += 1
        except IndexError:
            pass
    return count


def timing():
    import timeit

    print(
        timeit.timeit(
            "part_1_solve()", setup="from __main__ import part_1_solve", number=100
        )
    )

    print(
        timeit.timeit(
            "part_2_solve()", setup="from __main__ import part_2_solve", number=100
        )
    )


if __name__ == "__main__":
    result_1 = part_1_solve()
    print(result_1)
    result_2 = part_2_solve()
    print(result_2)

    timing()
