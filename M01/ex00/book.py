if "datetime.datetime" not in dir():
    import datetime


class book:
    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.recipes_list = {"starter": {},
                             "lunch": {},
                             "dessert": {}
                             }

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipe_type][recipe.name] = recipe
        self.last_update = datetime.datetime.now()

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and
        returns the instance"""
        for recipe_type in self.recipes_list:
            if name in self.recipes_list[recipe_type]:
                print(self.recipes_list[recipe_type][name])
        pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for recipe in self.recipes_list[recipe_type]:
            self.get_recipe_by_name(recipe)
        pass
