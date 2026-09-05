print("==Welcome to my Expense Tracker==")
balance=0
while True:
    method=input("Please Choose Your method Expense/Income or Exit: ")
    if method =="Exit":
        break
    if method=="Expense":
        taka=int(input("Enter your amount: "))
        balance = balance - taka
        print(f"Your current balance is: {balance}","taka")
    elif method=="Income":
        taka=int(input("Enter your amount: "))
        balance = balance + taka
        print(f"Your current balance is: {balance}","taka")
    else:
        print("You typed wrong")

print("==Thank You==")