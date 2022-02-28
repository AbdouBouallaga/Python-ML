from book import book
from recipe import recipe
import datetime
from time import sleep

mybook = book("hello")

print("creation_date", mybook.creation_date)
print("list before", mybook.recipes_list, end="\n\n")

mybook.add_recipe(recipe("harira",
                         3,
                         60,
                         ["hmes", "tomatos", "ze3ter", "rr3ed"],
                         "",
                         "dessert"))
sleep(2)
mybook.add_recipe(recipe("tagine",
                         3,
                         120,
                         ["potatos", "tomatos", "onions", "meatos", "saltos"],
                         "bninos",
                         "lunch"))
mybook.add_recipe(recipe("couscous",
                         4,
                         130,
                         ["couscous", "hmes", "ger3a", "dajaj"],
                         "aussi bnin",
                         "lunch"))


print("list after", mybook.recipes_list, end="\n\n")
print("last_update_date", mybook.last_update)
mybook.get_recipe_by_name("harira")
mybook.get_recipes_by_types("lunch")
