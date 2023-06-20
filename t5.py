def has_duplicate_digits(n, p):
    if p > 9:
        print("P не должно быть больше 9.")
        return False

    digits = []

    # Переводим n в p-ичную систему исчисления
    while n > 0:
        digit = n % p
        if digit in digits:
            return True
        digits.append(digit)
        n //= p

    return False


def test_has_duplicate_digits():
    print(has_duplicate_digits(121, 2) == True)
    print(has_duplicate_digits(235, 6) == True)
    print(has_duplicate_digits(231, 6) == False)


test_has_duplicate_digits()


