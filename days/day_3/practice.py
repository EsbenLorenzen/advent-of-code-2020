def part_1_solve():
    lines = [
        line.rstrip("\n")
        for line in open(
            "/home/el/dev/advent_of_code/2020/days/day_3/input", "r"
        ).readlines()
    ]
    tree_count = 0
    x = 0
    for line in lines:
        if line[x] == "#":
            tree_count += 1
        x += 3
        if x >= 31:
            x -= 31
    return tree_count


def part_2_solve():
    import math

    lines = [
        line.rstrip("\n")
        for line in open(
            "/home/el/dev/advent_of_code/2020/days/day_3/input", "r"
        ).readlines()
    ]
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]
    tree_counts = [0 for x in range(5)]
    for s, slope in enumerate(slopes):
        x = 0
        for i in range(0, len(lines), slope[1]):
            if lines[i][x] == "#":
                tree_counts[s] += 1
            x += slope[0]
            if x >= 31:
                x -= 31
    return math.prod(tree_counts)


def faster_1_solve():
    pass


def help_1_solve():
    pass


def timing():
    import timeit

    print(
        timeit.timeit(
            "part_1_solve()", setup="from __main__ import part_1_solve", number=100
        )
    )

    # print(
    #     timeit.timeit(
    #         "faster_1_solve()", setup="from __main__ import faster_1_solve", number=100
    #     )
    # )

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
