P = float(input("Enter Principal amount  :  "))
R= float(input("Enter rate of intrest  :  "))
N=float(input("Enter duration of amount  :  "))

Simple_Intrest = (P*R*N)/100
Ci= P*(1+R/100)** N-P
print("AMOUNT IS ",P)
print("RATE IS ",R)
print("DURATION IS ",N)
print("Your Simple Intrest is",Simple_Intrest)
print("Your Compound intrest is",Ci)