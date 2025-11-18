def ten_to_bin(x) -> str:
    if x == 0:
        return ""
    return ten_to_bin(x // 2) + str(x % 2)


if __name__ == "__main__":
    print(ten_to_bin(int(input())))
