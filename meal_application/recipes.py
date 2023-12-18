#! /usr/bin/env python3
# Import statements
import requests
import textwrap

def show_title():
    """
        This method will display the program title to screen
    """
    print("My Recipe Program")
    print()


def show_menu():
    """
        This method will display the menu to screen
    """
    print("Command Menu")
    print("1 - List all categories")
    print("2 - List all meals for categories")
    print("3 - Search meal by name")
    print("4 - Get a random meal")
    print("5 - List all areas")
    print("6 - List all meals for an area")
    print("7 - Display menu")
    print("0 - Exit the application")
    print()


def list_categories():
    """
        This method will get and display the list of categories to screen
    """
    categories = requests.get_categories()
    print()
    if categories is None:
        print("Technical difficulties, please try again later\n")
    else:
        print("CATEGORIES")
        for i in range(len(categories)):
            category = categories[i]
            print("  " + category.get_name())
        print()


def list_meals(title, meals):
    """
        This method will display the list of
        meals for a category or area to screen
    """
    if meals is None:
        print("Technical difficulties, please try again later\n")
    else:
        print(title.upper(), "MEALS")
        for i in range(len(meals)):
            meal = meals[i]
            print("  " + meal.get_name())
        print()

def list_recipe(title, meals):
    """
        This method will display a certain recipe
    """
    if meals is None:
        print("Invalid name, please try again later\n")
    else:
        print("Recipe: ", title.upper())
        print()
        for i in range(len(meals)):
            meal = meals[i]
            print("Instructions:")
            my_wrap = textwrap.TextWrapper(width=80)
            wrap_list = my_wrap.wrap(meal.get_instructions())

            for line in wrap_list:
                print(line)
            print()
            print("Ingredients:")
            print("{:20} {:40}".format("Measure", "Ingredient"))
            print("--------------------------------------------------------------------------------")

            if not ((meal.get_measure1() == " ")):
                print("{:20} {:40}".format(meal.get_measure1(), meal.get_ingredient1()))
            if not ((meal.get_measure2() == " ")):
                print("{:20} {:40}".format(meal.get_measure2(), meal.get_ingredient2()))
            if not ((meal.get_measure3() == " ")):
                print("{:20} {:40}".format(meal.get_measure3(), meal.get_ingredient3()))
            if not ((meal.get_measure4() == " ")):
                print("{:20} {:40}".format(meal.get_measure4(), meal.get_ingredient4()))
            if not ((meal.get_measure5() == " ")):
                print("{:20} {:40}".format(meal.get_measure5(), meal.get_ingredient5()))
            if not ((meal.get_measure6() == " ")):
                print("{:20} {:40}".format(meal.get_measure6(), meal.get_ingredient6()))
            if not ((meal.get_measure7() == " ")):
                print("{:20} {:40}".format(meal.get_measure7(), meal.get_ingredient7()))
            if not ((meal.get_measure8() == " ")):
                print("{:20} {:40}".format(meal.get_measure8(), meal.get_ingredient8()))
            if not ((meal.get_measure9() == " ")):
                print("{:20} {:40}".format(meal.get_measure9(), meal.get_ingredient9()))
            if not ((meal.get_measure10() == " ")):
                print("{:20} {:40}".format(meal.get_measure10(), meal.get_ingredient10()))
            if not ((meal.get_measure11() == " ")):
                print("{:20} {:40}".format(meal.get_measure11(), meal.get_ingredient11()))
            if not ((meal.get_measure12() == " ")):
                print("{:20} {:40}".format(meal.get_measure12(), meal.get_ingredient12()))
            if not ((meal.get_measure13() == " ")):
                print("{:20} {:40}".format(meal.get_measure13(), meal.get_ingredient13()))
            if not ((meal.get_measure14() == " ")):
                print("{:20} {:40}".format(meal.get_measure14(), meal.get_ingredient14()))
            if not ((meal.get_measure15() == " ")):
                print("{:20} {:40}".format(meal.get_measure15(), meal.get_ingredient15()))
            if not ((meal.get_measure16() == " ")):
                print("{:20} {:40}".format(meal.get_measure16(), meal.get_ingredient16()))
            if not ((meal.get_measure17() == " ")):
                print("{:20} {:40}".format(meal.get_measure17(), meal.get_ingredient17()))
            if not ((meal.get_measure18() == " ")):
                print("{:20} {:40}".format(meal.get_measure18(), meal.get_ingredient18()))
            if not ((meal.get_measure19() == " ")):
                print("{:20} {:40}".format(meal.get_measure19(), meal.get_ingredient19()))
            if not ((meal.get_measure20() == " ")):
                print("{:20} {:40}".format(meal.get_measure20(), meal.get_ingredient20()))


        print()


