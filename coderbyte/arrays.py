array = []

# Append method

values = [11, '22', -3.9]

print('\n__append(self, v, /)__\nAppend new value v to the end of the array.\n')

array.append(1)
array.append('1')
array.append(-3.0)
array.append('1')
array.append(values)

print(array)

print('\n__count(self, v, /)__\nReturn number of occurrences of v in the array.\n')

print(array.count('1'))

print('\n__extend(self, v, /)__\nAppend items to the end of the array.\n')
print(array.extend(values))
print(array)

print('\n__index(self, v, /)__\nReturn index of first occurrence of v in the array\n.')
print(array.index('1'))

print('\n__remove(self, v, /)__\nRemove the first occurrence of v in the array.\n')
print(array.remove('1'))
print(array)

print('\n__del__\n')
del array[2]
print(array)

print('\n__pop(self, i=-1, /)__\nDeletes an element from array.Return the i-th element and delete it from the array.\n')
print(array.pop(2))
print(array)

print('\n__reverse(self, /)__\nReverse the order of the items in the array.\n')
print(array.reverse())
print(array)
