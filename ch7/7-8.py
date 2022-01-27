# 7-8. Deli
sandwich_orders = ['poboy', 'muffuletta', 'clubhouse', 'reuben', 'grilled', 'meat']
finished_sandwiches = []

while sandwich_orders:
    curr_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(curr_sandwich)
    print(f"\nI made your {curr_sandwich} sandwich.")

print("I have made these sandwiches today:")
for sandwich in finished_sandwiches:
    print(sandwich)