# Function to generate all possible secret codes
from verifiers.V01 import V01
from verifiers.V02 import V02
from verifiers.V03 import V03
from verifiers.V04 import V04
from verifiers.V05 import V05
from verifiers.V06 import V06
from verifiers.V07 import V07
from verifiers.V08 import V08
from verifiers.V09 import V09
from verifiers.V10 import V10
from verifiers.V11 import V11
from verifiers.V12 import V12
from verifiers.V13 import V13
from verifiers.V14 import V14
from verifiers.V15 import V15
from verifiers.V16 import V16
from verifiers.V17 import V17
from verifiers.V18 import V18
from verifiers.V19 import V19
from verifiers.V20 import V20


def generate_secret_codes():
    codes = []
    for i in range(1, 6):
        for j in range(1, 6):
            for k in range(1, 6):
                codes.append((i, j, k))
    return codes


def solve(num1, num2, num3, num4):
    allCodes = generate_secret_codes()
    code_dict = {}
    for code in allCodes:
        code_dict[code] = {"number_1": code[0],
                           "number_2": code[1],
                           "number_3": code[2],
                           "solution_count": 0}

    vA = getVerifier(num1)
    vB = getVerifier(num2)
    vC = getVerifier(num3)
    vD = getVerifier(num4)

    for a in range(vA.number_criteria()):
        for b in range(vB.number_criteria()):
            for c in range(vC.number_criteria()):
                for d in range(vD.number_criteria()):
                    codes = []
                    for code in code_dict:
                        if vA.test(a, code) and vB.test(b, code) and vC.test(c, code) and vD.test(d, code):
                            print(f"found {code}")
                            codes.append((code, a,b,c,d))
                    if len(codes) == 1:
                        code_dict[codes[0][0]]["solution_count"] = code_dict[codes[0][0]]["solution_count"] + 1
                        vA.solutions[a] = vA.solutions[a] + 1
                        vB.solutions[b] = vB.solutions[b] + 1
                        vC.solutions[c] = vC.solutions[c] + 1
                        vD.solutions[d] = vD.solutions[d] + 1

    solutions = {}
    for code in code_dict:
        if code_dict[code]["solution_count"] != 0:
            solutions[code] = code_dict[code]
    code_dict = solutions

    print(code_dict.keys())
    print(len(code_dict.keys()))
    print(vA.solutions)
    print(vB.solutions)
    print(vC.solutions)
    print(vD.solutions)
    return code_dict


def getVerifier(number):
    if number == 1:
        return V01()
    if number == 2:
        return V02()
    if number == 3:
        return V03()
    if number == 4:
        return V04()
    if number == 5:
        return V05()
    if number == 6:
        return V06()
    if number == 7:
        return V07()
    if number == 8:
        return V08()
    if number == 9:
        return V09()
    if number == 10:
        return V10()
    if number == 11:
        return V11()
    if number == 12:
        return V12()
    if number == 13:
        return V13()
    if number == 14:
        return V14()
    if number == 15:
        return V15()
    if number == 16:
        return V16()
    if number == 17:
        return V17()
    if number == 18:
        return V18()
    if number == 19:
        return V19()
    if number == 20:
        return V20()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solve(4,9,11,14)