def list_random_recipe(meals):
    """
        This method will display the random meal
    """
    print()
    print("A random meal was selected just for you! :)")
    print()
    for i in range(len(meals)):
        meal = meals[i]
        print("Recipe: ", meal.get_name().upper())
        print()
        print("Instructions:")
        my_wrap = textwrap.TextWrapper(width=80)
        wrap_list = my_wrap.wrap(meal.get_instructions())

        for line in wrap_list:
            print(line)

        print()
        print("Ingredients:")
        print("{:20} {:40}".format("Measure", "Ingredient"))
        print("--------------------------------------------------------------------------------")

        if not((meal.get_measure1() == " ")):
            print("{:20} {:40}".format(meal.get_measure1(), meal.get_ingredient1()))
        if not((meal.get_measure2() == " ")):
            print("{:20} {:40}".format(meal.get_measure2(), meal.get_ingredient2()))
        if not((meal.get_measure3() == " ")):
            print("{:20} {:40}".format(meal.get_measure3(), meal.get_ingredient3()))
        if not((meal.get_measure4() == " ")):
            print("{:20} {:40}".format(meal.get_measure4(), meal.get_ingredient4()))
        if not((meal.get_measure5() == " ")):
            print("{:20} {:40}".format(meal.get_measure5(), meal.get_ingredient5()))
        if not((meal.get_measure6() == " ")):
            print("{:20} {:40}".format(meal.get_measure6(), meal.get_ingredient6()))
        if not((meal.get_measure7() == " ")):
            print("{:20} {:40}".format(meal.get_measure7(), meal.get_ingredient7()))
        if not((meal.get_measure8() == " ")):
            print("{:20} {:40}".format(meal.get_measure8(), meal.get_ingredient8()))
        if not((meal.get_measure9() == " ")):
            print("{:20} {:40}".format(meal.get_measure9(), meal.get_ingredient9()))
        if not((meal.get_measure10() == " ")):
            print("{:20} {:40}".format(meal.get_measure10(), meal.get_ingredient10()))
        if not((meal.get_measure11() == " ")):
            print("{:20} {:40}".format(meal.get_measure11(), meal.get_ingredient11()))
        if not((meal.get_measure12() == " ")):
            print("{:20} {:40}".format(meal.get_measure12(), meal.get_ingredient12()))
        if not((meal.get_measure13() == " ")):
            print("{:20} {:40}".format(meal.get_measure13(), meal.get_ingredient13()))
        if not((meal.get_measure14() == " ")):
            print("{:20} {:40}".format(meal.get_measure14(), meal.get_ingredient14()))
        if not((meal.get_measure15() == " ")):
            print("{:20} {:40}".format(meal.get_measure15(), meal.get_ingredient15()))
        if not((meal.get_measure16() == " ")):
            print("{:20} {:40}".format(meal.get_measure16(), meal.get_ingredient16()))
        if not((meal.get_measure17() == " ")):
            print("{:20} {:40}".format(meal.get_measure17(), meal.get_ingredient17()))
        if not((meal.get_measure18() == " ")):
            print("{:20} {:40}".format(meal.get_measure18(), meal.get_ingredient18()))
        if not((meal.get_measure19() == " ")):
            print("{:20} {:40}".format(meal.get_measure19(), meal.get_ingredient19()))
        if not((meal.get_measure20() == " ")):
            print("{:20} {:40}".format(meal.get_measure20(), meal.get_ingredient20()))


    print()

def list_meals_by_category():
    """
         This method will prompt the user for a category
         and gets the meal list if the category is valid
    """
    lookup_category = input("Enter a category: ")
    print()

    categories = requests.get_categories()
    found = False

    if categories is None:
        print("Technical difficulties, please try again later\n")
    else:
        for i in range(len(categories)):
            category = categories[i]
            if category.get_name().lower() == lookup_category.lower():
                found = True
                break

        if found:
            meals = requests.get_meals_by_category(lookup_category)
            list_meals(lookup_category, meals)
        else:
            print("Invalid category, please try again.\n")


def list_areas():
    """
        This method will get and display the list of areas to screen
    """
    areas = requests.get_areas()

    if areas is None:
        print("Technical difficulties, please try again later\n")
    else:
        print("AREAS")
        for i in range(len(areas)):
            area = areas[i]
            print(" " + area.get_name())
        print()


def list_meals_by_area():
    """
         This method will prompt the user for an area
         and get the meal list if the area is valid
    """
    lookup_area = input("Enter an area: ")
    print()

    areas = requests.get_areas()
    found = False

    if areas is None:
        print("Technical difficulties, please try again later\n")
    else:
        for i in range(len(areas)):
            area= areas[i]
            if area.get_name().lower() == lookup_area.lower():
                found = True
                break

        if found:
            meals = requests.get_meals_by_area(lookup_area)
            list_meals(lookup_area, meals)
        else:
            print("Invalid area, please try again.\n")

def list_meals_by_name():
    """
         This method will prompt the user for a name
         and get the meal if the name is valid
    """
    lookup_name = input("Enter a name: ")
    print()

    meals = requests.get_meals_by_name(lookup_name)
    list_recipe(lookup_name, meals)

def list_random_meal():
    """

        This method will list a random meal
    """
    meals = requests.get_random_meal()
    list_random_recipe(meals)




def main():
    """
        This method controls the flow of the program
    """

    show_title()
    show_menu()

    while True:
        command = input("What would you like to do? ")
        if command == "1":
            list_categories()
        elif command == "2":
            list_meals_by_category()
        elif command == "3":
            list_meals_by_name()
        elif command == "4":
            list_random_meal()
        elif command == "5":
            list_areas()
        elif command == "6":
            list_meals_by_area()
        elif command == "7":
            print("Command Menu")
            print("1 - List all categories")
            print("2 - List all meals for categories")
            print("3 - Search meal by name")
            print("4 - Get a random meal")
            print("5 - List all areas")
            print("6 - List all meals for an area")
            print("7 - Display menu")
            print("0 - Exit the application")
            print()
        elif command == "0":
            print("Thank you for dining with us!")
            break
        else:
            print("Invalid command, please try again\n")

# Used to run main
if __name__ == "__main__":
    main()

