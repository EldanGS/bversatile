from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    is_prime, primes = [True] * (n + 1), []
    if n < 2:
        return primes
    is_prime[0] = is_prime[1] = False
    i = 2
    while i <= n:
        if is_prime[i]:
            primes.append(i)
            j = i * i
            while j <= n:
                is_prime[j] = False
                j += i
        i += 1

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("5-09-prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
