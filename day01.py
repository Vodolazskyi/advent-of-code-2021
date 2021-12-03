RAW = """
199
200
208
210
200
207
240
269
260
263
"""


INPUT = [int(x) for x in RAW.split()]


def count_increases(depths: list, gap: int = 1) -> int:
    return sum(depths[i] < depths[i + gap] for i in range(len(depths) - gap))


assert count_increases([1, 2, 3]) == 2
assert count_increases(INPUT) == 7
assert count_increases(INPUT, gap=3) == 5

if __name__ == "__main__":
    with open("data/day01.txt") as f:
        data = f.read()
        depths = [int(x) for x in data.split()]
        print(count_increases(depths))
        print(count_increases(depths, gap=3))
