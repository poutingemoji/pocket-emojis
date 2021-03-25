import json

# Pre-sort the formulas for a constant-time lookup
with open('../../src/data/formulas.json', encoding='utf8') as json_file:

    formulas = json.load(json_file)
    
    sorted_formulas = {}
    for formula, result in formulas.items():
        sorted_formulas[''.join(sorted(formula))] = result


def react(*args):
    formula = "".join(sorted("".join([arg for arg in args])))
    try:
        return sorted_formulas[formula]
    except KeyError:
        return None
