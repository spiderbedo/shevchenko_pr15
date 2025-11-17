def degree5(n) -> int:
    if n == 5:
        return 1
    elif n % 5 != 0 and n % 10 != 0:
        return -1
    return degree5(n // 5) + 1


if __name__ == "__main__":
    print(degree5(int(input())))
