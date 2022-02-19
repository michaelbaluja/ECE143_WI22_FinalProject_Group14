# FoodMe: User-Guided Recipe Recommendations

## Dataset
https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions

## Problem Statement
With the vast number of recipes and food blogs online, it can be a real challenge to pick out the recipes that you want to try, and get enough variety in your life. To combat this, we look to build a flexible, user-powered recommendation system for recipes.

## Proposed Solution
To provide recommendations, we consider using a weighted k-nearest neighbors algorithm on the recipes to provide k different ranked recommendations. The ranks allow the user to choose what is most important to them in a recipe. This can include things such as specific ingredients for people cooking with limited items, cook time for people who need something fast, nutrition information for health-conscious people or those with dietary restrictions, and difficulty for those who are a pro or may not know their way around the kitchen. 

In addition to the method mentioned above, we also intend to use collaborative filtering, latent factor models to build the recommender system. Based on the recipes that the user has made in the past, combined with the user's ratings of recipes, and analyzing the preferences of other users who are similar to the user's preferences, the potential recipes that the user may make in the future can be predicted.

Based on the above analysis, there is certainly a real-world use for this algorithm. As many people during the pandemic have had to stay at home and chosen to cook more, along with many people facing job and food insecurity, it’s important for people to have access to recipes that they can use and tailor for their needs, along with the ability to get inspiration on limited resources. The food we eat is what powers us, and it’s vital that we get to control it. 
