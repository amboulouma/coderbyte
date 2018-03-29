def LongestWord(sen):
    ALPHABET_WITH_SPACE = [' ', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
    sentence = list(sen)
    letters = []
    for i in sentence:
        if i in ALPHABET_WITH_SPACE:
            letters.append(i)
    s = ''.join(letters)
    words = s.split(' ')
    lengths = []
    for i in range(len(words)):
        lengths.append(len(words[i]))
    max_lengths = max(lengths)
    index_of_max_lengths = lengths.index(max_lengths)
    longuest_word = words[index_of_max_lengths]
    return longuest_word
print LongestWord(raw_input())  


