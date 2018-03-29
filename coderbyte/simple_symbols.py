def SimpleSymbols(str): 
    # code goes here 
    q = list(str)
    ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
    result = 'true'
    if q[0] in ALPHABET:
        return 'false'
    if q[len(q)-1] in ALPHABET:
        return 'false'
    for i in range(1, len(q)-1):
        if q[i] in ALPHABET:
            if q[i-1] != '+' and q[i+1] != '+':
                return 'false'
            if q[i-1] == '=' or q[i+1] == '=':
                return 'false'
    return 'true'
# keep this function call here  
print SimpleSymbols(raw_input())