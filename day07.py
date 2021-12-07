from statistics import median, mean


RAW = "16,1,2,0,4,2,7,1,2,14"


def fuel(raw: str, constant: bool = True) -> int:
    crabs = [int(x) for x in raw.split(",")]
    if constant:
        level = int(median(crabs))
        return sum(abs(x - level) for x in crabs)
    else:
        # for input data mean is 489.501 but should be rounded down to get right answer
        level = round(mean(crabs))
        return sum(sum(range(abs(x - level) + 1)) for x in crabs)


assert fuel(RAW) == 37
assert fuel(RAW, constant=False) == 168


if __name__ == "__main__":
    with open("data/day07.txt") as f:
        raw = f.read()
        print(fuel(raw))
        print(fuel(raw, constant=False))
