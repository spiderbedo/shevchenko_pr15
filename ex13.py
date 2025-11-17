def odd_list(a, n) -> list:
    if n == 0:
        return []
    lol = odd_list(a, n-1)
    if a[n-1] % 2 == 0:
        lol.append(a[n-1])
    return lol


if __name__ == "__main__":
    print(odd_list([8377, 7, 245, 9999999, 202022, 936253, 54539287, 11], 8))
