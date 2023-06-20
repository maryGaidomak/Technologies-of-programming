def find_element_in_all_arrays(array1: [], array2: [], array3: []):
    n1 = len(array1)
    n2 = len(array2)
    n3 = len(array3)
    i = j = k = 0

    while i < n1 and j < n2 and k < n3:

        if array1[i] == array2[j] == array3[k]:
            return array1[i]
        elif array1[i] <= array2[j] and array1[i] <= array3[k]:
            i += 1
        elif array2[j] <= array1[i] and array2[j] <= array3[k]:
            j += 1
        elif array3[k] <= array1[i] and array3[k] <= array2[j]:
            k += 1

    return None


def test_find_element_in_all_arrays():
    print(find_element_in_all_arrays([1, 2, 3], [2, 3, 4], [2, 5, 6]) == 2)
    print(find_element_in_all_arrays([1, 2, 3, 5, 6], [3, 6, 7, 8], [6, 7, 8]) == 6)
    print(find_element_in_all_arrays([9, 10, 12], [1, 2, 3], [8, 9, 10]) == None)


test_find_element_in_all_arrays()