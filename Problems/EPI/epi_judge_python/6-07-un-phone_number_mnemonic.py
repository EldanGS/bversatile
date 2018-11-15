from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number):

    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "6-07-un-phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
