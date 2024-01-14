from verifiers.Verifier import Verifier
from verifiers.utils import count


class V17(Verifier):
    solutions = [0, 0, 0, 0]

    def test(self, number, code):
        even = count(code, 2) + count(code, 4)
        if number == 0:
            return even == 0
        if number == 1:
            return even == 1
        if number == 2:
            return even == 2
        if number == 3:
            return even == 3

    def number_criteria(self):
        return 4
