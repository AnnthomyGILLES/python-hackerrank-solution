from collections import Counter, defaultdict

number_of_shoes = int(input())
shoes = Counter(input().split())
number_of_customer = int(input())
customers_purchase = defaultdict(list)
total = 0
for i in range(number_of_customer):
    size, price = input().split()
    if size in shoes and shoes[size] > 0:
        total += int(price)
        shoes.subtract([size])
        
print(total)