from django.core.management.base import BaseCommand, CommandError
from planner.models import Location, Food
import requests
import json

class Command(BaseCommand):
    help = 'Populates the Database from the OSU API'
    def save_food(self, section_id, location):
        r = requests.get('https://content.osu.edu/v2/api/v1/dining/full/menu/section/' + str(section_id))
        food_data = json.loads(r.text)["data"]["fullMenu"]
        for food in food_data:
            f = Food()
            f.name = food["name"] + " - " + food["portionSize"]
            f.price = food["price"]
            f.portion_size = food["portionSize"]
            f.course = food["course"]
            f.ingredients = food["ingredients"]
            if(len(food["nutrition"]) > 0):
                f.calories = food["nutrition"][0]["quantity"]
                f.total_fat = str(food["nutrition"][1]["quantity"]) + " " + food["nutrition"][1]["unitOfMeasure"]
                f.saturated_fat = str(food["nutrition"][2]["quantity"]) + " " + food["nutrition"][2]["unitOfMeasure"]
                f.trans_fat = str(food["nutrition"][3]["quantity"]) + " " + food["nutrition"][3]["unitOfMeasure"]
                f.cholestrol = str(food["nutrition"][4]["quantity"]) + " " + food["nutrition"][4]["unitOfMeasure"]
                f.sodium = str(food["nutrition"][5]["quantity"]) + " " + food["nutrition"][5]["unitOfMeasure"]
                f.total_carbohydrates = str(food["nutrition"][6]["quantity"]) + " " + food["nutrition"][6]["unitOfMeasure"]
                f.dietary_fiber = str(food["nutrition"][7]["quantity"]) + " " + food["nutrition"][7]["unitOfMeasure"]
                f.sugars = str(food["nutrition"][8]["quantity"]) + " " + food["nutrition"][8]["unitOfMeasure"]
                f.protein = str(food["nutrition"][9]["quantity"]) + " " + food["nutrition"][9]["unitOfMeasure"]
                f.vitamin_a = food["nutrition"][10]["percentOfGoal"]
                f.vitamin_c = food["nutrition"][11]["percentOfGoal"]
                f.calcium = food["nutrition"][12]["percentOfGoal"]
                f.iron = food["nutrition"][13]["percentOfGoal"]
            allergens = ""
            requirements = ""
            for trait in food["traits"]:
                if trait["category"] == "Allergen":
                    allergens += trait["name"] + ", "
                elif trait["category"] == "Requirement":
                    requirements += trait["name"] + ", "
            f.requirement = requirements[:-2]
            f.allergen = allergens[:-2]
            f.location = location
            print f.name + ", " + location.location_name
            f.save()


    def save_location(self, location_json):
        l = Location()
        l.location_name = location_json["locationName"]
        l.address = location_json["address1"]
        l.address2 = location_json["address2"]
        l.city = location_json["city"]
        l.state = location_json["state"]
        l.zipcode = location_json["zip"]
        l.dining_style = location_json["diningStyle"]
        l.icon_URL = location_json["iconUrl"]
        l.photo_URL = location_json["photoUrl"]
        l.thumbnail_URL = location_json["thumbnailUrl"]
        cuisines = ""
        for cuisine_json in location_json["cuisines"]:
            cuisines += cuisine_json["cuisineType"] + ", "
        l.cuisines = cuisines[:-2]
        l.summary = location_json["summary"]
        l.latitude = location_json["geo_lat_long"]["lat"]
        l.longitude = location_json["geo_lat_long"]["lat"]
        l.is_day_specific = False if len(location_json["locationMenu"]) == 0 else location_json["locationMenu"][0]["isDaySpecificMenu"]
        if(len(location_json["locationMenu"]) > 0):
            for menu in location_json["locationMenu"]:
                print "saving food \n"
                self.save_food(menu["sections"][0]["sectionID"], l)
        l.save()

    def handle(self, *args, **options):
        print "test"
        r = requests.get('https://content.osu.edu/v2/api/v1/dining/locations/menus')
        location_data = json.loads(r.text)["data"]["locationsMenus"]
        for location in location_data:
            self.save_location(location)
