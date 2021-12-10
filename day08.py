from typing import List


RAW = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def count_unique_digits(input: List[str]) -> int:
    digits = input.split()
    return sum(len(digit) in (2, 3, 4, 7) for digit in digits)


INPUT = [line.split("|")[1] for line in RAW.splitlines()]

assert sum(count_unique_digits(line) for line in INPUT) == 26


class Decoder:
    def __init__(self, digits: List[str]) -> None:
        self.dict_str = {}
        self.dict_int = {}
        for digit in digits:
            match len(digit):
                case 2:
                    self.update_dicts(digit, 1)
                case 3:
                    self.update_dicts(digit, 7)
                case 4:
                    self.update_dicts(digit, 4)
                case 7:
                    self.update_dicts(digit, 8)
        for digit in digits:
            if digit not in self.dict_str:
                match len(set(digit) ^ set(self.dict_int[1])):
                    case 3:
                        self.update_dicts(digit, 3)
                    case 6:
                        self.update_dicts(digit, 6)
                match len(set(digit) ^ set(self.dict_int[4])):
                    case 5:
                        self.update_dicts(digit, 2)
                    case 2:
                        self.update_dicts(digit, 9)
        for digit in digits:
            if digit not in self.dict_str:
                match len(digit):
                    case 5:
                        self.update_dicts(digit, 5)
                    case 6:
                        self.update_dicts(digit, 0)

    def update_dicts(self, digit_str: str, digit_int: int) -> None:
        self.dict_str[digit_str] = digit_int
        self.dict_int[digit_int] = digit_str

    def get_digit_int(self, digit_str: str) -> int:
        for digit in self.dict_str:
            if set(digit) == set(digit_str):
                return self.dict_str[digit]


if __name__ == "__main__":
    with open("data/day08.txt") as f:
        raw = f.readlines()
        input = [line.split("|")[1] for line in raw]
        print(sum(count_unique_digits(line) for line in input))
        sum = 0
        for line in raw:
            encode_list = line.split("|")[0]
            decode_list = line.split("|")[1]
            decoder = Decoder([d for d in encode_list.split()])
            display = ''.join([
                str(decoder.get_digit_int(digit)) for digit in decode_list.split()
            ])
            sum += int(display)
        print(sum)
