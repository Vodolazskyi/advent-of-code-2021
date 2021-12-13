from typing import Iterator, Tuple


RAW = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


class Octopus:
    def __init__(self, raw: str) -> None:
        self.grid = [[int(x) for x in line] for line in raw.splitlines()]
        self.nr = len(self.grid)
        self.nc = len(self.grid[0])
        self.n_flashes = 0
        self.all_flash = False

    def get_neighbours(self, r, c) -> Iterator[Tuple[int, int]]:
        neighbours = (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        )
        for d_r, d_c in neighbours:
            if 0 <= r + d_r <= self.nr - 1 and 0 <= c + d_c <= self.nc - 1:
                yield r + d_r, c + d_c

    def step(self) -> None:
        for r in range(self.nr):
            for c in range(self.nc):
                self.grid[r][c] += 1

        new_flashes = True
        flashed = []
        while new_flashes:
            begin_len_flashed = len(flashed)
            for r in range(self.nr):
                for c in range(self.nc):
                    if self.grid[r][c] > 9 and (r, c) not in flashed:
                        self.n_flashes += 1
                        flashed.append((r, c))
                        for n_r, n_c in self.get_neighbours(r, c):
                            self.grid[n_r][n_c] += 1
            if len(flashed) == begin_len_flashed:
                new_flashes = False

        for r in range(self.nr):
            for c in range(self.nc):
                if self.grid[r][c] > 9:
                    self.grid[r][c] = 0

        if len(flashed) == self.nr * self.nc:
            self.all_flash = True

    def get_n_flashes(self) -> int:
        return self.n_flashes

    def is_all_flash(self) -> bool:
        return self.all_flash


oct = Octopus(RAW)
for _ in range(100):
    oct.step()

assert oct.get_n_flashes() == 1656

oct = Octopus(RAW)
n_steps = 0
while not oct.is_all_flash():
    oct.step()
    n_steps += 1

assert n_steps == 195


if __name__ == "__main__":
    with open("data/day11.txt") as f:
        raw = f.read()
        oct = Octopus(raw)
        for _ in range(100):
            oct.step()
        print(oct.get_n_flashes())

        oct = Octopus(raw)
        n_steps = 0
        while not oct.is_all_flash():
            oct.step()
            n_steps += 1
        print(n_steps)
