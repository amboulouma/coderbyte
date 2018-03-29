# Sorting an array - We take the array's elements and put them 
# in another array in order

ARRAY = [2, 3, 4, 5, 1, 2, 7, 8, 10, 27, 8, 11]

print(ARRAY)

def sort_array_1(array):
    sorted_array = []
    for i in range(len(array)):
        for j in array:
            if (j == min(array)):
                sorted_array.append(j)
                array.remove(j)
    return sorted_array

print(sort_array_1(ARRAY))

# Sorting an array without creating another array - We flip array's 
# elements 2 by 2 till the end of the arrays

ARRAY = [2, 3, 4, 5, 1, 2, 7, 8, 10, 27, 8, 11]

def sort_array_2(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                _temp = array[j]
                array[j] = array[j+1]
                array[j+1] = _temp
    return array

print(sort_array_2(ARRAY))

# Third way of sorting - We put do it through minimums 
# and maximums of the table 

ARRAY = [2, 3, 4, 5, 1, 2, 7, 8, 10, 27, 8, 11]

# def sort_array_3(array):
#     for i in range(int(len(array))):
#         for j in range(i, len(array)-i):
#             if array[i:len(array)-i-1] != []:
#                 if array[j] == max(array[i:len(array)-i-1]):
#                     _temp = array[j]
#                     array[j] = array[len(array)-i -1]
#                     array[len(array)-i -1] = _temp
#                 if array[j] == min(array[i:len(array)-i]):
#                     _temp = array[j]
#                     array[j] = array[i]
#                     array[i] = _temp
#     return array

# print(sort_array_3(ARRAY))