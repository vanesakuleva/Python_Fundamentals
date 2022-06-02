n = int(input())
list_positive = []
list_negative= []
count_positive = 0
sum_negative = 0

for i in range (n) :
    number = int(input())
    if number >= 0:
        count_positive += 1
        list_positive.append(number)
    else:
        sum_negative += number
        list_negative.append(number)

print(list_positive)
print(list_negative)
print (f'Count of positives: {count_positive}')
print(f'Sum of negatives: {sum_negative}')
