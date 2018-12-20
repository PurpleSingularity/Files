from data import dataset

#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник
#   Викликати функцію


def addUser(user_code, country_name, money):
    if user_code not in dataset:
    	dataset.setdefault(user_code)
    	dataset[user_code] = dict()
    	dataset[user_code].setdefault(country_name)
    	dataset[user_code][country_name]=[money]
    else:
    	if country_name not in dataset[user_code]:
    		dataset[user_code].setdefault(country_name)
    		dataset[user_code][country_name]=[money]
    	else:
    		dataset[user_code][country_name].append(money)



