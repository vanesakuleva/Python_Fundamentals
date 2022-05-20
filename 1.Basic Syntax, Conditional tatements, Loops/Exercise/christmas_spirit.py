quantity = int(input())
days_left_until_chr = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

point_spirit = 0
price = 0

for i in range (1, days_left_until_chr+ 1) :
    if i % 11 == 0:
        quantity += 2

    if i %2 == 0 :
        point_spirit += 5
        price+= ornament_set_price * quantity
    if i % 3 == 0 :
        point_spirit+= 13
        price+= (tree_skirt_price * quantity) + (tree_garland_price * quantity)
    if i % 5 == 0 :
        point_spirit += 17
        price+= tree_lights_price *quantity
    if i % 5 == 0 and i % 3== 0 :
        point_spirit += 30
    if i % 10 == 0 :
        point_spirit-= 20
        price += tree_lights_price + tree_skirt_price + tree_garland_price
        if i == days_left_until_chr :
            point_spirit-= 30

print(f'Total cost: {price}')
print(f"Total spirit: {point_spirit}")

