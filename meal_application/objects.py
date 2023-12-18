# Category class
class Category:
    def __init__(self, category):
        self.__category = category

    def get_name(self):
        return self.__category

    def set_name(self, category):
        self.__category = category

# Area class
class Area:
    def __init__(self, area):
        self.__area = area

    def get_name(self):
        return self.__area

    def set_name(self, area):
        self.__area = area

# Meal class, used for category and area related methods
class Meal:
    def __init__(self, meal_id, meal_name, meal_thumb):
        self.__meal_id = meal_id
        self.__meal_name = meal_name
        self.__meal_thumb = meal_thumb

    def get_meal_id(self):
        return self.__meal_id

    def set_meal_id(self, meal_id):
        self.__meal_id = meal_id

    def get_name(self):
        return self.__meal_name

    def set_name(self, meal_name):
        self.__meal_name = meal_name

    def get_meal_thumb(self):
        return self.__meal_thumb

    def set_meal_thumb(self, meal_thumb):
        self.__meal_thumb = meal_thumb

# Recipe class, used for the recipe by name and random meal methods
# Variables for each meal ingredient and meal measure were created
class Recipe:
    def __init__(self, meal_id, meal_name, meal_thumb, meal_instructions, meal_ingredient1,
                 meal_ingredient2, meal_ingredient3, meal_ingredient4, meal_ingredient5,
                 meal_ingredient6, meal_ingredient7, meal_ingredient8, meal_ingredient9,
                 meal_ingredient10, meal_ingredient11, meal_ingredient12, meal_ingredient13,
                 meal_ingredient14, meal_ingredient15, meal_ingredient16, meal_ingredient17,
                 meal_ingredient18, meal_ingredient19, meal_ingredient20, meal_measure1,
                 meal_measure2, meal_measure3, meal_measure4, meal_measure5, meal_measure6,
                 meal_measure7, meal_measure8, meal_measure9, meal_measure10, meal_measure11,
                 meal_measure12, meal_measure13, meal_measure14, meal_measure15, meal_measure16,
                 meal_measure17, meal_measure18, meal_measure19, meal_measure20):

        self.__meal_id = meal_id
        self.__meal_name = meal_name
        self.__meal_thumb = meal_thumb
        self.__meal_instructions = meal_instructions

        self.__meal_ingredient1 = meal_ingredient1
        self.__meal_ingredient2 = meal_ingredient2
        self.__meal_ingredient3 = meal_ingredient3
        self.__meal_ingredient4 = meal_ingredient4
        self.__meal_ingredient5 = meal_ingredient5
        self.__meal_ingredient6 = meal_ingredient6
        self.__meal_ingredient7 = meal_ingredient7
        self.__meal_ingredient8 = meal_ingredient8
        self.__meal_ingredient9 = meal_ingredient9
        self.__meal_ingredient10 = meal_ingredient10
        self.__meal_ingredient11 = meal_ingredient11
        self.__meal_ingredient12 = meal_ingredient12
        self.__meal_ingredient13 = meal_ingredient13
        self.__meal_ingredient14 = meal_ingredient14
        self.__meal_ingredient15 = meal_ingredient15
        self.__meal_ingredient16 = meal_ingredient16
        self.__meal_ingredient17 = meal_ingredient17
        self.__meal_ingredient18 = meal_ingredient18
        self.__meal_ingredient19 = meal_ingredient19
        self.__meal_ingredient20 = meal_ingredient20

        self.__meal_measure1 = meal_measure1
        self.__meal_measure2 = meal_measure2
        self.__meal_measure3 = meal_measure3
        self.__meal_measure4 = meal_measure4
        self.__meal_measure5 = meal_measure5
        self.__meal_measure6 = meal_measure6
        self.__meal_measure7 = meal_measure7
        self.__meal_measure8 = meal_measure8
        self.__meal_measure9 = meal_measure9
        self.__meal_measure10 = meal_measure10
        self.__meal_measure11 = meal_measure11
        self.__meal_measure12 = meal_measure12
        self.__meal_measure13 = meal_measure13
        self.__meal_measure14 = meal_measure14
        self.__meal_measure15 = meal_measure15
        self.__meal_measure16 = meal_measure16
        self.__meal_measure17 = meal_measure17
        self.__meal_measure18 = meal_measure18
        self.__meal_measure19 = meal_measure19
        self.__meal_measure20 = meal_measure20

    def get_meal_id(self):
        return self.__meal_id

    def set_meal_id(self, meal_id):
        self.__meal_id = meal_id

    def get_name(self):
        return self.__meal_name

    def set_name(self, meal_name):
        self.__meal_name = meal_name

    def get_meal_thumb(self):
        return self.__meal_thumb

    def set_meal_thumb(self, meal_thumb):
        self.__meal_thumb = meal_thumb

    def get_instructions(self):
        return self.__meal_instructions

    def set_meal_instructions(self, meal_instructions):
        self.__meal_instructions = meal_instructions

    def get_ingredient1(self):
        return self.__meal_ingredient1

    def set_meal_ingredient1(self, meal_ingredient1):
        self.__meal_ingredient1 = meal_ingredient1

    def get_ingredient2(self):
        return self.__meal_ingredient2

    def set_meal_ingredient2(self, meal_ingredient2):
        self.__meal_ingredient2 = meal_ingredient2

    def get_ingredient3(self):
        return self.__meal_ingredient3

    def set_meal_ingredient3(self, meal_ingredient3):
        self.__meal_ingredient3 = meal_ingredient3

    def get_ingredient4(self):
        return self.__meal_ingredient4

    def set_meal_ingredient4(self, meal_ingredient4):
        self.__meal_ingredient4 = meal_ingredient4

    def get_ingredient5(self):
        return self.__meal_ingredient5

    def set_meal_ingredient5(self, meal_ingredient5):
        self.__meal_ingredient5 = meal_ingredient5

    def get_ingredient6(self):
        return self.__meal_ingredient6

    def set_meal_ingredient6(self, meal_ingredient6):
        self.__meal_ingredient6 = meal_ingredient6

    def get_ingredient7(self):
        return self.__meal_ingredient7

    def set_meal_ingredient7(self, meal_ingredient7):
        self.__meal_ingredient7 = meal_ingredient7

    def get_ingredient8(self):
        return self.__meal_ingredient8

    def set_meal_ingredient8(self, meal_ingredient8):
        self.__meal_ingredient8 = meal_ingredient8

    def get_ingredient9(self):
        return self.__meal_ingredient9

    def set_meal_ingredient9(self, meal_ingredient9):
        self.__meal_ingredient9 = meal_ingredient9

    def get_ingredient10(self):
        return self.__meal_ingredient10

    def set_meal_ingredient10(self, meal_ingredient10):
        self.__meal_ingredient10 = meal_ingredient10

    def get_ingredient11(self):
        return self.__meal_ingredient11

    def set_meal_ingredient11(self, meal_ingredient11):
        self.__meal_ingredient11 = meal_ingredient11

    def get_ingredient12(self):
        return self.__meal_ingredient12

    def set_meal_ingredient12(self, meal_ingredient12):
        self.__meal_ingredient12 = meal_ingredient12

    def get_ingredient13(self):
        return self.__meal_ingredient13

    def set_meal_ingredient13(self, meal_ingredient13):
        self.__meal_ingredient13 = meal_ingredient13

    def get_ingredient14(self):
        return self.__meal_ingredient14

    def set_meal_ingredient14(self, meal_ingredient14):
        self.__meal_ingredient14 = meal_ingredient14

    def get_ingredient15(self):
        return self.__meal_ingredient15

    def set_meal_ingredient15(self, meal_ingredient15):
        self.__meal_ingredient15 = meal_ingredient15

    def get_ingredient16(self):
        return self.__meal_ingredient16

    def set_meal_ingredient16(self, meal_ingredient16):
        self.__meal_ingredient16 = meal_ingredient16

    def get_ingredient17(self):
        return self.__meal_ingredient17

    def set_meal_ingredient17(self, meal_ingredient17):
        self.__meal_ingredient17 = meal_ingredient17

    def get_ingredient18(self):
        return self.__meal_ingredient18

    def set_meal_ingredient18(self, meal_ingredient18):
        self.__meal_ingredient18 = meal_ingredient18

    def get_ingredient19(self):
        return self.__meal_ingredient19

    def set_meal_ingredient19(self, meal_ingredient19):
        self.__meal_ingredient19 = meal_ingredient19

    def get_ingredient20(self):
        return self.__meal_ingredient20

    def set_meal_ingredient20(self, meal_ingredient20):
        self.__meal_ingredient20 = meal_ingredient20

    def get_measure1(self):
        return self.__meal_measure1

    def set_meal_measure1(self, meal_measure1):
        self.__meal_measure1 = meal_measure1

    def get_measure2(self):
        return self.__meal_measure2

    def set_meal_measure2(self, meal_measure2):
        self.__meal_measure2 = meal_measure2

    def get_measure3(self):
        return self.__meal_measure3

    def set_meal_measure3(self, meal_measure3):
        self.__meal_measure3 = meal_measure3

    def get_measure4(self):
        return self.__meal_measure4

    def set_meal_measure4(self, meal_measure4):
        self.__meal_measure4 = meal_measure4

    def get_measure5(self):
        return self.__meal_measure5

    def set_meal_measure5(self, meal_measure5):
        self.__meal_measure5 = meal_measure5

    def get_measure6(self):
        return self.__meal_measure6

    def set_meal_measure6(self, meal_measure6):
        self.__meal_measure6 = meal_measure6

    def get_measure7(self):
        return self.__meal_measure7

    def set_meal_measure7(self, meal_measure7):
        self.__meal_measure7 = meal_measure7

    def get_measure8(self):
        return self.__meal_measure8

    def set_meal_measure8(self, meal_measure8):
        self.__meal_measure8 = meal_measure8

    def get_measure9(self):
        return self.__meal_measure9

    def set_meal_measure9(self, meal_measure9):
        self.__meal_measure9 = meal_measure9

    def get_measure10(self):
        return self.__meal_measure10

    def set_meal_measure10(self, meal_measure10):
        self.__meal_measure10 = meal_measure10

    def get_measure11(self):
        return self.__meal_measure11

    def set_meal_measure11(self, meal_measure11):
        self.__meal_measure11 = meal_measure11

    def get_measure12(self):
        return self.__meal_measure12

    def set_meal_measure12(self, meal_measure12):
        self.__meal_measure12 = meal_measure12

    def get_measure13(self):
        return self.__meal_measure13

    def set_meal_measure13(self, meal_measure13):
        self.__meal_measure13 = meal_measure13

    def get_measure14(self):
        return self.__meal_measure14

    def set_meal_measure14(self, meal_measure14):
        self.__meal_measure14 = meal_measure14

    def get_measure15(self):
        return self.__meal_measure15

    def set_meal_measure15(self, meal_measure15):
        self.__meal_measure15 = meal_measure15

    def get_measure16(self):
        return self.__meal_measure16

    def set_meal_measure16(self, meal_measure16):
        self.__meal_measure16 = meal_measure16

    def get_measure17(self):
        return self.__meal_measure17

    def set_meal_measure17(self, meal_measure17):
        self.__meal_measure17 = meal_measure17

    def get_measure18(self):
        return self.__meal_measure18

    def set_meal_measure18(self, meal_measure18):
        self.__meal_measure18 = meal_measure18

    def get_measure19(self):
        return self.__meal_measure19

    def set_meal_measure19(self, meal_measure19):
        self.__meal_measure19 = meal_measure19

    def get_measure20(self):
        return self.__meal_measure20

    def set_meal_measure20(self, meal_measure20):
        self.__meal_measure20 = meal_measure20


# Name class for recipes
class Name:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

