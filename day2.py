from notebooks.advent_of_code_2022.advent import load_plain_txt


def load_data(data_path):
    plain_txt = load_plain_txt(data_path)
    txt_strip = [line.strip().split(" ") for line in plain_txt]
    return txt_strip



def score_what_I_choose(choice: str):
    match choice:
        case "Y":  # paper
            return 2
        case "X":  # rock
            return 1
        case "Z": # scissors
            return 3
        case _:
            ValueError("unknown value")


def compute_result(oponent_chooses: str, i_chooses:  str):
    if oponent_chooses == "A":
        # rock
        match i_chooses:
            case "Y":  # paper
                return 6
            case "X":  # rock
                return 3
            case "Z":  # scissors
                return 0

    if oponent_chooses == "B":
        # paper
        match i_chooses:
            case "Y":  # paper
                return 3
            case "X":  # rock
                return 0
            case "Z":  # scissors
                return 6

    if oponent_chooses == "C":
        # scissors
        match i_chooses:
            case "Y":  # paper
                return 0
            case "X":  # rock
                return 6
            case "Z":  # scissors
                return 3


def compute_score(oponent_chooses: str, i_chooses:  str):
    my_score = score_what_I_choose(i_chooses)

    result = compute_result(oponent_chooses, i_chooses)

    return result + my_score


def compute_score_II(oponent_chooses: str, result_of_the_game:  str):

    result, what_i_choose = compute_result_II(oponent_chooses, result_of_the_game)

    my_score = score_what_I_choose(what_i_choose)

    return result + my_score


def compute_result_II(oponent_chooses: str, result:  str):
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
    if oponent_chooses == "A":
        # rock
        match result:
            case "Y":  # draw
                return 3, "X"
            case "X":  # lose => scirre
                return 0, "Z"
            case "Z":  # win
                return 6, "Y"

    if oponent_chooses == "B":
        # paper
        match result:
            case "Y":  # draw
                return 3, "Y"
            case "X":  # lose
                return 0, "X"
            case "Z":  # win
                return 6, "Z"

    if oponent_chooses == "C":
        # scissors
        match result:
            case "Y":  # draw
                return 3, "Z"
            case "X":  # lose
                return 0, "Y"
            case "Z":  # win
                return 6, "X"


if __name__ == "__main__":
    data_path = 'day2.txt'
    data = load_data(data_path)
    score = 0
    for line in data:
        score = score + compute_score(line[0], line[1])

    print(score)

    score = 0
    for line in data:
        score = score + compute_score_II(line[0], line[1])

    print(score)