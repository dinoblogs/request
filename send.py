import requests
import time

while True:
    time.sleep(5)
    x = requests.get('https://townend.onrender.com')
    m = x.text
    print(f'Status Code - {x.status_code}')
