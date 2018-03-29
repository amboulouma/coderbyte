def AlphabetSoup(str): 
    array = list(str)
    sorted_array = []

    for i in range(len(array)):
        for j in array:
            if (j == min(array)):
                sorted_array.append(j)
                array.remove(j)
    l = ''
    return l.join(sorted_array)
print AlphabetSoup(raw_input())  