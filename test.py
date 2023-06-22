import requests
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import json

concurrency = 1



json_data = {
    'dbt': 'debug',
}



def http():
    response = requests.post('http://10.204.14.29:5000/', json=json_data)
    return response.content


with ThreadPoolExecutor(max_workers=concurrency) as executor:
    results = [executor.submit(http) for _ in range(concurrency)]
    
    for f in as_completed(results):
        print(json.loads(f.result()))


response = requests.post('http://10.204.14.29:5000/', json=json_data)
print(response.content.decode('unicode-escape'))


