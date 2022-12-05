from pathlib import Path

import numpy as np
import re
from notebooks.advent_of_code_2022.day1 import load_plain_txt


def load_data(path_input):
    plain_txt = load_plain_txt(path_input)

    init_positions, instructions = Path(path_input).read_text().split("\n\n")
    init_positions_split = init_positions.split("\n")
    lenght = 4
    split_by = [[init[y-lenght:y].strip('[] ') for y in range(lenght, len(init)+lenght,lenght)] for init in init_positions_split]
    split_by.reverse()

    #instructions
    instructions_split = instructions.split('\n')

    return np.array([np.array(x) for x in split_by]), instructions_split


class Stack:
    def __init__(self, init_positions: np.ndarray):

        self.id = init_positions[0]
        self.crates =[]
        for init in init_positions[1:]:
            if init != '':
                self.crates.append(init)


class Instruction:
    def __init__(self, init: str):
        split_init = init.split(" ")

        self.number = int(split_init[1])
        self.move_from = int(split_init[3])
        self.move_to = int(split_init[5])



class Warehouse:
    def __init__(self, init_positions: np.ndarray):

        nb_stack = init_positions.shape[1]

        self.stacks = [Stack(init_positions[:, i]) for i in range(nb_stack)]

    def apply_instruction(self, ins: Instruction, reverse_order: bool) -> None:

        # take n last from 'from_pile'
        crates_to_move = self.stacks[ins.move_from - 1].crates[-ins.number:]

        if reverse_order:
            crates_to_move.reverse()

        # append it to - reverse the order
        self.stacks[ins.move_to - 1].crates.extend(crates_to_move)

        # delete it
        self.stacks[ins.move_from -1].crates = self.stacks[ins.move_from -1].crates[:-ins.number]

    def print_result_1(self):
        data = [stack.crates[-1] for stack in self.stacks]
        buffer = ''
        for d in data:
            buffer = buffer + d
        print(buffer)


if __name__ == "__main__":
    path_input = 'input_5.txt'
    init_positions, instructions = load_data(path_input)

    warehouse = Warehouse(init_positions)
    for ins in instructions:
        if ins != '':
            warehouse.apply_instruction(Instruction(ins,), True)

    warehouse.print_result_1()

    warehouse = Warehouse(init_positions)
    for ins in instructions:
        if ins != '':
            warehouse.apply_instruction(Instruction(ins, ), False)

    warehouse.print_result_1()
