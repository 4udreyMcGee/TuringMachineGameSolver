from verifiers.Verifier import Verifier
from Constants import *


class V04(Verifier):
    solutions = [0, 0, 0]

    def test(self, number, code):
        if number == 0:
            return code[YELLOW] < 4
        if number == 1:
            return code[YELLOW] == 4
        if number == 2:
            return code[YELLOW] > 4

    def number_criteria(self):
        return 3
