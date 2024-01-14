from Constants import *


def count(code, number):
    counter = 0
    if code[BLUE] == number:
        counter += 1
    if code[YELLOW] == number:
        counter += 1
    if code[PURPLE] == number:
        counter += 1
    return counter


def sum_all(code):
    return code[BLUE] + code[YELLOW] + code[PURPLE]