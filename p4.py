# ACTIVITY-4: Shopping Discount Calculator

amount = float(input("Enter purchase amount: ₹"))

if amount >= 2000:
    discount = amount * 10 / 100
    final_amount = amount - discount
else:
    discount = 0
    final_amount = amount

print(f"Purchase Amount: ₹{amount:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final Amount: ₹{final_amount:.2f}")