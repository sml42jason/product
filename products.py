products = []
while True:
    name = input('Please key in your product name :')
    if name == 'q':
        break
    price = input('Please key in your product price :')
    products.append([name, price])
#print(products)


for p in products:
    print(p)

with open('products.csv', 'w') as f:
    for p in products:
        f.write(p[0] + ', ' + p[1] + '\n')
