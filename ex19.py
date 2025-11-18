def count(a, b) -> int:
    if a == 0 or b == 0:
        return 0
    if a < b:
        a, b = b, a
    return a // b + count(b, a % b)


if __name__ == "__main__":
    print(count(int(input()), int(input())))
