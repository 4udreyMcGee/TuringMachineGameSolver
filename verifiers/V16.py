from verifiers.Verifier import Verifier
from verifiers.utils import count


class V16(Verifier):
    solutions = [0, 0]

    def test(self, number, code):
        even = count(code, 2) + count(code, 4)
        if number == 0:
            return even == 2
        if number == 1:
            return even <= 1

    def number_criteria(self):
        return 2
