# FoodMe: User-Guided Recipe Recommendations

## Dataset
https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions

## Project Idea
With the vast number of recipes and food blogs online, it can be a real challenge to pick out the recipes that you want to try, and get enough variety in your life. To combat this, we look to build a flexible, user-powered recommendation system for recipes.

## Dependencies
Usage has been guaranteed as of Python 3.8
* matplotlib
* nltk
* numpy
* pandas
* plotly
* wordcloud
* sklearn

## Installation and Use
### Installation
We recommend installing in a virtual environment to ensure package 
compatability. 

Installation of the source code simply requires
```bash
$ git clone https://github.com/michaelbaluja/ECE143_WI22_FinalProject_Group14.git
$ cd ECE143_WI22_FinalProject_Group14
$ pip install .
```

### Use
To run the notebook code, open Jupyter Notebook and simply run the cells
provided. There are helper functions provided through ```scripts/``` for 
cleaning the data and creating recommendations. To get a recommendation, you
can run ```main.py``` from ```scripts/Recommender System```.

The data used for development can be found under the ```data``` folder. When running,
ensure that the proper file path is configured for reading in the data.

## File Structure
```
data/
├── ingr_map.pkl
├── interactions_test.csv
├── interactions_train.csv
├── interactions_validation.csv
├── PP_recipes.csv
├── PP_users.csv
├── RAW_interactions.csv
└── RAW_recipes.csv
notebooks/
├── Data_Vis.ipynb
├── Exploratory_Analysis.ipynb
└── Recipe recommendation based on ingredients.ipynb
scripts/
├── Data Visualization/
│   ├── main.py
│   ├── histogram.py
│   ├── pie_chart.py
│   └── word_cloud.py
├── Recommender System/
│   ├── compute_similarity.py
│   ├── getNewIngredients.py
│   ├── load_data.py
│   ├── main.py
│   └── visualization.py
├── PDV Analysis/
│   └── final_pdv_analysis.py
├── High Rating Reason/
│   └── why_high_rating.py
└── cleaning.py
presentation/
└── ECE143_Group14.pptx.pdf
README.md
setup.py
```
