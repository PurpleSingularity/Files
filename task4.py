from data import dataset
from task1 import *
from task3 import *

import plotly
import plotly.graph_objs as go


#Вивести стовпчикову діаграму: хто скільки грошей витратив.

data = recursionByUsers()

diagram = go.Bar(x=list(data.keys()), y=list(data.values()))

fig = go.Figure(data=[diagram])

plotly.offline.plot(fig, filename='expenses.html')