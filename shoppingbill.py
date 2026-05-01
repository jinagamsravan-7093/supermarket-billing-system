from datetime import datetime

name = input("Enter your Name: ")

# Items with prices
items = {
    1: ("Rice", 50),
    2: ("Sugar", 10),
    3: ("Oil", 85),
    4: ("Salt", 20),
    5: ("paneer", 150),
    6: ("Maggie", 15),
    7: ("Boost", 200),
    8: ("Dairy Milk", 100),
    9: ("Thumsup", 20),
    10: ("Sprite", 20)
}

totalprice = 0
cart = []

# Display menu
print("\nAvailable Items:")
for key, value in items.items():
    print(f"{key}. {value[0]} - Rs {value[1]}")

# Purchase loop
while True:
    choice = input("\nEnter item number (or 0 to exit): ")
    
    if not choice.isdigit():
        print("Invalid input!")
        continue
    
    choice = int(choice)
    
    if choice == 0:
        break
    
    if choice not in items:
        print("Invalid item number!")
        continue
    
    item_name, price_per_unit = items[choice]
    
    qty = input("Enter quantity: ")
    if not qty.isdigit():
        print("Invalid quantity!")
        continue
    
    qty = int(qty)
    price = qty * price_per_unit
    
    totalprice += price
    cart.append((item_name, qty, price))
    
    print(f"{item_name} added to cart!")

# Billing
tax = totalprice * 0.12
finalprice = totalprice + tax

# Print Bill
print("\n" + "="*25 + " Ganesh SuperMarket " + "="*25)
print("Name:", name)
print("Date:", datetime.now())
print("-"*70)

print("S.No   Item       Qty     Price")
for i, item in enumerate(cart, start=1):
    print(f"{i:<6}{item[0]:<10}{item[1]:<8}{item[2]}")

print("-"*70)
print(f"{'Total:':>50} Rs {totalprice}")
print(f"{'Tax (12%):':>50} Rs {tax}")
print(f"{'Final Amount:':>50} Rs {finalprice}")
print("-"*70)
print("====================================")
print(" ---Thanks for visiting our supermarket!---")
print("---- Visit Again!---")