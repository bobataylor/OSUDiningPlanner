import requests
import json
import manage
from planner.models import Location, Food

r = requests.get('https://content.osu.edu/v2/api/v1/dining/locations/menus')
location_data = json.loads(r)["data"]["locationsMenus"]
for location in location_data:
    print(location["locationName"])
