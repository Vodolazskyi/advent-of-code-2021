from typing import Iterable
from heapq import heappop, heappush


RAW = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


Grid = Iterable[Iterable[int]]


def parse(raw: str) -> Grid:
    return [[int(x) for x in line] for line in raw.splitlines()]


def lowest_risk_path(grid: Grid) -> int:
    nr = len(grid)
    nc = len(grid[0])

    q = []
    heappush(q, (0, 0, 0))

    visited = {(0, 0)}

    while q:
        cost, r, c = heappop(q)

        if r == nr - 1 and c == nc - 1:
            return cost
        for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            r_ = r + dr
            c_ = c + dc
            if 0 <= r_ < nr and 0 <= c_ < nc and (r_, c_) not in visited:
                heappush(q, (grid[r_][c_] + cost, r_, c_))
                visited.add((r_, c_))


def shrink(x: int) -> int:
    if x > 9:
        return x - 9
    return x


def grow(grid: Grid) -> Grid:
    nr = len(grid)
    nc = len(grid[0])

    new_grid = [[0 for _ in range(nc * 5)] for _ in range(nr * 5)]
    for i in range(5):
        for j in range(5):
            for r in range(nr):
                for c in range(nc):
                    new_value = shrink(grid[r][c] + i + j)
                    new_grid[r + i * nr][c + j * nc] = new_value
    return new_grid


GRID = parse(RAW)
assert lowest_risk_path(GRID) == 40

BIG_GRID = grow(GRID)
assert lowest_risk_path(BIG_GRID) == 315

if __name__ == "__main__":
    with open("data/day15.txt") as f:
        raw = f.read()
        grid = parse(raw)
        print(lowest_risk_path(grid))
        print(lowest_risk_path(grow(grid)))
