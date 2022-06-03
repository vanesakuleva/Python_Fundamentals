n = int(input())
word = input()
list_strings = []
filtered_list = []

for i in range (n) :
    string = input()
    list_strings.append(string)
    if word in string :
        filtered_list. append(string)

print(list_strings)
print(filtered_list)