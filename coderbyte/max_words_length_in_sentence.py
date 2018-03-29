def LongestWord(sen): 

    # code goes here 
    
    words = sen.split(' ')

    lengths = []
    
    for i in range(len(words)):
        lengths.append(len(words[i]))
    
    max_lengths = max(lengths)
    
    index_of_max_lengths = lengths.index(max_lengths)

    longuest_word = words[index_of_max_lengths]
    
    return longuest_word
    
# keep this function call here  
print LongestWord(raw_input())
















  