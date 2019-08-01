"""
Given a string as input, return the list of all the patterns possible:

'1' : ['A', 'B', 'C'],
'2' : ['D', 'E'],
'12' : ['X']
'3' : ['P', 'Q']

Example if input is '123', then output should be
[ADP, ADQ, AEP, AEQ, BDP, BDQ, BEP, BEQ, CDP, CDQ, CEP, CEQ, XP, XQ]

"""


def generate_patterns(data, digits):
    if not data or not digits:
        return []

    combinations = ['']
    for i in range(len(digits)):
        candidates = data[digits[i]]

        temp_combinations = []
        for candidate in candidates:
            for j in range(len(combinations)):
                temp_combinations.append(combinations[j] + candidate)

        combinations = temp_combinations

    return combinations


if __name__ == '__main__':
    data = {'1' : ['A', 'B', 'C'], '2' : ['D', 'E'], '12' : ['X'], '3' : ['P', 'Q']}
    digits = '123'

    print(generate_patterns(data, digits))