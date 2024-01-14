from verifiers.Verifier import Verifier
from verifiers.utils import sum_all


class V18(Verifier):
    solutions = [0, 0]

    def test(self, number, code):
        if number == 0:
            return sum_all(code) % 2 == 0
        if number == 1:
            return sum_all(code) % 2 == 1
    def number_criteria(self):
        return 2
