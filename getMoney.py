import re

user_input = input()
flo = re.search(r"(\d{1,4}\.\d{1,2})", user_input)
print(flo.group(1))
flo = float(flo.group(1))
print(flo)
input()

print("Task 1")

#Додати нового користувача та нову покупку
addUser(user_code = 'BB-333-2', country_name = 'France', money = '2222.22 usd')

#Додати існуючому користувачу нову покупку нового продукту
addUser(user_code = 'AA-444-1', country_name = 'France', money = '2222.22 usd')

#Додати існуючому користувачу нову покупку існуючого продукту
addUser(user_code = 'AA-444-1', country_name = 'Ukraine' , money = '2222.22 usd')

print(dataset)
input()

print("\n\n")