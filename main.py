import math

m = int(input())
n = int(input())
arr = []

  
for i in range(m, n+1) :
    count = 2
    while  True:
        if i % count == 0 :
            break
        if count == math.trunc(i**(1/2)) :
            if i % count != 0 :
                arr.append(i)
                break
            else : break
        count += 1
        
if sum(arr) == 0 :
    print('-1')
else :
    print(sum(arr))
    print(arr[0])          
