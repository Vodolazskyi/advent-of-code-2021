from dataclasses import dataclass


RAW = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


INPUT = [x for x in RAW.strip().splitlines()]


@dataclass
class Command:
    direction: str
    distance: int

    @staticmethod
    def from_string(s: str):
        direction, distance = s.split()
        return Command(direction, int(distance))


@dataclass
class Position:
    horizontal: int = 0
    depth: int = 0

    def move(self, command: Command):
        if command.direction == "forward":
            self.horizontal += command.distance
        elif command.direction == "up":
            self.depth -= command.distance
        elif command.direction == "down":
            self.depth += command.distance


@dataclass
class AimPosition:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0

    def move(self, command: Command):
        if command.direction == "forward":
            self.horizontal += command.distance
            self.depth += self.aim * command.distance
        elif command.direction == "up":
            self.aim -= command.distance
        elif command.direction == "down":
            self.aim += command.distance


position = Position()
aim_position = AimPosition()
for line in INPUT:
    command = Command.from_string(line)
    position.move(command)
    aim_position.move(command)


assert position.horizontal == 15
assert position.depth == 10
assert aim_position.horizontal == 15
assert aim_position.depth == 60


if __name__ == "__main__":
    position = Position()
    aim_position = AimPosition()
    with open("data/day02.txt") as f:
        commands = f.readlines()
        for command in commands:
            position.move(Command.from_string(command))
            aim_position.move(Command.from_string(command))
    print(position.horizontal * position.depth)
    print(aim_position.horizontal * aim_position.depth)
