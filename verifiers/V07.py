from verifiers.Verifier import Verifier
from Constants import *


class V07(Verifier):
    solutions = [0, 0]
    def test(self, number, code):
        if number == 0:
            return code[PURPLE] % 2 == 0
        if number == 1:
            return code[PURPLE] % 2 == 1

    def number_criteria(self):
        return 2
