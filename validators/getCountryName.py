import re

def getCountryName():
    user_input = input('getCountryName: ')

    if (re.search(r"/w+", user_input) ):
        return user_input
    else:
        return False