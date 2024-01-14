from verifiers.Verifier import Verifier
from Constants import *


class V11(Verifier):
    solutions = [0, 0, 0]

    def test(self, number, code):
        if number == 0:
            return code[BLUE] < code[YELLOW]
        if number == 1:
            return code[BLUE] == code[YELLOW]
        if number == 2:
            return code[BLUE] > code[YELLOW]

    def number_criteria(self):
        return 3
