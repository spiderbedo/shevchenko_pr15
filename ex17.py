import math

def is_prime(x, d) -> int:
    if d > math.sqrt(x):
        return 1
    if x % d == 0:
        return 0
    return is_prime(x, d + 1)


def function1(x) ->int:
    if x < 2:
        return 0
    return is_prime(x, 2)


if __name__ == "__main__":
    print(function1(int(input())))
