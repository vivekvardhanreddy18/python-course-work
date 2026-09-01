data = {'sugar': 50, 'flour': 40, 'eggs': 75, 'milk': 70, 'butter': 60, 'chocolate': 90, 'vanilla': 80, 'baking powder': 30, 'salt': 20, 'yeast': 25,
'rice': 35, 'pasta': 45, 'tomato sauce': 55, 'cheese': 65, 'onion': 15, 'garlic': 10, 'bell pepper': 25, 'carrot': 20, 'broccoli': 30, 'spinach': 40,
}


while True:
    products =list(map(str.strip, input("Enter the product name: ").split(",")))

    if products == in data:
        print(i.ljust(25), data[i])
    else:
        print(i.ljust(25), "Product not found")
print("Total bill: ".ljust(25), sum(data[i] for i in products if i in data ))

