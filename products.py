products = []
while True:
    name = input('Please key in your product name :')
    if name == 'q':
        break
    price = input('Please key in your product price :')
    products.append([name, price])
print(products)

for p in products:
    print(p)