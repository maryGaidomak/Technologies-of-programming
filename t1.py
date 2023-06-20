def longest_same_sign_sequence(arr):
    max_len = 1
    current_len = 1

    for i in range(1, len(arr)):
        if arr[i] * arr[i - 1] > 0:  # знаки совпадают
            current_len += 1
        else:
            max_len = max(max_len, current_len) # ищем максимальную длину
            current_len = 1

    return max(max_len, current_len)


def test_longest_same_sign_sequence():
    print(longest_same_sign_sequence([1, 2, 3, 4, 5, -1, 2, -4, -5]) == 5)
    print(longest_same_sign_sequence([1, -2, -3,- 4, -5, -1, -2, 4, -5]) == 6)
    print(longest_same_sign_sequence([1, -2, 3, -4, -5, 1, 2, -4, -6, -5, -9]) == 4)

test_longest_same_sign_sequence()


