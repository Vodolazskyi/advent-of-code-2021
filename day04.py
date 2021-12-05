from typing import List, Union


RAW = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


class Board:
    WIN_SETS = (
        {0, 1, 2, 3, 4},
        {5, 6, 7, 8, 9},
        {10, 11, 12, 13, 14},
        {15, 16, 17, 18, 19},
        {20, 21, 22, 23, 24},
        {0, 5, 10, 15, 20},
        {1, 6, 11, 16, 21},
        {2, 7, 12, 17, 22},
        {3, 8, 13, 18, 23},
        {4, 9, 14, 19, 24},
    )

    def __init__(self, rows: List[int]) -> None:
        self.rows = rows
        self.marked_indices = set()
        self.sum = sum(sum(row) for row in self.rows)

    def mark_number(self, number: int) -> None:
        for i, row in enumerate(self.rows):
            if number in row:
                self.marked_indices.add(row.index(number) + i * 5)
                self.sum -= number
                break

    def is_win(self) -> bool:
        return any(win_set.issubset(self.marked_indices) for win_set in self.WIN_SETS)

    def get_remain_sum(self) -> int:
        return self.sum


INPUT = RAW.splitlines()


def get_numbers_and_boards(input: List[str]) -> Union[List[int], List[Board]]:
    numbers = [int(x) for x in input[0].split(",")]
    boards = []
    temp_rows = []
    for line in input[2:]:
        if line == "":
            boards.append(Board(temp_rows))
            temp_rows = []
        else:
            temp_rows.append([int(x) for x in line.split()])
    boards.append(Board(temp_rows))

    return numbers, boards


def get_first_win_score(input: List[str]) -> int:
    numbers, boards = get_numbers_and_boards(input)
    for number in numbers:
        for board in boards:
            board.mark_number(number)
            if board.is_win():
                return board.get_remain_sum() * number


def get_last_win_score(input: List[str]) -> int:
    numbers, boards = get_numbers_and_boards(input)
    win_boards = []
    for number in numbers:
        if not boards:
            break
        for board in boards:
            board.mark_number(number)
            if board.is_win():
                score = board.get_remain_sum() * number
                win_boards.append(board)
        if win_boards:
            boards = [board for board in boards if board not in win_boards]
            win_boards = []
    return score


assert get_first_win_score(INPUT) == 4512
assert get_last_win_score(INPUT) == 1924


if __name__ == "__main__":
    with open("data/day04.txt") as f:
        input = f.read().splitlines()
        print(get_first_win_score(input))
        print(get_last_win_score(input))
