from typing import Tuple


RAW = """
2199943210
3987894921
9856789892
8767896789
9899965678"""


def get_risk_levels(raw: str) -> Tuple[int, int]:
    heightmap = [[int(x) for x in line] for line in raw.strip().splitlines()]
    sum = 0
    product = 1
    basins = []
    for i, line in enumerate(heightmap):
        for j, height in enumerate(line):
            if all(
                (
                    height < heightmap[i][j - 1] if j > 0 else True,
                    height < heightmap[i - 1][j] if i > 0 else True,
                    height < heightmap[i][j + 1] if j < len(line) - 1 else True,
                    height < heightmap[i + 1][j] if i < len(heightmap) - 1 else True,
                )
            ):
                sum += height + 1

                counted_points = set()

                def count_basin(i, j):
                    if (
                        j > 0
                        and heightmap[i][j - 1] != 9
                        and heightmap[i][j] < heightmap[i][j - 1]
                    ):
                        count_basin(i, j - 1)
                    if (
                        i > 0
                        and heightmap[i - 1][j] != 9
                        and heightmap[i][j] < heightmap[i - 1][j]
                    ):
                        count_basin(i - 1, j)
                    if (
                        j < len(line) - 1
                        and heightmap[i][j + 1] != 9
                        and heightmap[i][j] < heightmap[i][j + 1]
                    ):
                        count_basin(i, j + 1)
                    if (
                        i < len(heightmap) - 1
                        and heightmap[i + 1][j] != 9
                        and heightmap[i][j] < heightmap[i + 1][j]
                    ):
                        count_basin(i + 1, j)

                    counted_points.add((i, j))

                count_basin(i, j)
                basins.append(len(counted_points))

    for basin in sorted(basins, reverse=True)[:3]:
        product *= basin
    return sum, product


assert get_risk_levels(RAW) == (15, 1134)


if __name__ == "__main__":
    with open("data/day09.txt") as f:
        raw = f.read()
        print(get_risk_levels(raw))
