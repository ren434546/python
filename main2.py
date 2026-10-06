sales_data = [
    {"продукт": "Raspberry Pi", "кількість": 2, "ціна": 1500},
    {"продукт": "Arduino Uno", "кількість": 5, "ціна": 400},
    {"продукт": "Raspberry Pi", "кількість": 1, "ціна": 1500},
    {"продукт": "Датчик руху", "кількість": 10, "ціна": 80},
]


def calculate_total_revenue(sales):
    revenue_dict = {}
    for sale in sales:
        product = sale["продукт"]
        total_price = sale["кількість"] * sale["ціна"]
        revenue_dict[product] = revenue_dict.get(product, 0) + total_price

    return revenue_dict


total_revenues = calculate_total_revenue(sales_data)
print(total_revenues)

profitable_products = [product for product, revenue in total_revenues.items() if revenue > 1000]
print(profitable_products)