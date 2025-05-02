def prime_checker(number):
    while number>1:
        for num in range(1, number):
            if number%num==0:
                print("it is not a prime number")
                # break
            else:
                print("it is a prime number")
    
if_num_is_prime= int(input("enter the number you wanna check "))
prime_checker(number=if_num_is_prime)