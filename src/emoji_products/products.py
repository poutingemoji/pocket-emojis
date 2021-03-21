import json

# Pre-sort the recipes for a constant-time lookup
with open('./src/reactants.json', encoding="utf8") as json_file:

    recipes = json.load(json_file)
    
    sorted_recipes = {}
    for recipe, result in recipes.items():
        sorted_recipes[''.join(sorted(recipe))] = result


def mealify(*args):
    recipe = "".join(sorted("".join([arg for arg in args])))
    try:
        return sorted_recipes[recipe]
    except KeyError:
        return None
