import pandas as pd
import plotly.express as px

def pie_chart(data, data2):
    minutes = data['minutes'].tolist()
    interval = {}
    interval['Time <= 30 min'] = len([i for i in minutes if i <= 30])
    interval['30 < Time <= 60 min'] = len([i for i in minutes if 30 < i <= 60])
    interval['60 < Time <= 90 min'] = len([i for i in minutes if 60 < i <= 90])
    interval['90 < Time <= 120 min'] = len([i for i in minutes if 90 < i <= 120])
    interval['120 < Time <= 150 min'] = len([i for i in minutes if 120 < i <= 150])
    interval['150 < Time'] = len([i for i in minutes if 150 < i])

    col1 = [i for i in interval.keys()]
    col2 = [i for i in interval.values()]
    c = {'a': col1, 'b': col2}
    da = pd.DataFrame(c)
    fig = px.pie(da, values='b', names='a', title='Cooking Time for Database')
    fig.update_traces(textposition='inside', textinfo='percent+label', insidetextorientation='radial')
    fig.show()

    r = data2['rating'].tolist()
    rating = {}
    ra = [i for i in range(6)]
    for i in ra:
        rating[i] = len([j for j in r if j == i])

    col1 = [i for i in rating.keys()]
    col2 = [i for i in rating.values()]
    c = {'a': col1, 'b': col2}
    da = pd.DataFrame(c)
    fig = px.pie(da, values='b', names='a', title='Rating for Database')
    fig.update_traces(textposition='inside', textinfo='percent+label', insidetextorientation='radial')
    fig.show()

    nutrition = data['nutrition'].tolist()
    nu = [eval(i) for i in nutrition]
    interval = {}
    interval['Calories <= 200'] = len([i[0] for i in nu if i[0] <= 200])
    interval['200 < Calories <= 400'] = len([i[0] for i in nu if 200 < i[0] <= 400])
    interval['400 < Calories <= 600'] = len([i[0] for i in nu if 400 < i[0] <= 600])
    interval['600 < Calories <= 800'] = len([i[0] for i in nu if 600 < i[0] <= 800])
    interval['800 < Calories <= 1000'] = len([i[0] for i in nu if 800 < i[0] <= 1000])
    interval['1000 < Calories'] = len([i[0] for i in nu if 1000 < i[0]])

    col1 = [i for i in interval.keys()]
    col2 = [i for i in interval.values()]
    c = {'a': col1, 'b': col2}
    da = pd.DataFrame(c)
    fig = px.pie(da, values='b', names='a', title='Calories for Database')
    fig.update_traces(textposition='inside', textinfo='percent+label', insidetextorientation='radial')
    fig.show()
