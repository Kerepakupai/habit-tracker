import requests
from datetime import datetime


USERNAME = "kerepakupai"
TOKEN = "F*zNvc3UZazBVUrjj2TFNxPbGhM2!Q"
GRAPH_ID = "graph1"

# Create a new Pixela user
user_params = {
    "token": "F*zNvc3UZazBVUrjj2TFNxPbGhM2!Q",
    "username": "kerepakupai",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url="https://pixe.la/v1/users", json=user_params)


# Create a new pixelation graph definition.
graph_config = {
    "id": GRAPH_ID,
    "name": "Learning English",
    "unit": "Hrs",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs", json=graph_config, headers=headers)

# It records the quantity of the specified date as a "Pixel".
today = datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today?")
}
response = requests.post(
    url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}",
    json=pixel_config,
    headers=headers
)
# print(response.text)

# Update predefined pixelation graph definitions.
pixel_update = {
    "quantity": "9"
}
# response = requests.put(
#    url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20221221",
#    json=pixel_update,
#    headers=headers
# )
# print(response.text)

# Delete the registered "Pixel".
# response = requests.delete(
#    url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}",
#    headers=headers
# )
