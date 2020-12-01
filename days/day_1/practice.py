# --- Day 1: Report Repair ---


def part_1_solve():
    with open("input", "r", encoding="utf8") as f:
        lines = f.readlines()
        for i, _ in enumerate(lines):
            for j, _ in enumerate(lines):
                if int(lines[i]) + int(lines[j]) == 2020:
                    return int(lines[i]) * int(lines[j])


def part_2_solve():
    with open("input", "r", encoding="utf8") as f:
        lines = f.readlines()
        for i, _ in enumerate(lines):
            for j, _ in enumerate(lines):
                for k, _ in enumerate(lines):
                    if not i == j and not i == k and not j == k:
                        if int(lines[i]) + int(lines[j]) + int(lines[k]) == 2020:
                            return int(lines[i]) * int(lines[j]) * int(lines[k])


# Terrible
def extra_sort_solve():
    HALF = 2020 // 2
    with open("input", "r", encoding="utf8") as f:
        lines = sorted(f.readlines())
        for n1 in lines:
            n1 = int(n1)
            direction = 0 if n1 > HALF else 1
            start = n1 if direction else 0
            for j, n2 in enumerate(lines, start):
                n2 = int(n2)
                if n1 + n2 == 2020:
                    return n1 * n2


def part_1_help():
    xs = [int(x) for x in open("input").readlines()]
    n = len(xs)
    for i in range(n):
        for j in range(i + 1):
            if xs[i] + xs[j] == 2020:
                return xs[i] * xs[j]


def part_2_help():
    X = [int(line) for line in open("input").readlines()]
    n = len(X)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if X[i] + X[j] + X[k] == 2020:
                    return X[i] * X[j] * X[k]


def timing():
    import timeit

    print(
        timeit.timeit(
            "part_2_solve()", setup="from __main__ import part_2_solve", number=10
        )
    )
    print(
        timeit.timeit(
            "part_1_help()",
            setup="from __main__ import part_1_help",
            number=100,
        )
    )
    print(
        timeit.timeit(
            "part_2_help()",
            setup="from __main__ import part_2_help",
            number=10,
        )
    )


if __name__ == "__main__":
    result_1 = part_1_solve()
    print(result_1)
    result_2 = part_2_solve()
    print(result_2)
    result_4 = extra_sort_solve()
    print(result_4)
    result_4 = part_2_help()
    print(result_4)

    timing()
