def pownum(a, n):
    if n == 1:
        return a
    return a * pownum(a, n - 1)


if __name__ == "__main__":
    print(pownum(int(input()), int(input())))
