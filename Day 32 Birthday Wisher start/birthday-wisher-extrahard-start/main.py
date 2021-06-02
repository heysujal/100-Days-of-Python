##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import pandas as pd
import datetime as dt
import random

df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
month = now.month
day = now.day

inter_df = df[df.day == day]
final = inter_df[inter_df.month == month]

if not final.empty:
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        letter_body = file.read()
        letter_body = letter_body.replace("[NAME]", final.name.item())
        my_email = "YOUR_EMAIL"
        password = "YOUR_PASSWORD"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=final.email.item(),
                            msg=f"Subject:Testing Email\n\n{letter_body}")
        connection.quit()
