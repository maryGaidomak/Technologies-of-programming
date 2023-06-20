def calculate_inversions_count(array):
    count = 0
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                count += 1
    return count


def test_calculate_inversions_count():
    print(calculate_inversions_count([3,2,1]) == 3)
    print(calculate_inversions_count([5, 4, 1, 2, 1]) == 8)
    print(calculate_inversions_count([1,2,3,4,4,4,4]) == 0)


test_calculate_inversions_count()


