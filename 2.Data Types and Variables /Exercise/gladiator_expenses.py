lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
counter = 0

total_price = 0
for i in range (1, lost_fights_count +1 ):
    if i % 2 ==0 :
        total_price += helmet_price

    if i % 3 == 0 :
        total_price += sword_price
        if i % 2 ==0:
            counter +=1
            total_price += shield_price
            if counter == 2 :
                total_price += armor_price
                counter = 0

print (f"Gladiator expenses: {total_price:.2f} aureus")
