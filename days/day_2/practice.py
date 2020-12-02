import re


def part_1_solve():
    lines = [
        line
        for line in open(
            "/home/el/dev/advent_of_code/2020/days/day_2/input", "r"
        ).readlines()
    ]
    count = 0
    for line in lines:
        occ_lo, occ_hi, rule, password, *_ = re.split(r"[-\s:]\s*", line)
        occ = password.count(rule)
        if occ >= int(occ_lo) and occ <= int(occ_hi):
            count += 1
    return count


# RegEx explanation
# https://regex101.com/r/6MT4np/1


def faster_1_solve():
    lines = [
        line
        for line in open(
            "/home/el/dev/advent_of_code/2020/days/day_2/input", "r"
        ).readlines()
    ]
    r = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
    count = 0
    for line in lines:
        occ_lo, occ_hi, rule, password, *_ = r.match(line).groups()
        if int(occ_lo) <= password.count(rule) <= int(occ_hi):
            count += 1
    return count


def help_1_solve():
    p = re.compile("(\d+)-(\d+) (\w): (\w+)")
    content = open("/home/el/dev/advent_of_code/2020/days/day_2/input").readlines()

    # part 1
    count = 0
    for entry in content:
        (lower, upper, symbol, password) = p.match(entry).groups()
        if int(lower) <= password.count(symbol) <= int(upper):
            count += 1

    return count


def part_2_solve():
    lines = [
        line
        for line in open(
            "/home/el/dev/advent_of_code/2020/days/day_2/input", "r"
        ).readlines()
    ]
    count = 0
    for line in lines:
        occ_lo, occ_hi, rule, password, *_ = re.split(r"[-\s:]\s*", line)
        if (password[int(occ_lo) - 1] == rule) ^ (password[int(occ_hi) - 1] == rule):
            count += 1
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
            "faster_1_solve()", setup="from __main__ import faster_1_solve", number=100
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
    faster_1 = faster_1_solve()
    print(faster_1)
    result_2 = part_2_solve()
    print(result_2)

    timing()
