def getNewIngredients(f, ing):
    ingredients = []
    for i in range(f.shape[0]):
        ingredients.extend(eval(f['ingredients'][i]))

    dict = {}
    for key in ingredients:
        dict[key] = dict.get(key, 0) + 1

    new = []
    for s in ing:
        for i in dict:
            if s.find(i) != -1 and dict[i] > 300:
                    new.append(i)

    for s in ing:
        dict2 = {}
        for key in dict:
            if key.find(s) != -1:
                dict2[key] = dict[key]
        ww = sorted(dict2.items(), key=lambda x: x[1], reverse=True)
        if dict[ww[0][0]] > 300:
            new.append(ww[0][0])

    return set(new)