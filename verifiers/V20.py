from Constants import *
from verifiers.Verifier import Verifier


class V20(Verifier):
    solutions = [0, 0, 0]

    def test(self, number, code):
        if number == 0:
            return allTheSame(code)
        if number == 1:
            return not allTheSame(code) and not allDifferent(code)
        if number == 2:
            return allDifferent(code)
    def number_criteria(self):
        return 3

def allTheSame(code):
    return code[BLUE] == code[YELLOW] and code[BLUE] == code[PURPLE]

def allDifferent(code):
    return code[BLUE] != code[YELLOW] and code[BLUE] != code[PURPLE] and code[YELLOW] != code[PURPLE]
