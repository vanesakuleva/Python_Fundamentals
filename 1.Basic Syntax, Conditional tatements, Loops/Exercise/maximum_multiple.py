divisor = int(input())
boundary = int(input())
n= 0
for i in range (boundary,-1, -1) :
    if i % divisor == 0 :
        n = i
        break
print(n)
