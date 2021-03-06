"""
Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

"""
def nth_prime(n):
    counter = 2
    for i in range(3, n**2, 2):
        k = 1
        while k*k < i:
            k += 2
            if i % k == 0:
                break
        else:
            counter += 1
        if counter == n:
            return i


print(nth_prime(10001))
"""


def nth_prime(n):
    x = 2
    list_of_primes = []

    while (len(list_of_primes) < n):
        if all(x % prime for prime in list_of_primes):
            list_of_primes.append(x)
        x += 1

    print(list_of_primes[-1])


nth_prime(6)
