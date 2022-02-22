cookbook = { 'sandwich' : {'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
                            'meal' : 'lunch',
                            'prep_time' : '10'},
            'cake'      : {'ingredients' : ['flour', 'sugar', 'eggs'],
                            'meal' : 'dessert',
                            'prep_time' : '60'},
            'cake'      : {'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
                            'meal' : 'lunch',
                            'prep_time' : '15'}
            }

def printrecipe(res):
    item = cookbook[res]
    ing = item['ingredients']
    meal = item['meal']
    eta = item['prep_time']
    print('Sandwich’s ingredients are ham

printrecipe('sandwich')
