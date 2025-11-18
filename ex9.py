def combin(n, k) -> int:
    if n == k or k == 0:
        return 1
    return combin(n - 1, k - 1) + combin(n - 1, k)


if __name__ == "__main__":
    print(combin(int(input()), int(input())))
