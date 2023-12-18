# Import statements
from urllib import request, parse
import json

from objects import Category, Meal, Area, Recipe


# Get a list of the meal categories from themealdb
def get_categories():
    url = "https://www.themealdb.com/api/json/v1/1/list.php?c=list"
    f = request.urlopen(url)
    categories = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for category_data in data['meals']:
            category = Category(category_data['strCategory'])

            categories.append(category)
    except (ValueError, KeyError, TypeError):
        return None

    return categories

# Get meals by inputted category
def get_meals_by_category(category):
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + parse.quote(category)
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            meal = Meal(meal_data['idMeal'],
                        meal_data['strMeal'],
                        meal_data['strMealThumb'])
            meals.append(meal)
    except (ValueError, KeyError, TypeError):
        return None

    return meals


# Get a list of the meal areas from themealdb
def get_areas():
    url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
    f = request.urlopen(url)
    areas = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for area_data in data['meals']:
            area = Area(area_data['strArea'])

            areas.append(area)
    except (ValueError, KeyError, TypeError):
        return None

    return areas

# Get meals by inputted area
def get_meals_by_area(area):
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?a=" + parse.quote(area)
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            meal = Meal(meal_data['idMeal'],
                        meal_data['strMeal'],
                        meal_data['strMealThumb'])
            meals.append(meal)
    except (ValueError, KeyError, TypeError):
        return None

    return meals

# Get meals by inputted name
def get_meals_by_name(name):
    url = "https://www.themealdb.com/api/json/v1/1/search.php?s=" + parse.quote(name)
    f = request.urlopen(url)
    meals = []
    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            meal = Recipe(meal_data['idMeal'], meal_data['strMeal'], meal_data['strMealThumb'],
                             meal_data['strInstructions'], meal_data['strIngredient1'],
                             meal_data['strIngredient2'], meal_data['strIngredient3'], meal_data['strIngredient4'],
                             meal_data['strIngredient5'], meal_data['strIngredient6'], meal_data['strIngredient7'],
                             meal_data['strIngredient8'], meal_data['strIngredient9'], meal_data['strIngredient10'],
                             meal_data['strIngredient11'], meal_data['strIngredient12'], meal_data['strIngredient13'],
                             meal_data['strIngredient14'], meal_data['strIngredient15'], meal_data['strIngredient16'],
                             meal_data['strIngredient17'], meal_data['strIngredient18'], meal_data['strIngredient19'],
                             meal_data['strIngredient20'], meal_data['strMeasure1'], meal_data['strMeasure2'],
                             meal_data['strMeasure3'], meal_data['strMeasure4'], meal_data['strMeasure5'],
                             meal_data['strMeasure6'], meal_data['strMeasure7'], meal_data['strMeasure8'],
                             meal_data['strMeasure9'], meal_data['strMeasure10'], meal_data['strMeasure11'],
                             meal_data['strMeasure12'], meal_data['strMeasure13'], meal_data['strMeasure14'],
                             meal_data['strMeasure15'], meal_data['strMeasure16'], meal_data['strMeasure17'],
                             meal_data['strMeasure18'], meal_data['strMeasure19'], meal_data['strMeasure20'])
            meals.append(meal)
    except(ValueError, KeyError, TypeError):
        return None

    return meals

# Hence the name, get a random meal
def get_random_meal():
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    f = request.urlopen(url)
    meals = []
    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            meal = Recipe(meal_data['idMeal'], meal_data['strMeal'], meal_data['strMealThumb'],
                             meal_data['strInstructions'], meal_data['strIngredient1'],
                             meal_data['strIngredient2'], meal_data['strIngredient3'], meal_data['strIngredient4'],
                             meal_data['strIngredient5'], meal_data['strIngredient6'], meal_data['strIngredient7'],
                             meal_data['strIngredient8'], meal_data['strIngredient9'], meal_data['strIngredient10'],
                             meal_data['strIngredient11'], meal_data['strIngredient12'], meal_data['strIngredient13'],
                             meal_data['strIngredient14'], meal_data['strIngredient15'], meal_data['strIngredient16'],
                             meal_data['strIngredient17'], meal_data['strIngredient18'], meal_data['strIngredient19'],
                             meal_data['strIngredient20'], meal_data['strMeasure1'], meal_data['strMeasure2'],
                             meal_data['strMeasure3'], meal_data['strMeasure4'], meal_data['strMeasure5'],
                             meal_data['strMeasure6'], meal_data['strMeasure7'], meal_data['strMeasure8'],
                             meal_data['strMeasure9'], meal_data['strMeasure10'], meal_data['strMeasure11'],
                             meal_data['strMeasure12'], meal_data['strMeasure13'], meal_data['strMeasure14'],
                             meal_data['strMeasure15'], meal_data['strMeasure16'], meal_data['strMeasure17'],
                             meal_data['strMeasure18'], meal_data['strMeasure19'], meal_data['strMeasure20'])
            meals.append(meal)
    except(ValueError, KeyError, TypeError):
        return None

    return meals

