def Jaccard(s1, s2):
    """

    :param s1: set one
    :param s2: set two
    :return: the similarity
    """
    numer = len(s1.intersection(s2))
    denom = len(s1.union(s2))
    return numer / denom

def mostSimilar_recipe(i, iPerR):
    """

    :param i: target recipe name
    :param iPerR: the recipe set
    :return: the most similar 5 recipes
    """
    similarities = []
    ing = iPerR[i]
    for i2 in iPerR:
        if i2 == i: continue
        sim = Jaccard(ing, iPerR[i2])
        similarities.append((sim,i2))
    similarities.sort(key=lambda x: (-x[0]))
    return similarities[:5]

def mostSimilar_ingredient(i, rPerI):
    """

    :param i: target ingredient name
    :param rPerI: the ingredient set
    :return: the most similar 5 ingredients
    """
    similarities = []
    reci = rPerI[i]
    for i2 in rPerI:
        if i2 == i: continue
        sim = Jaccard(reci, rPerI[i2])
        similarities.append((sim,i2))
    similarities.sort(key=lambda x: (-x[0], x[1]))
    return similarities[:5]

def mostSimilar_recipte_given_ingredients(ing, iPerR):
    """

    :param ingredients:
    :return:
    """
    similarities2 = []
    for i2 in iPerR:
        sim = Jaccard(ing, iPerR[i2])
        similarities2.append((sim, i2, iPerR[i2]))
    similarities2.sort(key=lambda x: (-x[0]))
    return similarities2
