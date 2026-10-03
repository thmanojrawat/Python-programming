# Inventory management

inventory = {
    "001": {"name": "Laptop", "price": 999.99, "quantity": 15},
    "002": {"name": "Mouse", "price": 19.99, "quantity": 50},
    "003": {"name": "Keyboard", "price": 49.99, "quantity": 25}
}

inventory["004"] = {
    "name": "Monitor",
    "price": 199.99,
    "quantity": 10
}

def update_stock(product_id, quantity_sold):
    if product_id in inventory:
        inventory[product_id]["quantity"] -= quantity_sold
        print(f"Updated stock for {inventory[product_id]['name']}")
    else:
        print("Product not found")

update_stock("001", 3)

print(inventory["001"]["quantity"])

low_stock = {
    product_id: details
    for product_id, details in inventory.items()
    if details["quantity"] < 20
}

print("Low stock items:", low_stock)
