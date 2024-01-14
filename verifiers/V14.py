from Constants import *
from verifiers.Verifier import Verifier


class V14(Verifier):
    solutions = [0, 0, 0]

    def test(self, number, code):
        if number == 0:
            return code[BLUE] < code[YELLOW] and code[BLUE] < code[PURPLE]
        if number == 1:
            return code[YELLOW] < code[BLUE] and code[YELLOW] < code[PURPLE]
        if number == 2:
            return code[PURPLE] < code[YELLOW] and code[PURPLE] < code[BLUE]

    def number_criteria(self):
        return 3
