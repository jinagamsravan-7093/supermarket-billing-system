import sqlite3
from datetime import datetime

def get_product_price(name):
    conn = sqlite3.connect("supermarket.db")
    cursor = conn.cursor()

    cursor.execute("SELECT price FROM products WHERE name=?", (name,))
    result = cursor.fetchone()

    conn.close()
    return result[0] if result else None


def generate_bill():
    print("\n===== Supermarket Billing System =====")

    items = []
    subtotal = 0

    while True:
        name = input("\nEnter product name (or 'done'): ")

        if name.lower() == 'done':
            break

        price = get_product_price(name)

        if price is None:
            print("Product not found in database!")
            continue

        quantity = int(input("Enter quantity: "))
        total = price * quantity

        subtotal += total

        items.append((name, quantity, price, total))

    # Calculations
    gst = subtotal * 0.05   # 5% GST
    discount = subtotal * 0.10 if subtotal > 500 else 0
    grand_total = subtotal + gst - discount

    # Date & Time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print Bill
    print("\n\n========= SUPERMARKET BILL =========")
    print("Date:", now)
    print("------------------------------------")
    print("{:<15}{:<10}{:<10}{:<10}".format("Item", "Qty", "Price", "Total"))

    for item in items:
        print("{:<15}{:<10}{:<10}{:<10}".format(*item))

    print("------------------------------------")
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"GST (5%): ₹{gst:.2f}")
    print(f"Discount: ₹{discount:.2f}")
    print(f"Grand Total: ₹{grand_total:.2f}")
    print("====================================")

    # Save to file
    with open("bill.txt", "w", encoding="utf-8") as f:
        f.write("===== SUPERMARKET BILL =====\n")
        f.write(f"Date: {now}\n\n")

        for item in items:
            f.write(f"{item[0]} x{item[1]} = ₹{item[3]}\n")

        f.write(f"\nSubtotal: ₹{subtotal}\n")
        f.write(f"GST: ₹{gst}\n")
        f.write(f"Discount: ₹{discount}\n")
        f.write(f"Grand Total: ₹{grand_total}\n")
    print("\nBill saved as 'bill.txt'")
    print("\nThanks for visiting!")
# Run system
generate_bill()