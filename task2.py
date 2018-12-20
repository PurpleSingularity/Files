from data import dataset
import re

#    Створити пакет validators та написати функції, що валідують усі дані. Імпорутвати дані функції.

from validators.lib import getUserPasCode
from validators.lib import getCountryName
from validators.lib import getMoney


from task1 import addUser


#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник.
#   Усі дані вводить користувач. Використати валідатори. Викликати функцію

def addUserValidator():
    #TODO
    user_code = getUserPasCode()
    while not user_code:
    	user_code = getUserPasCode()

    country_name = getCountryName()
    while not country_name:
    	country_name = getCountryName()

    money = getMoney()
    while not money:
    	money = getMoney()
    flo = re.search(r"(\d{1,4}\.\d{1,2})", money)
    money = float(flo.group(1))
    addUser(user_code, country_name, money)



print("Task 2")
addUserValidator()
print(dataset)
input()


print("\n\n")