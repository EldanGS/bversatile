from test_framework import generic_test, test_utils

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')


def phone_mnemonic(phone_number):
    def helper(digit):
        if digit == len(phone_number):
            mnemonics.append(''.join(partial_mnemonic))
        else:
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                helper(digit + 1)

    mnemonics, partial_mnemonic = [], [0] * len(phone_number)
    helper(0)
    return mnemonics


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "06-07-phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
