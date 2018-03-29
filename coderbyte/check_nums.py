def CheckNums(num1,num2): 

    # code goes here 

    if int(num1)<int(num2) :
        return 'true'
    if int(num1)==int(num2):
        return '-1'
    if int(num1)>int(num2):
        return 'false'
    
# keep this function call here  
print CheckNums(raw_input())  