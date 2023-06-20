def find_max_value(array):
    if len(array) == 1:
        return array[0]
    else:
        # Вызываем для хвоста части массива
        max_rest = find_max_value(array[1:])
        return array[0] if array[0] > max_rest else max_rest


def test_find_max_value():
    print(find_max_value([1, 2, 3, 4, 5]) == 5)
    print(find_max_value([10, 2, 3, 4, 5]) == 10)
    print(find_max_value([-5, 2, 3, 8, 5, 5, 8, 1]) == 8)


test_find_max_value()



