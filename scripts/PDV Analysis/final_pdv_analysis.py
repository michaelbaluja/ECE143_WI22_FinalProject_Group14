import torch.nn as nn
import torch
from tqdm import tqdm
import numpy as np
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme( palette="pastel")



def get_data(file_path: str):
    return pd.read_csv(f'{file_path}')

    
def get_calorie_ratio(dataset, nut_val:int)->dict:
    """
    :function
        This function creates a dictionary of individual nutritional values
        vs the year they were submitted.

    param:
        str: filI-path:
            path to where the csv dataset is located
        int: nut_val -> the nutritional DV in the dataset.
            [(calories (#), total fat (PDV), 
            sugar (PDV) , sodium (PDV) ,
             protein (PDV), saturated fat]
    """
    assert isinstance(nut_val, int)

    
    dataset['submitted'] =  pd.to_datetime(dataset['submitted'], dayfirst=True)
    submitted = np.array(list(dataset['submitted']))
    submitted = np.array([i.year for i in submitted])

    nut = np.array(list(dataset['nutrition']))
    calories = np.array([(eval(i)[nut_val])/np.sum(eval(i)) for i in nut])
    print(calories)

    zipped_calorie_vs_date = zip(submitted, calories)

    unique_years = dict(zip(np.unique(submitted), [[]for i in range(len(np.unique(submitted)))]))
    for i, (date, cal) in enumerate(zipped_calorie_vs_date):
        unique_years[date].append(cal)


    mean_cal_year = dict(zip(np.unique(submitted), [ 0 for i in range(len(np.unique(submitted)))]))

    for year in mean_cal_year.keys():
        mean_cal_year[year] = np.mean(unique_years[year])

    return mean_cal_year


def get_calorie_corr(dataset, nut_val:int)->dict:
    """
    :function
        This function creates a dictionary of individual nutritional values
        vs the year they were submitted.

    param:
        str: filI-path:
            path to where the csv dataset is located
        int: nut_val -> the nutritional DV in the dataset.
            [(calories (#), total fat (PDV), 
            sugar (PDV) , sodium (PDV) ,
             protein (PDV), saturated fat]
    """
    assert isinstance(nut_val, int)

    dataset['submitted'] =  pd.to_datetime(dataset['submitted'], dayfirst=True)
    submitted = np.array(list(dataset['submitted']))
    submitted = np.array([i.year for i in submitted])

    nut = np.array(list(dataset['nutrition']))
    calories = np.array([eval(i)[nut_val] for i in nut])

    zipped_calorie_vs_date = zip(submitted, calories)

    unique_years = dict(zip(np.unique(submitted), [[]for i in range(len(np.unique(submitted)))]))
    for i, (date, cal) in enumerate(zipped_calorie_vs_date):
        unique_years[date].append(cal)


    mean_cal_year = dict(zip(np.unique(submitted), [ 0 for i in range(len(np.unique(submitted)))]))
    mean_cal_year_raw = dict(zip(np.unique(submitted), [ 0 for i in range(len(np.unique(submitted)))]))

    for year in mean_cal_year.keys():
        mean_cal_year[year] = np.mean(unique_years[year])
        mean_cal_year_raw[year] = unique_years[year]

    return mean_cal_year,mean_cal_year_raw



def pdv_year_plot(title:str, pdv1:dict, pdv_name:str, path:str)->None:
    """
    
    """
    assert isinstance(title, str)
    assert isinstance(pdv_name, str) and isinstance(path, str)
    assert isinstance(pdv1, dict)
    
    plt.plot(list(pdv1.keys())[3:-4], list(pdv1.values())[3:-4], linewidth=5, c='b')
    plt.title(title)
    axis_ = list(pdv1.keys())
    plt.xticks(axis_[3:-4:2], rotation=70)
    plt.grid('on')
    plt.xlabel('Year Submitted')
    plt.ylabel(f'{pdv_name} (PDV)')
    plt.savefig(f'{path}', dpi=1000)
    

def pdv_corr_scatterplot(title:str, pdv1:dict, pdv2:dict, pdv1_name:str, pdv2_name:str, path:str):
    """
    Plot the scatter correlation between PDV values of different nutrition types

    params:
        tile: title of plot ->str
        pdv1, pdv2, dv dict containing year and mean of Nvalues -> dict
        pdv1_name,pdv2_name, path to save fig -> str.
        

    """
    assert isinstance(title, str)
    assert isinstance(pdv2_name, str)
    assert isinstance(pdv1_name, str) and isinstance(path, str)
    assert isinstance(pdv1, dict)
    assert isinstance(pdv2, dict)
    

    plt.scatter(list(pdv1.values())[3:-4], list(pdv2.values())[3:-4],marker='o', s=200,c='r'
    ,cmap='viridis')
    sns.regplot(list(pdv2.values())[3:-4], list(pdv1.values())[3:-4],color='g')
    plt.title(title)
    plt.xlabel(f'{pdv1_name} (PDV)')
    plt.ylabel(f'{pdv2_name} (PDV)')
    plt.savefig(path, dpi=1000)
    