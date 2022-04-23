import pandas as pd
import json
import requests


r = requests.get("https://api.dclimate.net/apiv3/grid-history/prismc-tmax-daily/30_-97?also_return_metadata=false&use_imperial_units=false&also_return_snapped_coordinates=true&convert_to_local_time=true")
data = r.json()["data"]




index = pd.to_datetime(list(data.keys()))
values = [float(s.split()[0]) if s else None for s in data.values() ]
series = pd.Series(values, index=index)
series.plot(figsize=(100,10))




# with open('data.json') as data:
#     d = json.load(data)
#     print(d)

# index = pd.to_datetime(list(d.keys()))
# values = [float(s.split()[0]) if s else None for s in d.values() ]


