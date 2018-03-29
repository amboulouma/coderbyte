def FirstReverse(num): 

    # code goes here 
    if (int(num) == 0):
        return 1
    else:
        f = 1
        for i in range(1,int(num)+1):
            f = f*i
    return f
    
# keep this function call here  
print FirstFactorial(raw_input())





