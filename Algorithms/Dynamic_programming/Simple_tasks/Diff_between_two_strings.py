"""
Diff Between Two Strings task
On the Internet, I recently came across an interesting task. I share with you its decision.

Task Description Given two strings of uppercase letters source and target,
list (in string form) a sequence of edits to convert from source to
targetthat uses the least edits possible. For example, with strings source =
"ABCDEFG", and target = "ABDFFGH" we might return: ["A", "B", "-C", "D",
"-E", "F", "+F", "G", "+H" More formally, for each character C in source,
we will either write the token C, which does not count as an edit; or write
the token -C, which counts as an edit. Additionally, between any token that
we write, we may write +D where D is any letter, which counts as an edit. At
the end, when reading the tokens from left to right, and not including tokens
prefixed with a minus-sign, the letters should spell out target (when
ignoring plus-signs.) In the example, the answer of A B -C D -E F +F G +H has
total number of edits 4 (the minimum possible), and ignoring
subtraction-tokens, spells out A, B, D, F, +F, G, +H which represents the
string target. If there are multiple answers, use the answer that favors
removing from the source first. Constraints: [time limit] 5000ms [input]
string source 2 ≤ source.length ≤ 12 [input] string target 2 ≤ target.length
≤ 12 [output] array.string

"""


def diff_between_two_strings(source, target):
    n, m = len(source), len(target)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if source[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    result = []
    while n > 0 and m > 0:
        if source[n - 1] == target[m - 1]:
            result.append(source[n - 1])
            n, m = n - 1, m - 1
        else:
            if dp[n][m] == dp[n][m - 1] + 1:  # add
                result.append("+" + target[m - 1])
                m -= 1
            elif dp[n][m] == dp[n - 1][m] + 1:  # removing
                result.append("-" + source[n - 1])
                n -= 1

    while n > 0:
        result.append('-' + source[n - 1])
        n -= 1

    while m > 0:
        result.append('+' + target[m - 1])
        m -= 1

    return result[::-1]

