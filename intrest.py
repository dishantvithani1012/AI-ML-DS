Principle = float(input("Enter Principal amount  :  "))
Rate= float(input("Enter rate of intrest  :  "))
N=float(input("Enter duration of amount  :  "))

Intrest = (Principle*Rate*N)/100
Ci= Principle*(1+Rate/100)** N-Principle
print("AMOUNT IS ",Principle)
print("RATE IS ",Rate)
print("DURATION IS ",N)
print("Your Simple Intrest is",Intrest)
print("Your Compound intrest is",Ci)