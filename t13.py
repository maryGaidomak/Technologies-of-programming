import math

def recursive_sin(x, eps, n=0):
    term = ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)

    if abs(term) < eps:
        return term

    return term + recursive_sin(x, eps, n + 1)


# Факториал
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def test_recursive_sin():
    x = 0
    epsilon = 1e-6
    result = recursive_sin(x, epsilon)
    expected = 0  # sin(0) = 0
    print(result == expected)

    x = math.pi / 4
    epsilon = 1e-6
    result = recursive_sin(x, epsilon)
    expected = math.sin(x)
    # math.sin не принимает аргумента для установки точности
    # поэтому результат принудительно округлен
    print(round(result, 6) == round(expected, 6))

    x = 1.2
    epsilon = 1e-6
    result = recursive_sin(x, epsilon)
    expected = math.sin(x)  # Сравнение с результатом функции math.sin(x)
    print(round(result, 6) == round(expected, 6))


test_recursive_sin()