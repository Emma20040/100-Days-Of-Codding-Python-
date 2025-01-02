numbers= [2, 3, 4, 5]
new_list= [n+1 for n in numbers]
print(new_list)

name= "Emma"
new_name = [letter for letter in name]
print(new_name)

dnum= [n*2 for n in range(1,6)]
print(dnum)

name = ["Beth", 'John', "monica", "alexcia", "eleanor"]
long_names= [n.upper() for n in name if len(n)>5]
print(long_names)