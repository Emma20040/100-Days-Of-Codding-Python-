# try:
#     file = open("./Day 30/a_file.txt")
# except:
#     file = open("./Day 30/a_file.txt", "w")

height = float(input("Enter height in meter "))
weight = int(input("enter you r weight "))

if height >3:
    raise ValueError("human height can't be over three meters")
bmi = weight/ height**2
print(bmi)