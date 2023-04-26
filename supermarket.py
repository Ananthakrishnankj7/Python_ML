n = int(input("Enter the number of items "))
items = {}
product = ()
for i in range(n):
    product = input("Enter product ")
    name, price = product.rsplit()
    items[name] = float(price)
    print("hello")
#print(items)
print(product)

input_list = items
print("hello you")

printed_items = set()

for item in input_list:
    if item not in printed_items:
        printed_items.add(item)
        net_price = items[item] * input_list.count(item)
        print(item, net_price)
