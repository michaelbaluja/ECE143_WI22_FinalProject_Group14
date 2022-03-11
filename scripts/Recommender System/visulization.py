import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def plotBarh(num_list, prob, saveName):
    """
    plot  the barh image of the input list
    :param num_list: x
    :param prob: y
    :param saveName: the image save name
    :return: none
    """
    assert isinstance(num_list, list)
    assert isinstance(prob, list)
    assert isinstance(saveName, str)

    plt.barh(range(len(prob)), prob, tick_label=num_list)
    plt.savefig(saveName)
    plt.show()


def plotNutrientContent(f, num_list):
    """
    plot nutrient content of the input recipes
    :param f: the dataset
    :param num_list: the
    :return: none
    """
    assert isinstance(f, pd.DataFrame)
    assert isinstance(num_list, list)

    list1 = eval(f.iloc[f[f.name == num_list[0]].index.tolist()[0]]["nutrition"])
    list2 = eval(f.iloc[f[f.name == num_list[1]].index.tolist()[0]]["nutrition"])
    list3 = eval(f.iloc[f[f.name == num_list[2]].index.tolist()[0]]["nutrition"])
    list4 = eval(f.iloc[f[f.name == num_list[3]].index.tolist()[0]]["nutrition"])
    list5 = eval(f.iloc[f[f.name == num_list[4]].index.tolist()[0]]["nutrition"])

    x = [1, 2, 3, 4, 5]
    k1 = [list1[0], list2[0], list3[0], list4[0], list5[0]]
    plt.plot(x, k1, 's-', color='r', label="calories")
    plt.xlabel("Recipe Number")
    plt.ylabel("Content(g/mg)")
    plt.legend(loc="best")
    plt.savefig("Recipe number vs. Calories.jpg")
    plt.show()

    x = [1, 2, 3, 4, 5]
    k2 = [list1[1],list2[1],list3[1],list4[1],list5[1]]
    k3 = [list1[2],list2[2],list3[2],list4[2],list5[2]]
    k4 = [list1[3],list2[3],list3[3],list4[3],list5[3]]
    k5 = [list1[4],list2[4],list3[4],list4[4],list5[4]]
    plt.plot(x,k2,'o-',color = 'g',label="total fat")
    plt.plot(x,k3,'o-',color = 'b',label="sugar")
    plt.plot(x,k4,'o-',color = 'y',label="sodium")
    plt.plot(x,k5,'o-',color = 'c',label="protein")
    plt.xlabel("Recipe Number")
    plt.ylabel("Content(g/mg)")
    plt.legend(loc="best")
    plt.savefig("Recipe number vs. content.jpg")
    plt.show()

def plotRecipeTimeAndStep(f, num_list):
    """
    plot time and steps of the input recipes
    :param f:
    :param num_list: the input list to plot
    :return: none
    """
    assert isinstance(f, pd.DataFrame)
    assert isinstance(num_list, list)

    k1, k2 = [], []
    for i in range(5):
        k1.append(f.iloc[f[f.name == num_list[i]].index.tolist()[0]]["minutes"])
        k2.append(f.iloc[f[f.name == num_list[i]].index.tolist()[0]]["n_steps"])
    fig, ax = plt.subplots()
    x = [1, 2, 3, 4, 5]
    ax.bar(np.arange(5), k1, tick_label=x, width=0.45, label='time')
    ax.bar(np.arange(5) + 0.45, k2, tick_label=x, width=0.45, label='steps')
    plt.xlabel("Recipe Number")
    plt.ylabel("time/steps number")
    ax.legend()
    plt.savefig("Recipe number vs. time or steps.jpg")
    plt.show()