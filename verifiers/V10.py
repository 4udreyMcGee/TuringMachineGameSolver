from verifiers import utils

from verifiers.Verifier import Verifier


class V10(Verifier):
    solutions = [0, 0, 0]

    def test(self, number, code):
        sum = utils.count(code, 4)
        if number == 0:
            return sum == 0
        if number == 1:
            return sum == 1
        if number == 2:
            return sum == 2

    def number_criteria(self):
        return 3
