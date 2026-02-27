import requests
from config import PRINTER_IP

def get_printer_status():
    try:
        response = requests.get(f"http://{PRINTER_IP}/status")
        return response.json()
    except:
        return {"status": "offline"}