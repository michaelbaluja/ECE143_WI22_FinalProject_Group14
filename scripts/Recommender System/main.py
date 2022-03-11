from load_data import loadData
from compute_similarity import *
from visulization import *
from getNewIngredients import *


f, iPerR, rPerI = loadData('RAW_recipes.csv')
print(f.head())
print(f.shape[0])

query = f['name'][500]
print(mostSimilar_recipe(query, iPerR))

ing = {'cheese', 'pepper', 'onion', 'chicken'}
similarities = mostSimilar_recipte_given_ingredients(ing, iPerR)
for j in range(5):
    print(similarities[j])

num_list = [i[1] for i in similarities[0:5]]
prob = [i[0] for i in similarities[0:5]]
plotBarh(num_list, prob, "top_5.jpg")
plotNutrientContent(f, num_list)
plotRecipeTimeAndStep(f, num_list)

ing = {'lettuce heart', 'butterscotch', 'low-fat bacon'}
similarities = mostSimilar_recipte_given_ingredients(ing, iPerR)
for j in range(5):
    print(similarities[j])

newIng = getNewIngredients(f, ing)
similarities = mostSimilar_recipte_given_ingredients(newIng, iPerR)
for j in range(5):
    print(similarities[j])