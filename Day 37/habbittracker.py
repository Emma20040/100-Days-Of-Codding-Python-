import requests

pixela_endpoint = "https://pixe.la/v1/users"

# USERNAME = "amma"
# TOKEN ="83fhrfhiw793kgd0asurhdkf"
user_params ={
    "token":"djsd73kf0erjf904kd8dff",
    "username":"emmanuel",
    "agreeTermsOfService":'yes',
    "notMinor":"yes",
} 

# graph_config= {
#     "id":"graph1",
#     "name":"Cycling Graph",
#     "unit":"Km",
#     "type": "float",
#     "color": "sora"
# }

# headers ={
#     "X-USER-TOKEN": TOKEN
# }
# graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs"
response = requests.post(url= pixela_endpoint, json= user_params)
print(response.text)

# response = requests.post(url=graph_endpoint, json=graph_config, headers= headers)
# print(response.text)