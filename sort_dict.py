person= [
    {'name':'da', 'house':'eth'},
    {'name':'ba', 'house':'tig'},
    {'name':'ca', 'house':'usa'},
    {'name':'aa', 'house':'canada'}

]

print(person[0]['name']) #  output da
# print(person.sort()) # TypeError: '<' not supported between instances of 'dict' and 'dict'

#function return name
def f(p):
    return p['name']

person.sort(key=f)
print(person)
# using lambda function
person.sort(key = lambda x:x['name']) 
print('out of lambda : ', person)