import os
import logging
from dotenv import load_dotenv
load_dotenv()
import requests
from controller import ACController


logger = logging.getLogger("my_location")

HA_TOKEN = os.getenv("HA_TOKEN")
HA_URL = os.getenv("HA_URL")

headers = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json"
}

ac_controller = ACController()


def get_current_weather_temp():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=35.71&lon=139.70&appid={os.getenv('OPENWEATHER_API_KEY')}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data['main']['temp']


def handle_location_call(switch: bool):
    if switch == 'true':
        logger.info("Turning on AC")
        action = ac_controller.turn_on()
    else:
        logger.info("Turning off AC")
        action = ac_controller.turn_off()
    response = requests.post(f"{HA_URL}/api/services/{action['domain']}/{action['service']}", headers=headers, json=action['service_data'])
    logger.debug(f"Response: {response.status_code} {response.text}")    