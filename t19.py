def generate_subsets(arr):
    subsets = []
    backtrack([], 0, arr, subsets)
    return subsets


def backtrack(current, start, arr, subsets):
    # Не добавляем пустой список
    if current:
        subsets.append(list(current))

    for i in range(start, len(arr)):
        current.append(arr[i])
        backtrack(current, i + 1, arr, subsets)
        current.pop()


def test_generate_subsets():
    print(generate_subsets([1, 2, 3]) == [[1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])
    print(generate_subsets([3, 4]) == [[3], [3, 4], [4]])
    print(generate_subsets([1]) == [[1]])


test_generate_subsets()