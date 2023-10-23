# Четем количеството на наличната храна и поръчките.
food_quantity = int(input())
orders = list(map(int, input().split()))

# Намираме най-голямата поръчка.
max_order = max(orders)

# Общ брой поръчки.
total_orders = len(orders)

while orders:
    current_order = orders[0]
    if current_order <= food_quantity:
        food_quantity -= current_order
        orders.pop(0)
    else:
        break

if not orders:
    print(max_order)
    print("Orders complete")
else:
    remaining_orders = ", ".join(map(str, orders))
    print(max_order)
    print(f"Оставащи поръчки: {remaining_orders}")
