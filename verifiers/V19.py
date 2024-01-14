from Constants import *
from verifiers.Verifier import Verifier
from verifiers.utils import sum_all


class V19(Verifier):
    solutions = [0, 0, 0]

    def test(self, number, code):
        if number == 0:
            return code[BLUE] + code[YELLOW] < 6
        if number == 1:
            return code[BLUE] + code[YELLOW] == 6
        if number == 2:
            return code[BLUE] + code[YELLOW] > 6
    def number_criteria(self):
        return 3
