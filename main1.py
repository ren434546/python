inventory = {
    "Сервер": 10,
    "Комутатор Cisco": 3,
    "Кабель UTP": 50,
    "Патч-панель": 2
}

def update_inventory(product_name, quantity_change):
    if product_name in inventory:
        inventory[product_name] += quantity_change
        if inventory[product_name] <= 0:
            del inventory[product_name]
    else:
        if quantity_change > 0:
            inventory[product_name] = quantity_change

update_inventory("Комутатор Cisco", 2)
update_inventory("Патч-панель", -2)
update_inventory("Роутер", 4)

print(inventory)

low_stock_products = [product for product, qty in inventory.items() if qty < 5]
print(low_stock_products)