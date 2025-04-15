item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(total)
discount = int(input("Do you have a discount?: "))
total2 = total - discount
print(total2)
taxes = float(input("The tax is: "))
total3= total2 + taxes
print(total3)
shipping = float(input("The shipping is: "))
total4= total3 + shipping
print(total4)