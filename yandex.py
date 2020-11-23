f = open('prices.txt', "r")
data = f.readlines()
f.close()
price = 0
for i in data:
    check = i.split()
    amount = check[1]
    cost = check[2]
    price += int(amount) * float(cost)
print(price)