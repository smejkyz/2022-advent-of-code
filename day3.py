import numpy as np

from notebooks.advent_of_code_2022.advent import load_plain_txt


def load_data(file: str):
    plain_txt = load_plain_txt(file)
    return [line.strip() for line in plain_txt]


def priority(char: str) -> int:
    if len(char) != 1:
        ValueError('wrong')
    add = 0 if char.islower() else 26
    return ord(char.lower()) - 96 + add


class Bag:
    def __init__(self, list_of_content: str):

        halve = len(list_of_content) // 2

        self.complete = list_of_content
        self.first_compartment = list_of_content[:halve]
        self.second_compartment = list_of_content[halve:]

    @property
    def common_items(self):
        return list(set(self.first_compartment) & set(self.second_compartment))


class Group:
    def __init__(self,data: np.ndarray):
        data = data.flatten()
        self.first = data[0]
        self.second = data[1]
        self.third = data[2]

    @property
    def common_item(self):
        return list(set(self.first) & set(self.second) & set(self.third))


if __name__ == "__main__":
    path_file = 'input_3.txt'
    data = load_data(path_file)

    # first
    bags = [Bag(line) for line in data]
    common_items = [item for bag in bags for item in bag.common_items]
    priorities = [priority(item) for item in common_items]
    print(sum(priorities))

    #second divide to three
    data_by_three = np.array_split(np.array(data), len(data)//3)
    groups = [Group(da) for da in data_by_three]
    common_items = [item for group in groups for item in group.common_item]
    priorities = [priority(item) for item in common_items]
    print(sum(priorities))
