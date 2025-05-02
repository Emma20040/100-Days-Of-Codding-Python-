from data import MENU, resources


water= 300
milk=200
coffee=100

def calculate_price():
    print("Please insert coin")
    quarters = int(input("quaters "))
    dimes = int(input("dimes "))
    nickles = int(input("nickles "))
    pennies= int(input('pennies '))
    total_price= (quarters*0.25 + dimes*0.10) +(nickles*0.05 + pennies*0.01)
    return total_price


def choice():
    user_choice= input("what would like espresso/latte/cappuccino ").lower()
    if user_choice== "report":
        print(resources)
    elif user_choice== 'espresso':
        total = calculate_price()
        if total >= 1.5:
           total_change= total - 1.5
           print(f"your change is {total_change}")
        else:
            print("insufficent fund, add more balance")
    elif user_choice == 'latte':
         total = calculate_price()
         if total >= 2.5:
           total_change= total - 2.5
           print(f"your change is {total_change}")
         else:
            print("insufficent fund, add more balance")
        # calculate_price()
    elif user_choice == 'cappuccino':
         total = calculate_price()
         if total >= 3.0:
           total_change= total - 3.0
           print(f"your change is {total_change}")
         else:
            print("insufficent fund, add more balance")
    else:
        print("we don't have that coffe here!")

choice()


def order():
    pass