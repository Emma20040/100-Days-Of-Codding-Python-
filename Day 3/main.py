print("Welcome to rollercoster")
height= int(input("what is our height in cm? "))
bill= 0
# condition
if height>= 120:
    picture=input("do you want to take a picture? Y or N")
    if picture=="Y":
        # bill+=3
    # print("you can proceed")
        age= int(input("enter your age"))
        if age<12:
            bill=8
            print(f"you will pay ${bill}")
        elif age>=18:
            bill=23
            print("you will pay ${bill}")
        else:
            bill=13
            print(f"you will pay ${bill}")
    else:
        pass
else:
    print("you are to short for the ride ")