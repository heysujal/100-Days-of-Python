# import smtplib
# import random
#
# with open("quotes.txt") as quotes:
#     quotes_list = quotes.readlines()
#
# my_email = ""
# password = ""
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# random_quote = random.choice(quotes_list)
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email,to_addrs="",
#                     msg=f"Subject:Testing Email\n\n{random_quote}")
# connection.quit()

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(year)
# print(month)
# print(day_of_week)
# print(type(year))
#
# date_of_birth = dt.datetime(year=2000,month=11,day=6)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
    random_quote = random.choice(quotes_list)
    my_email = "YOUREMAIL"
    password = "YOUR PASSWORD"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="RECEIVER EMAIL ADDRESS",
                        msg=f"Subject:Testing Email\n\n{random_quote}")
    connection.quit()
