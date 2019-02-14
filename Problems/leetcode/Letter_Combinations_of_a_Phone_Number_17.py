# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/


# O(2^N) time, O(2^N) space
class Solution:
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        if not digits:
            return []

        phone_number_chars = [None, None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        combinations = ['']
        for i in range(len(digits)):
            candidates = phone_number_chars[int(digits[i])]
            if not candidates:
                continue

            temporary_combinations = []
            for candidate in candidates:
                for j in range(len(combinations)):
                    temporary_combinations.append(combinations[j] + candidate)

            combinations = temporary_combinations

        return combinations
