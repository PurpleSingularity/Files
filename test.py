with open('orders.csv', encoding='utf-8', newline='\r\n') as f:
    dataset=dict()
    data=f.readlines()

    for i in range(1, len(data)):
        string=data[i]
        string=string.split(', ')
        Name=string[0]
        Date=string[1]
        Product=string[2]
        if Name not in dataset:
            dataset[Name]=dict()
        if Date not in dataset[Name]:
            dataset[Name][Date]=dict()
        dataset[Name][Date][Product]=[string[3], string[4]]
        print(dataset)

print('!!!!!!!!file is closed!!!!!!!!!')


#f.readline()
#f.close()

