def simmetr(s, i, j) -> None:
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return simmetr(s, i + 1, j - 1)


if __name__ == "__main__":
    st = input()
    print(simmetr(st, 0, len(st)-1))
