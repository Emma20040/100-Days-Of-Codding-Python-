import random
# payer=['aa', 'sasas', 'saasas', 'tyty']
# payer= random.randrange(0, 3)
# print(payer) 

names= input("enter everyone name sepearted by a comma ',' ")
name= names.split(",")

lenth= len(name)
random_pick= random.randint(0, lenth-1)
payer= names[random_pick]
print(f"{payer} will pay the bill today")