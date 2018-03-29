def TimeConvert(num): 
    heures = 0
    while num >= 60:
        num -= 60
        heures += 1
    return str(heures)+":"+str(num)
print TimeConvert(int(raw_input()))  

