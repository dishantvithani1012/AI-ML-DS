# 1. EMPLOYEE PAYROLL

def calculate_gross_salary(basic, allowance):
    return basic + allowance


def calculate_deduction(gross, deduction_rate):
    return gross * deduction_rate / 100


def calculate_net_salary(gross, deduction):
    return gross - deduction


name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
deduction_rate = float(input("Enter deduction percentage: "))

gross = calculate_gross_salary(basic, allowance)
deduction = calculate_deduction(gross, deduction_rate)
net_salary = calculate_net_salary(gross, deduction)

print("\n----- EMPLOYEE PAYROLL -----")
print("Employee Name:", name)
print(f"Basic Salary: ₹{basic:.2f}")
print(f"Allowance: ₹{allowance:.2f}")
print(f"Gross Salary: ₹{gross:.2f}")
print(f"Deduction: ₹{deduction:.2f}")
print(f"Net Salary: ₹{net_salary:.2f}")