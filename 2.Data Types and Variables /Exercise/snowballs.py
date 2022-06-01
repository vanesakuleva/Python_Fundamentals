number_of_snowballs = int(input())
result = 0
highest_value = 0

for i in range (number_of_snowballs) :
    weight_of_the_snowball= int(input())
    time_needed= int(input())
    quality = int(input())
    result = (weight_of_the_snowball / time_needed) ** quality
    if result > highest_value :
        highest_value = result
        best_snowball_data= f'{weight_of_the_snowball} : {time_needed} = {int(highest_value)} ({quality})'


print(best_snowball_data)