import os
 
def calculateInput(i:str):
    arr_str = i.split("x")
    
    arr_str[0] = int(arr_str[0])
    arr_str[1] = int(arr_str[1])
    arr_str[2] = int(arr_str[2])
    
    arr_str.sort()

    print(arr_str)

    result = (arr_str[0] * 2) + (arr_str[1]*2) + (arr_str[0] * arr_str[1] * arr_str[2])
    return result


all_result = 0
with open('input.txt') as f:
    for line in f:   
        all_result += calculateInput(line)

print(all_result)



