def is_palindrome(number, base):
    digits = []
    while number > 0:
        digits.append(number % base)
        number //= base
    # Сравниваем список с самим собой в обратном порядке
    return digits == digits[::-1]


def test_is_palindrome():
    print(is_palindrome(121, 10) == True)
    print(is_palindrome(5665, 10) == True)
    print(is_palindrome(5, 2) == True)


test_is_palindrome()


