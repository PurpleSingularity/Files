import re

user_input = input()
flo = float(re.match(r"(\d{1,4}\.\d{1,2})", user_input))
print(flo)
input()