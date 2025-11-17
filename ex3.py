def progress(a1, r, n):
    if n == 1:
        return a1
    return progress(a1, r, n - 1) + r


if __name__ == "__main__":
    print(progress(int(input()), int(input()), int(input())))
