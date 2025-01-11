import smtplib

my_email = "emmanuelfongong10@gmail.com"
password= "tvxctuenoostquel"

with smtplib.SMTP("smtp.gmail.com") as connection:
# encrypt email
  connection.starttls()

  connection.login(user=my_email, password=password )
  connection.sendmail(from_addr=my_email,
                      to_addrs="robertjones237@yahoo.com",
                        msg="subject:hello Jones\n\n hope you are doing great")
# connection.close()
