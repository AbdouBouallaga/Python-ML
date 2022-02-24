cookbook = {'sandwich': {
    'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
    'meal': 'lunch',
    'prep_time': '10'
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': '60'
        },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': '15'
        }
    }


def clr():
    print("\033c", end="")


def printrecipe(res, *deb):
    print()
    item = cookbook[res]
    ing = item['ingredients']
    meal = item['meal']
    eta = item['prep_time']
    print("Recipe for", res, end=':\n')
    print("Ingredients list:", ing)
    print("To be eaten for", meal, end=".\n")
    print("Takes "+eta+" minutes of cooking.", end='\n\n')
    if not deb:
        print("0: Back")
        print("1: Main menu")
        inp = input(">>")
        if inp.isdigit():
            if inp == '0':
                meals()
            elif inp == '1':
                menu()
        clr()
        printrecipe(res)


def meals(*deb):
    if not deb:
        clr()
    i = 1
    dict_m = {}
    for meal in cookbook:
        dict_m[i] = meal
        meal = meal.capitalize()
        print(i, meal, sep=": ")
        i += 1
    print("0: Back")
    ch = input(">> ")
    if ch.isdigit() and int(ch) <= i:
        ch = int(ch)
        if ch == 0:
            menu()
        else:
            printrecipe(dict_m[ch])
    else:
        clr()
        print("Please select an option by typing the corresponding number:")
        meals(1)


def save(name, item):
    cookbook[name] = item
    menu()


def asksave(name, item):
    ch = input("\nSave this recipe ? y = Yes; n = No.\n>> ")
    if ch == 'y' or ch == 'Y' or ch == 'yes':
        save(name, item)
    elif ch == 'n' or ch == 'N' or ch == 'no':
        menu()
    else:
        asksave(name, item)


def addrecipe():
    clr()
    item = {}
    print("Add your new recipe.")
    name = input("Name of the recipe:\n>> ")
    item['ingredients'] = input(
            "Ingredients (separated with ',' ex: eggs,sugar...):\n>> "
            ).split(',')
    item['meal'] = input("Type ex: dessert:\n>> ")
    item['prep_time'] = input("Preparation time:\n>> ")
    asksave(name, item)


def printall():
    clr()
    print("Welcome")
    for meal in cookbook:
        printrecipe(meal, 1)
    print("0: Main menu")
    ch = input(">> ")
    if ch == '0':
        menu()
    else:
        clr()
        printall()


def delete():
    i = 1
    dict_m = {}
    for meal in cookbook:
        dict_m[i] = meal
        print(i, meal, sep=": ")
        i += 1
    nm = input("Which one you want to delete ?\n>> ")
    print("0: Back")
    if nm.isdigit() and int(nm) <= i:
        if (nm == '0'):
            menu()
        ch = input(
                "\nDelete " +
                dict_m[int(nm)]
                + " recipe ? y = Yes; n = No.\n>> ")
        if ch == 'y' or ch == 'Y' or ch == 'yes':
            del cookbook[dict_m[int(nm)]]
        elif ch == 'n' or ch == 'N' or ch == 'no':
            delete()
    else:
        print("Please select an option by typing the corresponding number:")
        delete()


def menu():
    clr()
    menu_l = [
            'Add a recipe', 'Delete a recipe',
            'Print a recipe', 'Print the cookbook',
            'Quit'
            ]
    print("Please select an option by typing the corresponding number:")
    for i, m in enumerate(menu_l):
        print(i+1, m, sep=': ', end='\n')
    inp = input(">> ")
    print()
    if (inp == '1'):
        addrecipe()
    elif (inp == '2'):
        delete()
    elif (inp == '4'):
        printall()
    elif (inp == '5'):
        print('Cookbook closed.')
        quit()
    elif (inp == '3'):
        meals()
    menu()


if __name__ == "__main__":
    menu()
    print()
