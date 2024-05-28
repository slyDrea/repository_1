import random

print("Your credit is 800000 ")
house_price = random.randint(0, 1000000)
print(f'House price is {house_price}')

if house_price >= 800000:
    buyer_credit_is_good = False
    down_payment = house_price - 800000
    print("House price is above 800000")

else:
    buyer_credit_is_good = True
    down_payment = 0 * house_price
    print("House price is below 800000")

print(f"You should reduce the price by ${down_payment} ")
print(f"Final price {house_price - down_payment}")
