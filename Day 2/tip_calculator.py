print("Welcome to tip calculator")
bill= float(input("what was your total bill? $\n"))
percentage_tip= int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
tip= percentage_tip/100
tip_bill= bill*tip
total_bill=bill + tip_bill
num_of_people=int(input("How many people to split the bill\n"))
personal_bill= total_bill/num_of_people
bill_per_person= "{:.2f}".format(personal_bill)
print(f'Each person should pay ${bill_per_person}')