mass = float(input('Enter your mass in kg\n'))
height= float(input('Input your height in meter\n'))
height_square= height*height
bmi= mass/height_square
print(int(bmi))

# conditions
if bmi <=18.5:
    print("You are Underweight")

elif bmi>18.5 and bmi<=25:
    print("You have a normal bmi ")
elif bmi>25 and bmi<=30:
    print("You are overweight")
elif bmi>30 and bmi<=35:
    print("you are obessed")
else:
    print("you are clincally obessed")
