number = int(input())
total_price = 0
for i in range(number) :
    price_per_capsule = float(input())
    days = int(input())
    needed_capsule = int(input())
    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= needed_capsule <= 2000:
        final_price = price_per_capsule * needed_capsule* days

        print (f"The price for the coffee is: ${final_price:.2f}")
        total_price += final_price
print(f"Total: ${total_price:.2f}")


