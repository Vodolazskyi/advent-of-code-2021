RAW = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

CHAR_CORRUPTED_POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
CHAR_COMPLETED_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}
CHAR_PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}


def score_corrupted_lines(raw: str) -> int:
    lines = raw.splitlines()
    score = 0
    for line in lines:
        stack = []
        for char in line:
            if char in CHAR_PAIRS:
                stack.append(char)
            elif CHAR_PAIRS[stack.pop()] != char:
                score += CHAR_CORRUPTED_POINTS[char]
                break
    return score


def score_incomplete_lines(raw: str) -> int:
    lines = raw.splitlines()
    points = []
    for line in lines:
        is_corrupted = False
        stack = []
        for char in line:
            if char in CHAR_PAIRS:
                stack.append(char)
            elif CHAR_PAIRS[stack.pop()] != char:
                is_corrupted = True
                break
            else:
                continue
        if not is_corrupted:
            score = 0
            for char in stack[::-1]:
                score *= 5
                score += CHAR_COMPLETED_POINTS[CHAR_PAIRS[char]]
            points.append(score)
    median_index = round(len(points) / 2)
    return sorted(points)[median_index]


assert score_corrupted_lines(RAW) == 26397
assert score_incomplete_lines(RAW) == 288957


if __name__ == "__main__":
    with open("data/day10.txt") as f:
        raw = f.read()
        print(score_corrupted_lines(raw))
        print(score_incomplete_lines(raw))
