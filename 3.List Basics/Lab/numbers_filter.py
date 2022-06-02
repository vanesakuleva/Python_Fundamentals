n= int(input())

positive = []
negative= []
odd = []
even = []

for i in range(n) :
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)
    if number %2 == 0:
        even.append(number)
    else:
        odd.append(number)

command = input()
if command == "positive" :
    print(positive)
elif command == "negative" :
    print(negative)
elif command == "odd":
    print(odd)
elif command == "even":
    print (even)