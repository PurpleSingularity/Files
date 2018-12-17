import plotly.offline as pl
import plotly.graph_objs as go

f = open('Students.csv', 'r', encoding='utf-8', newline='\n')
dataset = []
f.readline()
data = f.readlines()
f.close()

for i in range(1, len(data)):
    dict_element = {
        'gender': '',
        'race': '',
        'par_lvl': '',
        'lunch': '',
        'prepare': '',
        'score': {
            'math': '',
            'reading': '',
            'writing': ''
        }
    }
    string = data[i]
    data_lst = string.split(',')
    dict_element['gender'] = data_lst[0].strip('"')
    dict_element['race'] = data_lst[1].strip('"')
    dict_element['par_lvl'] = data_lst[2].strip('"')
    dict_element['lunch'] = data_lst[3].strip('"')
    dict_element['prepare'] = data_lst[4].strip('"')
    dict_element['score']['math'] = data_lst[5].strip('"')
    dict_element['score']['reading'] = data_lst[6].strip('"')
    dict_element['score']['writing'] = data_lst[7].strip('"')
    dataset.append(dict_element)



math_score_data = {
    'group A' : {
        'male' : [],
        'female' : []
    },
    'group B' : {
        'male' : [],
        'female' : []
    },
    'group C' : {
        'male': [],
        'female': []
    },
    'group D' : {
        'male': [],
        'female': []
    },
    'group E' : {
        'male': [],
        'female': []
    }
}

for i in dataset:
    race = i['race']
    gender = i['gender']
    score = int(i['score']['math'])
    math_score_data[race][gender].append(score)

print(math_score_data)

def Sum (lst):
    out = 0
    for i in lst:
        out += int(i)
    return out

for i in math_score_data.values():
    sum_male = Sum(i['male'])
    sum_female = Sum(i['female'])
    i['male'] = sum_male / len(i['male'])
    i['female'] = sum_female / len(i['female'])

print(math_score_data)

x = []
ym = []
yf = []

for i in math_score_data.keys():
    x.append(i)
print(x)

for i in math_score_data.values():
    ym.append(i['male'])
print(ym)

for i in math_score_data.values():
    yf.append(i['female'])
print(yf)

pl.plot({
    'data' : [
        go.Bar(x = x, y = ym),
        go.Bar(x = x, y = yf)
    ]
})