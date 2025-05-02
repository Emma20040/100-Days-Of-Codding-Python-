def add(*args):
    sum =0
    for n in args:
        sum+= n
    return sum

print(add(4, 3, 5,65,44,2))

def calculate(**kwargs):
    print(type(kwargs))
    for (key, value) in kwargs.items():
        print(key)
        print(value)

calculate(add= 4, divide=3)

class Car:
    
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get('model')
        self.colour = kw.get("color")
        self.seats = kw.get('seats')

my_car = Car(make= "Nissan", model= "suv")
print(my_car.model)