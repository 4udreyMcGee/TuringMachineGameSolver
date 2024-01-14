from verifiers.Verifier import Verifier
from Constants import *


class V03(Verifier):
    solutions = [0, 0, 0]

    def test(self, number, code):
        if number == 0:
            return code[YELLOW] < 3
        if number == 1:
            return code[YELLOW] == 3
        if number == 2:
            return code[YELLOW] > 3

    def number_criteria(self):
        return 3
