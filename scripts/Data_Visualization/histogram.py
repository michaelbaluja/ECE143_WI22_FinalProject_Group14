import plotly as py
import plotly.graph_objects as go

def histogram(data):
    pyplt = py.offline.plot
    s = data['n_steps'].tolist()
    st = {}
    st[41] = 0
    step = [i for i in range(1, max(s) + 1)]
    for i in step:
        if 0 < i <= 40:
            st[i] = s.count(i)
        else:
            st[41] += 1

    col1 = [i for i in st.keys()]
    col2 = [i for i in st.values()]
    c = {'a': col1, 'b': col2}
    print(c)
    trace_basic = [go.Bar(x=col1, y=col2, )]
    layout_basic = go.Layout(
        title='Number of Steps',
        xaxis=go.XAxis(range=[-0.5, 41.5], domain=[0, 1])
    )
    figure_basic = go.Figure(data=trace_basic, layout=layout_basic)
    pyplt(figure_basic, filename='Number of Steps.html')
