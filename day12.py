from typing import Iterable, List
from collections import defaultdict
from copy import deepcopy


RAW = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""


class Map:
    def __init__(self, raw: str) -> None:
        self.caves = [line.split("-") for line in raw.splitlines()]
        self.map = defaultdict(list)
        for pair in self.caves:
            self.make_connection(pair)
        self.paths = []

    def make_connection(self, pair: Iterable[str]) -> None:
        if pair[0] == "start" or pair[1] == "end":
            self.map[pair[0]].append(pair[1])
        elif pair[1] == "start" or pair[0] == "end":
            self.map[pair[1]].append(pair[0])
        else:
            self.map[pair[0]].append(pair[1])
            self.map[pair[1]].append(pair[0])

    def find_paths(self, is_twice: bool = False) -> None:
        for cave in self.map["start"]:
            self.path(cave, ["start", cave], is_twice)

    def path(self, start_cave: str, path: List[str], is_twice: bool = False):
        path = deepcopy(path)
        for cave in self.map[start_cave]:
            if cave == "end":
                path.append(cave)
                self.paths.append(path)
            elif (cave.islower() and cave not in path) or cave.isupper():
                new_path = deepcopy(path)
                new_path.append(cave)
                self.path(cave, new_path, is_twice)
            elif cave.islower() and is_twice:
                new_path = deepcopy(path)
                new_path.append(cave)
                self.path(cave, new_path)

    def get_n_paths(self) -> int:
        return len(self.paths)


map = Map(RAW)
map.find_paths()

assert map.get_n_paths() == 10

map = Map(RAW)
map.find_paths(is_twice=True)

assert map.get_n_paths() == 36

if __name__ == "__main__":
    with open("data/day12.txt") as f:
        raw = f.read()
        map = Map(raw)
        map.find_paths()
        print(map.get_n_paths())

        map = Map(raw)
        map.find_paths(is_twice=True)
        print(map.get_n_paths())
