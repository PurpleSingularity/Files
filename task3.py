
from data import dataset
from task1 import *

#   Написати рекурсивну функцію, що повертає інформацію: хто і скільки грошей витратив на свої покупки.
#   Рекурсивно необхідно пройтись по користувачам та спискам їх товарів.


#product_list - словник з dataset, що зберігає товар та список його покупок (цін)
def recursionByProducts(user_code, country_list, amount_of_money = 0):
    #TODO

    if country_list==[]:
        return amount_of_money

    current_country_list = dataset[user_code][country_list[0]]
    amount_of_money = sum(current_country_list)

    return recursionByProducts(user_code,country_list[1:],amount_of_money)


def recursionByUsers(user_codes = list(dataset.keys()), result_dict = dict()):
    #TODO
    if user_codes == []:
        return result_dict
    user_code = user_codes[0]
    country_list = list (dataset[user_code].keys())
    money = recursionByProducts(user_code, country_list)

    result_dict[user_code] = money

    return recursionByUsers(user_codes[1:], result_dict)


print("Task 3")
result = recursionByUsers()
print(result)

print("\n\n")



