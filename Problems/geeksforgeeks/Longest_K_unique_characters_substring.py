# https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/


def is_valid_substr(entity_count, k):
    return k >= len([val for val in entity_count.values() if val > 0])


def longest_k_unique_characters_substr(s, k):
    if not s or len(set([c for c in s])) < k:
        return -1

    entity_count = {s[0]: 1}
    longest_substr, substr_start, start = 0, -1, 0
    for end in range(1, len(s)):
        entity_count[s[end]] = entity_count.get(s[end], 0) + 1

        while not is_valid_substr(entity_count, k):
            entity_count[s[start]] -= 1
            start += 1

        if longest_substr < end - start + 1:
            longest_substr = end - start + 1
            substr_start = start  # for print substring

    return longest_substr


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        s = input()
        k = int(input())

        print(longest_k_unique_characters_substr(s, k))
