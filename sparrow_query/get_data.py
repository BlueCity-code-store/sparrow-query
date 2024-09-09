import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import requests
import pandas as pd

load_dotenv()

APIKEY = os.getenv('APIKEY')

url = 'https://api.sparrow.city/get'
headers = {'Accept': 'application/json'}

# so2 is not available in the data
filters = ['pm1', 'pm25', 'pm10', 'co2', 'no2', 'o3', 'temperature', 'humidity', 'pressure', 'iri', 'bumps']
start_date = '2023-01-08T12:00:00'
end_date = '2023-01-10T15:00:00'
start_lat = 46.20391241
start_lon = 6.145815253
end_lat = 46.20585782
end_lon = 6.154720187

dfs = []

for filter in filters:
    params = {
        'filter': filter,
        'start_date': start_date,
        'end_date': end_date,
        'start_lat': start_lat,
        'start_lon': start_lon,
        'end_lat': end_lat,
        'end_lon': end_lon,
        'api_key': APIKEY
    }
    r = requests.get(url, headers=headers, params=params)
    data = r.json()
    df = pd.DataFrame(data['body'])
    df['filter'] = filter
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)
combined_df.to_csv('data.csv', index=False)
