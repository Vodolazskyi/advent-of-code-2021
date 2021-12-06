from typing import List, Tuple
from collections import defaultdict


RAW = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


class Vent:
    def __init__(self, line: str) -> None:
        self.x1, self.y1, self.x2, self.y2 = self.parse_line(line)

    def __repr__(self):
        return f"Vent({self.x1}, {self.y1}, {self.x2}, {self.y2})"

    @staticmethod
    def parse_line(line: str) -> Tuple[int]:
        start_point, end_point = line.split("->")
        x1, y1 = Vent.parse_point(start_point)
        x2, y2 = Vent.parse_point(end_point)
        return x1, y1, x2, y2

    @staticmethod
    def parse_point(point: str) -> Tuple[int]:
        x, y = point.split(",")
        return int(x), int(y)


def calculate_overlap_points(lines: List[str], count_diagonals: bool = False) -> int:
    diagram = defaultdict(lambda: defaultdict(int))
    for line in lines:
        vent = Vent(line)
        if vent.x1 == vent.x2:
            for y in range(min(vent.y1, vent.y2), max(vent.y1, vent.y2) + 1):
                diagram[vent.x1][y] += 1
        elif vent.y1 == vent.y2:
            for x in range(min(vent.x1, vent.x2), max(vent.x1, vent.x2) + 1):
                diagram[x][vent.y1] += 1
        elif count_diagonals and abs(vent.x1 - vent.x2) == abs(vent.y1 - vent.y2):
            x_range = (
                range(vent.x1, vent.x2 + 1)
                if vent.x2 > vent.x1
                else range(vent.x1, vent.x2 - 1, -1)
            )
            y_range = (
                range(vent.y1, vent.y2 + 1)
                if vent.y2 > vent.y1
                else range(vent.y1, vent.y2 - 1, -1)
            )
            for x, y in zip(x_range, y_range):
                diagram[x][y] += 1

    return sum(sum(point > 1 for point in row.values()) for row in diagram.values())


INPUT = RAW.splitlines()
assert calculate_overlap_points(INPUT) == 5
assert calculate_overlap_points(INPUT, count_diagonals=True) == 12


if __name__ == "__main__":
    with open("data/day05.txt") as f:
        input = f.read().splitlines()
        print(calculate_overlap_points(input))
        print(calculate_overlap_points(input, count_diagonals=True))
