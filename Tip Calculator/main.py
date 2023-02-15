print("Welcome to the tip calculator!")
bill = float(input("What was the total bill $ "))
tip = int(input("How much tip would you like to give 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))
tip_percent = tip/100
total_tip_percent = bill * tip_percent
total_bill = (bill + total_tip_percent)/split
print(f"Each person should pay ${round(total_bill, 2)}")