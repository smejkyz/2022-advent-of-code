from notebooks.advent_of_code_2022.advent import load_plain_txt


def load_data(path: str) -> list:
    plain_txt = load_plain_txt(path)
    return [line.strip().split(',')  for line in plain_txt]


class Section:
    def __init__(self, input: str):
        self.input = input
        split = input.split("-")
        self.start = int(split[0])
        self.end = int(split[1])

    @property
    def section_range(self):
        return set(i for i in range(self.start, self.end+1))


def is_fully_contain(first: Section, second: Section):
    # first is fully in second
    condition_1 = first.start >= second.start and first.end <= second.end

    # or second is fully in first
    condition_2 = second.start >= first.start and second.end <= first.end

    return condition_1 | condition_2


def there_is_overlap(first: Section, second: Section):

    overlap = first.section_range & second.section_range
    if len(overlap) == 0:
        return False
    return True


if __name__ == "__main__":
    input_file = "day4.txt"
    data = load_data(input_file)
    pair_of_sections = [(Section(line[0]), Section(line[1])) for line in data]
    are_fully_contain = [is_fully_contain(*pair) for pair in pair_of_sections ]
    print(sum(are_fully_contain))

    are_overlap = [there_is_overlap(*pair) for pair in pair_of_sections]
    print(sum(are_overlap))