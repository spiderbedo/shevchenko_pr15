def nod(a, b) -> int:
    if b == 0:
        return a
    return nod(b, a % b)


if __name__ == "__main__":
    print(nod(int(input()), int(input())))
