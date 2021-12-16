from collections import Counter, defaultdict


RAW = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


class Polymer:
    def __init__(self, template: str, insertion_rules: dict) -> None:
        self.template = defaultdict(int)
        for i in range(len(template) - 1):
            self.template[template[i : i + 2]] += 1
        self.insertion_rules = insertion_rules

    @staticmethod
    def parse(raw: str) -> "Polymer":
        template = raw.split("\n\n")[0]
        insertion_rules = {
            line.split(" -> ")[0]: line.split(" -> ")[1]
            for line in raw.split("\n\n")[-1].splitlines()
        }
        return Polymer(template, insertion_rules)

    def step(self) -> None:
        new_pairs = defaultdict()
        for pair, count in self.template.items():
            new_pairs[pair[0] + self.insertion_rules[pair]] += count
            new_pairs[self.insertion_rules[pair] + pair[1]] += count
        for pair, count in new_pairs.items():
            self.template[pair] += count

    def score(self) -> int:
        counter = Counter(self.template)
        counts = counter.most_common()
        return counts[0][-1] - counts[-1][-1]


pol = Polymer.parse(RAW)
for _ in range(10):
    pol.step()

assert pol.score() == 1588


if __name__ == "__main__":
    with open("data/day14.txt") as f:
        raw = f.read()
        pol = Polymer.parse(raw)
        for _ in range(10):
            pol.step()
        print(pol.score())
        for _ in range(40 - 10):
            pol.step()
        print(pol.score())
