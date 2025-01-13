from datetime import datetime
import requests

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "amma"
TOKEN ="83fhrfhiw793kgd0asurhdkf"
GRAHP_ID = "graph1"

user_params ={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":'yes',
    "notMinor":"yes",
} 

graph_config= {
    "id":GRAHP_ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type": "float",
    "color": "sora"
}

headers ={
    "X-USER-TOKEN": TOKEN
}
graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url= pixela_endpoint, json= user_params)
# print(response.text)

# response = requests.post(url=graph_endpoint, json=graph_config, headers= headers)
# print(response.text)

pixel_creation_endpoint= f"{pixela_endpoint}/ {USERNAME}/graphs/{GRAHP_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.1"
}

# requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAHP_ID}/ {today.strftime('%Y%m%d')}"

new_pixel_data ={
    "quantity": "5"
}

# response =requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAHP_ID}/ {today.strftime('%Y%m%d')}"
response= requests.delete(url=delete_endpoint, headers=headers)
print(response.text)