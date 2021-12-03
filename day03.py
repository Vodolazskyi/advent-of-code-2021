from collections import defaultdict
from typing import List


RAW = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

INPUT = RAW.splitlines()


class BitCounter:
    def __init__(self, input: List[str]) -> None:
        self.input = input
        self.counter = defaultdict(int)
        self.count_bits()

    def len(self) -> int:
        return len(self.input)

    def n_bits(self) -> int:
        return len(self.counter)

    def count_bits(self) -> None:
        for line in self.input:
            for i, bit in enumerate(line):
                self.counter[i] += int(bit)

    def get_most_common_bits(self) -> str:
        return "".join(
            [
                str(int(self.counter[i] >= len(self.input) / 2))
                for i in range(len(self.counter))
            ]
        )

    def get_least_common_bits(self) -> str:
        return "".join(
            [
                str(int(self.counter[i] < len(self.input) / 2))
                for i in range(len(self.counter))
            ]
        )


def get_gamma(counter: BitCounter) -> int:
    return int(counter.get_most_common_bits(), 2)


def get_epsilon(counter: BitCounter) -> int:
    return int(counter.get_least_common_bits(), 2)


def get_oxygen_rate(input: List[str]) -> int:
    oxygen_input = input
    oxygen_counter = BitCounter(oxygen_input)
    oxygen_pattern = ""
    for i in range(oxygen_counter.n_bits()):
        most_common = oxygen_counter.get_most_common_bits()
        oxygen_pattern += most_common[i]
        oxygen_input = [
            line for line in oxygen_input if line.startswith(oxygen_pattern)
        ]
        if len(oxygen_input) == 1:
            return int(oxygen_input[0], 2)
        oxygen_counter = BitCounter(oxygen_input)


def get_co2_rate(input: List[str]) -> int:
    co2_input = input
    co2_counter = BitCounter(co2_input)
    co2_pattern = ""
    for i in range(co2_counter.n_bits()):
        least_common = co2_counter.get_least_common_bits()
        co2_pattern += least_common[i]
        co2_input = [line for line in co2_input if line.startswith(co2_pattern)]
        if len(co2_input) == 1:
            return int(co2_input[0], 2)
        co2_counter = BitCounter(co2_input)


power_counter = BitCounter(INPUT)

assert get_gamma(power_counter) == 22
assert get_epsilon(power_counter) == 9
assert get_oxygen_rate(INPUT) == 23
assert get_co2_rate(INPUT) == 10


if __name__ == "__main__":
    with open("data/day03.txt") as f:
        data = f.read()
        input = data.splitlines()
        power_counter = BitCounter(input)
        print(get_gamma(power_counter) * get_epsilon(power_counter))
        print(get_oxygen_rate(input) * get_co2_rate(input))
