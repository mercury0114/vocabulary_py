from math import sqrt
from os import listdir
from os.path import join
from random import choice

HINT = "h"
QUIT = "q"
INITIAL_SCORE = 5
GOOD_SCORE = 10
MAX_SCORE = 15
NEXT_QUESTION_INDEX = -1


def close_words(user_input, answer):
    min_length = min(len(user_input), len(answer))
    return sum(user_input[i] != answer[i] for i in range(min_length)) + \
        abs(len(user_input) - len(answer)) < 3


def get_file_score(f):
    scores = ReadDataFromFile(f).values()
    score_sum = sum([sqrt(s[0]) + sqrt(s[1]) for s in scores])
    return score_sum / (len(scores) * 2)


def lowest_score_file(folder):
    return min(listdir(folder), key=lambda f: get_file_score(join(folder, f)))


def select_question_answer(word_pair, argument):
    question_index = choice([0, 1]) if argument == 2 else argument
    return word_pair[question_index], word_pair[not question_index]


def write_open(file_path):
    return open(file_path, "w", encoding='UTF-8')


def read_open(file_path):
    return open(file_path, encoding='UTF-8')


def ReadDataFromFile(file_path, read_all_words=True):
    statistics = {}
    open_file = read_open(file_path)
    for line in open_file:
        columns = line.split(', ')
        words = (columns[0], columns[1].strip('\n'))
        score1 = INITIAL_SCORE if len(columns) < 3 else int(columns[2])
        score2 = INITIAL_SCORE if len(columns) < 4 else int(columns[3])
        if read_all_words or score1 <= GOOD_SCORE or score2 <= GOOD_SCORE:
            statistics[words] = [score1, score2]
        else:
            print("You know {}".format(line))
    open_file.close()
    return statistics


def ReadPairsFromFile(file_path):
    return list(ReadDataFromFile(file_path).keys())
