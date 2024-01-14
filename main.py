# Function to generate all possible secret codes
from verifiers.V04 import V04
from verifiers.V09 import V09
from verifiers.V11 import V11
from verifiers.V14 import V14
from verifiers.V17 import V17
from verifiers.v13 import V13


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
    if number == 4:
        return V04()
    if number == 9:
        return V09()
    if number == 11:
        return V11()
    if number == 13:
        return V13()
    if number == 14:
        return V14()
    if number == 17:
        return V17()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solve(4,9,11,14)
