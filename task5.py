from data import dataset
from task1 import *
from task3 import *

import plotly
import plotly.graph_objs as go


#Вивести кругову діаграму: якого товару на яку суму продано.

data = recursionByUsers()

diagram = go.Pie(labels=list(data.keys()), values=list(data.values()))

plotly.offline.plot([diagram], filename='products.html')