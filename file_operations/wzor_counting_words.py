orders = {
    'ee': 72,
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}

sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)
key_list = list(orders.values())
key_list = sorted(key_list)
print(key_list)
min = key_list[0]
print(min)
max = key_list[-1]
print(max)
for element, val in orders.items():
    if val == max:
        print('stowa',element)