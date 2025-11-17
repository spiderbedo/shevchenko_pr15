def ind_maxlist(a) -> int:
    if len(a) == 1:
        return 0
    idx_tail = ind_maxlist(a[1:])
    idx_tail += 1
    return 0 if a[0] >= a[idx_tail] else idx_tail


if __name__ == "__main__":
    print(ind_maxlist([8377, 7, 245, 9999999, 202022, 936253, 54539287, 0, 11]))
