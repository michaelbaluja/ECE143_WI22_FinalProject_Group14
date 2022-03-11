def Jaccard(s1, s2):
    """
    Compute the Jaccard similarity
    Jaccard = intersection(u1, u2) / union(u1, u2)
    :param s1: set one
    :param s2: set two
    :return: the similarity result
    """
    numer = len(s1.intersection(s2))
    denom = len(s1.union(s2))
    return numer / denom

def mostSimilar_recipe(i, iPerR):
    """
    find the most similar recipe in the dataset
    :param i: target recipe name
    :param iPerR: the recipe set
    :return: the most similar 5 recipes
    """
    assert isinstance(i, str)
    assert isinstance(iPerR, dict)

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
    find the most similar ingredient in the dataset
    :param i: target ingredient name
    :param rPerI: the ingredient set
    :return: the most similar 5 ingredients
    """
    assert isinstance(i, str)
    assert isinstance(rPerI, dict)

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
