#!/usr/bin/python3

import re
from dataclasses import dataclass
from typing import Optional

with open("Day02Input.txt", "r") as f:
    instructions = f.read()

@dataclass
class Movement():
    direction: str
    distance: int

@dataclass
class CoOrd():
    x: int
    depth: int

def parse_instruction(instruction: str) -> Movement:
    m = re.match(r"(forward|down|up) (\d+)", instruction)
    if m:
        movement = Movement(direction=m.group(1), distance=int(m.group(2)))
    else:
        print(f"Unexpected instruction {instruction}")
        exit(1)
    return movement

def movement_part1():
    location = CoOrd(x=0,depth=0)
    for line in instructions.split("\n"):
        movement = parse_instruction(line)
        if movement.direction == "forward":
            location.x += movement.distance
        elif movement.direction == "up":
            location.depth -= movement.distance
        elif movement.direction == "down":
            location.depth += movement.distance
        else:
            raise ValueError("Invalid movement direction")

    print(f"Depth is {location.depth}, distsance is {location.x}")
    print(f"The product of those is {location.depth * location.x}")

@dataclass
class CoOrd2():
    x: int
    depth: int
    aim: int

def movement_part2():
    location = CoOrd2(x=0,depth=0, aim=0)
    for line in instructions.split("\n"):
        movement = parse_instruction(line)
        if movement.direction == "forward":
            location.x += movement.distance
            location.depth += movement.distance * location.aim
        elif movement.direction == "up":
            location.aim -= movement.distance
        elif movement.direction == "down":
            location.aim += movement.distance
        else:
            raise ValueError("Invalid movement direction")

    print(f"Depth is {location.depth}, distsance is {location.x}")
    print(f"The product of those is {location.depth * location.x}")

movement_part1()
movement_part2()
