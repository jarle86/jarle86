#creating and manipuling dictionarys
customer = {
    'name':'Jose',
    'lastname': 'Padilla',
    'age': 25}

#validating variable type
print(type(customer))

#printing the dictionary keys
print(customer.keys())

#validating if a key is in the dict
print("name" in customer.keys())

#adding new key
customer['phone'] = '123 456 7890'
print(customer)

#removing key
customer.pop("age")
print(customer)
