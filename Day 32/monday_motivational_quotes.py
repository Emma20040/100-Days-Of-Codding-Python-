import smtplib
import datetime as dt
import random

MY_EMAIL= "emmanuelfonfong10@gmail.com"
PASSWORD = "Emmnkwfon04"

now = dt.datetime.now()
weekday = now.weekday()
if weekday ==2:
    with open("./Day 32/quotes.txt","r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(all_quotes)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                             msg=f"subject: monday motivation \n\n {quote}")
