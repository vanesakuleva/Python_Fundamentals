budget = float(input())
price_fluor = float(input())

count_eggs = 0
loaves= 0



price_egg= price_fluor * 0.75
price_milk =  price_fluor + (price_fluor * 0.25)
needed_milk_price = price_milk / 4

price_for_loaves = price_egg + price_fluor + needed_milk_price

while budget >= price_for_loaves :
    loaves+=1
    budget -= price_for_loaves
    count_eggs+= 3
    if loaves % 3== 0 :
        count_eggs = count_eggs - (loaves - 2)

print(f'You made {loaves} loaves of Easter bread! Now you have {count_eggs} eggs and {budget:.2f}BGN left.')