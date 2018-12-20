import re

def getUserPasCode():

    user_input = input('getUserPasCode: ')

    if (re.match(r"(\W{2}),(-),(\d{3}),(-),(\d{1})", user_input) ):
        return user_input
    else:
        return False