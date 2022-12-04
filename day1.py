from itertools import groupby


def load_plain_txt(path: str) -> list:
    with open(path, 'r') as f:
        return f.readlines()


class Elf:
    def __init__(self,
                 id: int,
                 food_calories: list[int]):
        self.id = id
        self.food_calories = food_calories

    @property
    def total_food_carried(self):
        return sum(self.food_calories)


def load_data(data_path: str):
    plain_txt = load_plain_txt(data_path)
    data_strip = [int(line.strip()) if line.strip() != '' else '' for line in plain_txt]
    return [list(group) for k, group in groupby(data_strip, lambda x: x == "") if not k]


def sum_food_for_elves(sorted_elves: list[Elf], number_of_elves: int) -> int:
    count = 0
    for i, elf in enumerate(sorted_elves):
        count = count + elf.total_food_carried
        if i+1 == number_of_elves:
            return count


if __name__ == "__main__":
    data_path = 'input.txt'
    data = load_data(data_path)

    elves = [Elf(i, data) for i, data in enumerate(data)]

    sorted_elves = sorted(elves, key=lambda x: x.total_food_carried, reverse=True)

    # example 1: most elf
    print(f'question 1: {sorted_elves[0].total_food_carried}')

    # example 2: three most
    print(f'question 2: {sum_food_for_elves(sorted_elves, 3)}')