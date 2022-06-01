lines = int(input())

tank_capacity = 255
total_sum = 0

for i in range (lines) :
    liters = int(input())
    if liters + total_sum <= tank_capacity:
        total_sum += liters
        continue
    print('Insufficient capacity!')

print (total_sum)


