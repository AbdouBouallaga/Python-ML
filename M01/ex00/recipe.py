class recipe:
    def __init__(self, name, cooking_lvl,
                 cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    @property
    def name(self):
        return self._name

    @property
    def cooking_lvl(self):
        return self._cooking_lvl

    @property
    def cooking_time(self):
        return self._cooking_time

    @property
    def ingredients(self):
        return self._ingredients

    @property
    def recipe_type(self):
        return self._recipe_type

    @name.setter
    def name(self, value):
        if type(value) is not str:
            print(type(value))
            print("Name must be a string")
            quit()
        else:
            self._name = value

    @cooking_lvl.setter
    def cooking_lvl(self, value):
        if type(value) is not int or value not in range(1, 5, 1):
            print("Cooking level must be in range of 1 to 5")
            quit()
        else:
            self._cooking_lvl = value

    @cooking_time.setter
    def cooking_time(self, value):
        if value < 0:
            print("Cooking time must be a positif digit in minutes")
            quit()
        else:
            self._cooking_time = value

    @ingredients.setter
    def ingredients(self, value):
        bad = 0
        if type(value) is not list:
            bad = 1
        for st in value:
            if type(st) is not str:
                bad = 1
        if bad:
            print("Ingredients must be a list of strings")
            quit()
        else:
            self._ingredients = value

    @recipe_type.setter
    def recipe_type(self, value):
        bad = 0
        valid = ['starter', 'lunch', 'dessert']
        if type(value) is not str:
            bad = 1
        if value not in valid:
            bad = 1
        if bad:
            print("Recipe type must be: starter, lunch or dessert.")
            quit()
        else:
            self._recipe_type = value

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "Name: " + self.name + "\n"
        txt += "Cooking level: " + str(self.cooking_lvl) + "\n"
        txt += "Cooking time: " + str(self.cooking_time) + "\n"
        txt += "Ingredients: " + str(self.ingredients) + "\n"
        txt += "Description: " + self.description + "\n"
        txt += "Recipe type: " + self.recipe_type + "\n"
        return(txt)
