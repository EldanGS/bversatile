def solution(S):
    char_set = set(S)
    candidate = None

    for c in S:
        if c.lower() in char_set and c.upper() in char_set:
            if not candidate:
                candidate = c.upper()
            candidate = max(candidate, c.upper())

    return candidate if candidate else "NO"
