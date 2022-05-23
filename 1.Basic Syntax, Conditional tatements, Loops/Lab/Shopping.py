budget= int(input())
prices = input()

while prices != 'End':
    product_prices = int(prices)
    budget -= product_prices
    if budget <0 :
        print("You went in overdraft!")
    prices = input()
else:
    print ("You bought everything needed.")
