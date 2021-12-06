from typing import List
from collections import Counter


RAW = """3,4,3,1,2"""


class Lanternfish:
    def __init__(self, population: List[int]) -> None:
        self.population = Counter(population)

    @staticmethod
    def parse(raw: str) -> "Lanternfish":
        return Lanternfish([int(fish) for fish in raw.split(",")])

    def pass_n_days(self, n: int) -> None:
        for _ in range(n):
            older_fish = self.population[8]
            self.population[8] = 0
            for i in range(7, -1, -1):
                temp_fish = self.population[i]
                self.population[i] = older_fish
                older_fish = temp_fish
            self.population[6] += older_fish
            self.population[8] = older_fish

    def get_population_size(self) -> int:
        return self.population.total()


fish = Lanternfish.parse(RAW)
fish.pass_n_days(18)
assert fish.get_population_size() == 26

fish = Lanternfish.parse(RAW)
fish.pass_n_days(80)
assert fish.get_population_size() == 5934

fish = Lanternfish.parse(RAW)
fish.pass_n_days(256)
assert fish.get_population_size() == 26984457539


if __name__ == "__main__":
    with open("data/day06.txt") as f:
        raw = f.read()
        fish = Lanternfish.parse(raw)
        fish.pass_n_days(80)
        print(fish.get_population_size())

        fish = Lanternfish.parse(raw)
        fish.pass_n_days(256)
        print(fish.get_population_size())
