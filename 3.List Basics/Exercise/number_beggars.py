number_list = input().split(',')
count_of_beggars= int(input())
new_list = []
final_list = []
counter_of_index = 0
for i in number_list:
    new_list.append(int(i))
while counter_of_index < count_of_beggars:
    sum_for_beggar = 0
    for money_index in range (counter_of_index, len(new_list), count_of_beggars):
        sum_for_beggar += new_list[money_index]
    counter_of_index+= 1
    final_list.append(sum_for_beggar)
print(final_list)

