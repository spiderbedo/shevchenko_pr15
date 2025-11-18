def numbers(x) -> None:
    if x < 10:
        print(x)
    else:
        print(x % 10)
        numbers(x//10)


if __name__ == "__main__":
    numbers(int(input()))
