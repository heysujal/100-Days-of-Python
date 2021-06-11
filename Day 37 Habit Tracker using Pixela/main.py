USERNAME = "heysujal"
TOKEN = "thisisasecret"
GRAPH_ID = "graph1"
headers = {

    "X-USER-TOKEN": TOKEN
}

import requests
from datetime import date,timedelta




# Creating an account
pixela_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token": TOKEN,
#
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url = pixela_endpoint,json= user_params)
#
# print(response.text)

# Creating a graph
# graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
# graph_params = {"id": GRAPH_ID,
#                 "name": "coding-habit-tacker",
#                 "unit": "commit",
#                 "type": "int",
#                 "color": "ajisai",
#
#                 "timezone": "Asia/Kolkata",
#
#                 }
# headers = {
#
#     "X-USER-TOKEN": TOKEN
# }
# res =  requests.post(url=graph_endpoint, json=graph_params, headers=headers)


#Changing the date of commit
custom_date = date.today() + timedelta(days=0)
custom_date = custom_date.strftime("%Y%m%d")


# commit_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# commit_params = {
#     "date": custom_date,
#     "quantity": "1",
# }
# res = requests.post(url=commit_endpoint, json=commit_params, headers=headers)

# Update a commit
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{custom_date}"
update_params = {
"quantity":"1"

}
res = requests.put(url=update_endpoint, json=update_params, headers=headers)

print(res.text)


