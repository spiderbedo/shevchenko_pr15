def fib(k) -> int:
    if k == 1 or k == 2:
        return 1
    return fib(k-1) + fib(k-2)


if __name__ == "__main__":
    print(fib(int(input())))
