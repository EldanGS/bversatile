from test_framework import generic_test


# O(N * M) space and time
def num_combinations_for_final_score(final_score, individual_play_scores):
    num_combinations = [[1] + [0] * final_score for _ in individual_play_scores]
    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            without_current_player = num_combinations[i - 1][j] if i >= 1 else 0
            with_current_player = (num_combinations[i][j - individual_play_scores[i]]
                                   if j >= individual_play_scores[i] else 0)
            num_combinations[i][j] = without_current_player + with_current_player

    return num_combinations[-1][-1]


# O(N * M) time, O(M) space
def num_combinations_for_final_score(final_score, individual_play_scores):
    num_combinations = [1] + [0] * final_score
    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            if j >= individual_play_scores[i]:
                num_combinations[j] += num_combinations[j - individual_play_scores[i]]

    return num_combinations[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("16-01-number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
