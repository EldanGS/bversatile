"""
This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""


def justify_text(words, k):
    result = []
    begin, n = 0, len(words)
    while begin < n:
        last, line_len = begin, len(words[begin])
        begin += 1
        while begin < n and line_len + 1 + len(words[begin]) <= k:
            line_len += len(words[begin]) + 1
            begin += 1

        spaces, extra = 1, 0
        if begin < n and begin != last + 1:
            spaces = (k - line_len) // (begin - last - 1) + 1
            extra = (k - line_len) % (begin - last - 1)

        result.append(words[last])
        last += 1
        while extra != 0:
            result[-1] += ' ' * (spaces + 1)
            result[-1] += words[last]
            extra, last = extra - 1, last + 1
        while last < begin:
            result[-1] += ' ' * spaces
            result[-1] += words[last]
            last += 1
        result[-1] += ' ' * (k - len(result[-1]))

    return result


if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
             "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    # k = 16
    k = 20
    print('Words:', words)
    print(justify_text(words, k))
