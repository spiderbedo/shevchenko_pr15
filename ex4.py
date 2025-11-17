def sum_progress(a1, r, n) -> int:
    if n == 1:
        return a1
    return sum_progress(a1, r, n - 1) + (a1 + (n-1) * r)


if __name__ == "__main__":
    print(sum_progress(int(input()), int(input()), int(input())))
