import requests
import json

resp = requests.post('http://127.0.0.1:5000/add-person', json={"first_name": "Ok", "last_name": "Sat", "birth_date": "03.05.1995"})

r = json.loads(resp.text)

resp = requests.patch('http://127.0.0.1:5000/edit-person', json={"first_name": "Ok1", "last_name": "Sat1", "birth_date": "03.05.1995", "id": r['id']})

print(resp.text)