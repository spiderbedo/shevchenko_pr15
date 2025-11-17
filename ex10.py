def maxlist(a) -> int:
    if len(a) == 1:
        return a[0]
    if a[0] > maxlist(a[1:]):
        return a[0]
    else:
        maxlist(a[1:])


if __name__ == "__main__":
    print(maxlist([8377, 7, 245, 9999999, 202022, 936253, 54539287, 0, 11]))
