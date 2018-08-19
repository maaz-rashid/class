costomer = {
    "first_name" : "David",
    "last_name" : "Muller",
    "salary" : 600
}

for x in costomer.keys():
    print(f"{x} : {costomer[x]}")


some_numbers = {'n1':[2,3,1], 'n2':[5,1,2],'n3':[3,2,4]}
for key in some_numbers.keys():
    some_numbers[key] = sorted(some_numbers[key])
print(some_numbers)


{x:sorted(some_numbers[x]) for x in some_numbers.keys()}

{k:sorted(v) for (k,v) in some_numbers.items()}

inventory = {
    'gold' : 500,
    'pouch' : ['flint','twine','gemstone','hagger'],
    'backpack' : ['xylo', 'dagger','bedroll','bread']
}

if inventory['pouch']:
    [print(x) for x in inventory['pouch'] if x!='hagger']

{ print(y) for x in inventory.keys() if x == 'pouch'  for y in inventory[x] if y!='hagger' }

user_programming_languages = {
    "osama" : ["C","C#","Python"],
    "amir saleem":['html','css','excel']
}
if user_programming_languages['amir saleem']:
    [print(x) for x in user_programming_languages['amir saleem']]

{ print(y) for x in user_programming_languages.keys() if x == 'amir saleem'  for y in user_programming_languages[x] }

