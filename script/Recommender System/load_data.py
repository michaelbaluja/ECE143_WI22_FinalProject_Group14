import pandas as pd
from collections import defaultdict

def loadData(aPath):
    """

    :return:
    """
    f = pd.read_csv(aPath)

    iPerR = defaultdict(set)
    rPerI = defaultdict(set)
    for j in range(f.shape[0]):
        ingredientList = eval(f["ingredients"][j])
        for i in range(len(ingredientList)):
            ingredient, recipe = ingredientList[i], f['name'][j]
            iPerR[recipe].add(ingredient)
            rPerI[ingredient].add(recipe)
    return f, iPerR, rPerI
