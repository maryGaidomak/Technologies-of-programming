def move_negative_to_the_start(array):
    last_index = 0
    for i in range(0, len(array)):
        if array[i] < 0:
            array[last_index], array[i] = array[i], array[last_index]
            last_index += 1


def test_move_negative_to_the_start():
    array = [1, 2, -5, -3, 8, -10, 7, 5]
    move_negative_to_the_start(array)
    print(array == [-5, -3, -10, 2, 8, 1, 7, 5])

    array = [-1, 2, 5, -3, 8, 10, 7, 5]
    move_negative_to_the_start(array)
    print(array == [-1, -3, 5, 2, 8, 10, 7, 5])

    array = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]
    move_negative_to_the_start(array)
    print(array == [-5, -4, -3, -2, -1, 1, 2, 3,4, 5])


test_move_negative_to_the_start()