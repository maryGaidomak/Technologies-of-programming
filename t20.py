def find_three_min(array):
    if array == [] or len(array) < 3:
        return None

    # Возьмем за минимум первый элемент массива
    min1 = array[0]
    min2 = array[0]
    min3 = array[0]

    # Обход всех элементов массива
    for num in array:
        if num < min1:
            min3 = min2
            min2 = min1
            min1 = num
        elif num < min2 or min1 == min2:
            min3 = min2
            min2 = num
        elif num < min3 or min3 == min2 or min3 == min1:
            min3 = num

    return min1, min2, min3


def test_find_three_min():
    print(find_three_min([5, 2, 8, 1, 9, 3, -2, 6, 4, 7]) == (-2, 1, 2))
    print(find_three_min([1, 2, 3, 4, 5, 6]) == (1, 2, 3))
    print(find_three_min([6, 5, 4, -3, 3, 2, 1]) == (-3, 1, 2))


test_find_three_min()