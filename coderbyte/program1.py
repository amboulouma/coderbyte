# Sorting an array

array = [2, 3, 4, 5, 1, 2, 7, 8, 10, 27, 8, 11]

print(array)

def sortArray1(array):
    sortedArray = []
    for i in range(len(array)):
        for j in array:
            if (j == min(array)):
                sortedArray.append(j)
                array.remove(j)
    return sortedArray

print(sortArray1(array))

# Sorting an array without creating another array

array = [2, 3, 4, 5, 1, 2, 7, 8, 10, 27, 8, 11]

def sortArray2(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                _temp = array[j]
                array[j] = array[j+1]
                array[j+1] = _temp
    return array

print(sortArray2(array))

# Sorting an array with one loop

array = [2, 3, 4, 5, 1, 2, 7, 8, 10, 27, 8, 11]

