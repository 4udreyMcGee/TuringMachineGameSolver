from verifiers.Verifier import Verifier
from Constants import *


class V05(Verifier):
    solutions = [0, 0]
    def test(self, number, code):
        if number == 0:
            return code[BLUE] % 2 == 0
        if number == 1:
            return code[BLUE] % 2 == 1

    def number_criteria(self):
        return 2
