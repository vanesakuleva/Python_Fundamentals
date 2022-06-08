number_list = input().split()
numbers_to_remove= int(input())
new_num_list = []
the_smallest_num =0

for num in number_list :
    num = int(num)
    new_num_list.append(num)

for remove in range(numbers_to_remove) :
    new_num_list.remove(min(new_num_list))
print(', '.join(str(i)for i in new_num_list))




