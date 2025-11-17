def mod_number(a, b):
    if b == 0:
        raise ValueError("Нельзя делить на ноль")
    if a >= 0:
        if a < abs(b):
            return a
        return mod_number(a - abs(b), abs(b))
    else:
        return mod_number(a + abs(b), abs(b))


if __name__ == "__main__":
    print(mod_number(int(input()), int(input())))
