def ten_to_n(x, n) -> str:
    digits = "0123456789ABCDEF"
    if x == 0:
        return ""
    return ten_to_n(x // n, n) + digits[x % n]


if __name__ == "__main__":
    print(ten_to_n(int(input()), int(input())))
