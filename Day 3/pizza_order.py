print("Welcome to my pizza order calculator!!")
small=15
medium= 20
large= 25
bill=0

size=input("what size of pizzar do you want? ")
if size=="small":
    pepperoni= input("do you want to add pepperoni")
    if pepperoni=="yes":
        pep_bill =small +2

        extra= input("do yo want to add extra? ")
    
        if extra=="yes":
            bill =pep_bill + 1
            print(bill)       
        else:
                bill=pep_bill
                print(bill)
    else:
        bill=small
        print(bill)

elif size=="meduim":
    pepperoni= input("do you want to add pepperoni")
    if pepperoni=="yes":
        pep_bill =medium +3
        extra= input("do yo want to add extra? ")
        if extra=="yes":
            bill =pep_bill + 1
            print(bill)
        else:
            bill=pep_bill
            print(bill)
    else:
        bill=medium
        print(bill)

elif size=="large":
    pepperoni= input("do you want to add pepperoni")
    if pepperoni=="yes":
        pep_bill =large +3
        extra= input("do yo want to add extra? ")
        if extra=="yes":
            bill =pep_bill + 1
            print(bill)
        else:
            bill=pep_bill
            print(bill)
    else:
        bill=large
        print(bill)

else:
    print("invalid input, enter a valid input")
    