from typing import List, Tuple


RAW = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def read_instructions(raw: str) -> List[Tuple[str, int]]:
    return [
        (line.split()[-1].split("=")[0], int(line.split()[-1].split("=")[1]))
        for line in raw.splitlines()
        if line.startswith("fold")
    ]


class Paper:
    def __init__(self, dots: List[List[int]]) -> None:
        self.nc = max(dot[0] for dot in dots) + 1
        self.nr = max(dot[1] for dot in dots) + 1
        self.paper = [["." for _ in range(self.nc)] for _ in range(self.nr)]
        for dot in dots:
            self.paper[dot[1]][dot[0]] = "#"

    @staticmethod
    def parse(raw: str) -> "Paper":
        dots = []
        for line in raw.splitlines():
            if line == "":
                break
            dots.append([int(x) for x in line.split(",")])
        return Paper(dots)

    def number_of_dots(self) -> int:
        return sum(sum(dot == "#" for dot in row) for row in self.paper)

    def fold(self, axis: str, n: int) -> None:
        if axis == "y":
            for r in range(self.nr):
                if r > n:
                    for c in range(self.nc):
                        if self.paper[r][c] == "#":
                            self.paper[2 * n - r][c] = "#"
            self.paper = [self.paper[r] for r in range(n)]
            self.nr = len(self.paper)
        elif axis == "x":
            for r in range(self.nr):
                for c in range(self.nc):
                    if c > n and self.paper[r][c] == "#":
                        self.paper[r][2 * n - c] = "#"
            self.paper = [row[:n] for row in self.paper]
            self.nc = len(self.paper[0])
        else:
            raise ValueError("Non-existing axis")


def print_rectangle(rectangle: List[List[int]]) -> None:
    rec_str = [[str(i) for i in row] for row in rectangle]
    length_list = [len((element)) for row in rec_str for element in row]
    column_width = max(length_list)
    for row in rec_str:
        row = "".join(element.ljust(column_width + 2) for element in row)
        print(row)


paper = Paper.parse(RAW)
instructions = read_instructions(RAW)
paper.fold(*instructions[0])

assert paper.number_of_dots() == 17


if __name__ == "__main__":
    with open("data/day13.txt") as f:
        raw = f.read()
        paper = Paper.parse(raw)
        instructions = read_instructions(raw)
        paper.fold(*instructions[0])
        print(paper.number_of_dots())

        for instruction in instructions[1:]:
            paper.fold(*instruction)
        print_rectangle(paper.paper)
