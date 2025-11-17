def search(a, x) -> int:
    if not a:
        return 0
    if a[0] == x:
        return 1
    return search(a[1:], x)


if __name__ == "__main__":
    print(search([8377, 7, 245, 9999999, 202022, 936253, 54539287, 0, 11], 245))
    print(search([8377, 7, 245, 9999999, 202022, 936253, 54539287, 0, 11], -117722883399))
