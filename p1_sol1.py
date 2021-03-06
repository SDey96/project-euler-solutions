"""
Problem 1: Multiples of 3 and 5. (Soltuon 1)

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def result(target):
    result = sum(i for i in range(target) if (i % 3 == 0) or (i % 5 == 0))
    return result


if __name__ == '__main__':
    print(result(1000))
