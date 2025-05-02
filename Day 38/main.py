from datetime import datetime
import requests

GENDER = "male"
WEIGHT_KG = float(64.2)

HEIGHT_CM = float(174)
AGE = int(210)

APP_ID=  "c96f14a6"
API_KEY = "a5c604b708fdcde13458bc38c9f92881"

exercise_text = input("Tell the exercise you did today")
API_ENDPIONT ='https://trackapi.nutritionix.com/v2/natural/nutrients',
headers= {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID ,
    'x-app-key':API_KEY,
  }

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

response= requests.get(url=API_ENDPIONT, headers=headers)
print(response.text)
