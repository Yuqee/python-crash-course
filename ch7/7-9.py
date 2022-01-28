# 7-9. No Pastrami
sandwich_orders = ['poboy', 'Pastrami', 'muffuletta', 'Pastram', 'clubhouse', 'Pastram', 'reuben', 'grilled', 'Pastram', 'meat']
finished_sandwiches = []

while sandwich_orders:
    curr_sanwich = sandwich_orders.pop()
    finished_sandwiches.append(curr_sanwich)
    print(f"\nI made your {curr_sanwich} sandwich.")

print("I have made these sandwiches today:")
for sandwich in finished_sandwiches:
    print(sandwich)