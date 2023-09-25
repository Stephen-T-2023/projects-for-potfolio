def result(codes, Money):
    if codes == "a1":
        Code = 1.50
    elif codes == "a2":
        Code = 1.25
    elif codes == "a3":
        Code = 1.60
    elif codes == "b1":
        Code = 1.30
    elif codes == "b2":
        Code = 1.50
    elif codes == "b3":
        Code = 1.25
    elif codes == "c1":
        Code = 1.00
    elif codes == "c2":
        Code = 1.10
    elif codes == "c3":
        Code = 1.30
    elif codes == "d1":
        Code = 1.00
    elif codes == "d2":
        Code = 1.25
    elif codes == "d3":
        Code = 1.40

    if Code>Money:
        funds = False
        return funds
    else:
        change = Money - Code
        return change

item = input("Welcome to the vending machine, choose an item from the following, crisp 1 = a1, crisp 2 = a2, crisp 3 = a3, drink 1 = b1, drink 2 = b2, drink 3 = b3, sweets 1 = c1, sweets 2 = c2, sweets 3 = c3, chocolate 1 = d1, chocolate 2 = d2, chocolate 3 = d3. ")
item = item.lower()

money = float(input("Enter the money. "))

print("Your change is", result(item,money))
print("Your item will be produced shortly")