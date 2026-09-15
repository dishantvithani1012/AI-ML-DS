# 3. SHOPPING BILL

def calculate_subtotal(prices):
    return sum(prices)


def calculate_discount(subtotal):
    if subtotal >= 5000:
        return subtotal * 20 / 100
    elif subtotal >= 3000:
        return subtotal * 10 / 100
    elif subtotal >= 2000:
        return subtotal * 5 / 100
    else:
        return 0


def calculate_tax(amount):
    return amount * 5 / 100


def calculate_final_amount(subtotal, discount, tax):
    return subtotal - discount + tax


items = []
prices = []

n = int(input("Enter number of items: "))

for i in range(n):
    item = input(f"Enter item {i + 1} name: ")
    price = float(input(f"Enter price of {item}: ₹"))

    items.append(item)
    prices.append(price)

subtotal = calculate_subtotal(prices)
discount = calculate_discount(subtotal)
tax = calculate_tax(subtotal - discount)
final_amount = calculate_final_amount(subtotal, discount, tax)

print("\n----- SHOPPING BILL -----")

for i in range(n):
    print(f"{items[i]}: ₹{prices[i]:.2f}")

print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Tax: ₹{tax:.2f}")
print(f"Final Amount: ₹{final_amount:.2f}")