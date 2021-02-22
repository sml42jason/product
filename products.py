import os

products = []
if os.path.isfile('products.csv'):
    with open('products.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if 'Products, Price' in line:
                continue
            name, price = line.strip().split(', ')
            products.append([name, price])
    print(products)
else:
    print('NO file exist!!')
    
while True:
    name = input('Please key in your product name :')
    if name == 'q':
        break
    price = input('Please key in your product price :')
    products.append([name, price])
#print(products)

for p in products:
    print(p)

with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('Products, Price\n')
    for p in products:
        f.write(p[0] + ', ' + p[1] + '\n')
