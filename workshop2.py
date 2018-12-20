"""
Дано структуру даних:
smth = [
{
"brand": "Ford",
"model": "Mustang",
"year": 1964
“owners”: {
“Bob”,
“Boba”
}
},
{
"brand": "Mers",
"model": "C500",
"year": 2000
“owners”: {
“Bob”,
}
},
{
"brand": "Wolksvagen",
"model": "Polo",
"year": 2002
“owners”: { }
}
]
1. Написати рекурсивну функцію, що виводить brand авто з найбільшою кількістю
власників.
def getBrand(smth):
#some magic
return brand
2. Написати функцію, що до авто з брендом brand додає нового власника з іменем
name
def addOwner(smth, name):
#some magic
3. Написати функцію, повертає множину усых власників усіх автомобілів.
def getNames(smth):
#some magic
return [.....]
"""



if __name__ == "__main__":
    def getBrand(smth):
    """
    This fucntion convert list ['brand', 'number of owners'] to 'brand'
    Args:
        smth - structure that is list of dictionaries
    Returns:
        Brand - String that is car brand
    Examples:
        >>> print(getBrand(smth))
        Ford
    """
    return Brand(smth)[0]

	def Brand(smth):
	"""
    This fucntion find the car brand with the biggest number of owners
    Args:
        smth - structure that is list of dictionaries that is car information
    Returns:
        a - 2 element list of 'car brand' and number of owners
    Examples:
        >>> print(Brand(smth))
        'Ford', 2
    """
	    if(len(smth)>1):
	        a = max_owners(convert(smth[0]),Brand(smth[1:]))
	    else:
	        return convert(smth[0])
	    return a
	
	def convert(car):
		"""
	    This fucntion convert dictionary to 2 element list of brand and number of owners
	    Args:
	        car - car information dictionary
	    Returns:
	        car - 2 element list
	    Examples:
	        >>> print(convert({
	      "brand":"Ford",
	      "model":"Mustang",
	      "year":1964,
	      'owners':{
	            "Mark",
	            "Boba"
	          }))
	        [Ford, 2]
	    """
	    return [car["brand"],len(car["owners"])]

	def max_owners(car1,car2):
		"""
	    This fucntion compare to list by comparing numbers of owners
	    Args:
	        car1, car2 - car lists
	    Returns:
	        carN - list that is bigger
	    Examples:
	        >>> print(max_owners([Ford, 2], [Mers,1]))
	        [Ford, 2]
	    """
	    if(car1[1]>car2[1]):
	        return car1
	    else:
	        return car2

	def addOwner(smth, name):
		"""
	    This add owner to target brand
	    Args:
	        smth - structure that is list of dictionaries
	        name - new owners name
	    Returns:
	        none
	    """
	    name1= {name}
	    brand= getBrand(smth)
	    for i in smth:
	        needed=str(i['brand'])
	        if needed==brand:
	            i['owners'].update(name1)

	def getNames(smth):
		"""
	    This fucntion convert structure to set of owners
	    Args:
	        smth - structure that is list of dictionaries
	    Returns:
	        names - set of owners
	    Examples:
	        >>> print(getNames(smth))
	        Bob, Mark, Boba
	    """
	    names=set()
	    for j in smth:
	        names.update(j['owners'])
	    return names
	"""
	smth = [
	    {
	      "brand":"Ford",
	      "model":"Mustang",
	      "year":1964,
	      'owners':{
	            "Mark",
	            "Boba"
	          }
	    },
	    {
	      "brand":"Mers",
	      "model":"C500",
	      "year":2000,
	      'owners':{
	            "Bob"
	          }
	    },
	    {  "brand":"Wolksvagen",
	      "model":"Polo",
	      "year":2002,
	      "owners":{}
	    }
	]
	"""