def reverse_integer(num):
    reverse = 0
    negative = False

    if num < 0:
         negative = True
         num = -num  # Для алгоритма будем использовать положительное число
    while num > 0:
        remainder = num % 10
        reverse = reverse * 10 + remainder
        num = num // 10
    if negative:
        reverse = -reverse  # в конце вернем знак
    return reverse


def test_reverse_integer():
    print(reverse_integer(123) == 321)
    print(reverse_integer(5664) == 4665)
    print(reverse_integer(87918) == 81978)


test_reverse_integer()



