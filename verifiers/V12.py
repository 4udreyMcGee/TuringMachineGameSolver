from Constants import *
from verifiers.Verifier import Verifier


class V12(Verifier):
    solutions = [0, 0, 0]

    def test(self, number, code):
        if number == 0:
            return code[BLUE] < code[PURPLE]
        if number == 1:
            return code[BLUE] == code[PURPLE]
        if number == 2:
            return code[BLUE] > code[PURPLE]

    def number_criteria(self):
        return 3
