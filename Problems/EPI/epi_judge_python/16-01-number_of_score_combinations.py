from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    dp = [[1] + [0] * final_score for _ in individual_play_scores]
    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            teammate_score = dp[i - 1][j] if i > 0 else 0
            individual_score = dp[i][j - individual_play_scores[i]] if j - individual_play_scores[i] >= 0 else 0
            dp[i][j] = teammate_score + individual_score

    return dp[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("16-01-number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
