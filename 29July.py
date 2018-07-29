
#%%
has_cnic = True
name_in_voter_list = True

if has_cnic:
    if name_in_voter_list:
        print("You can vote.")
    else:
        print("Go home.")
else:
    print("Go home.")

#%%
# weight = eval(input("Enter your weight: "))
# print(type(weight))

#%%
cities = ["Atlanta","London"]
print(f"Welcome to {cities[0]}")
print("London" in cities)

#%%
numbers = list(range(1,10))
print(numbers)

even_numbers = list(range(0,15,2))
print(even_numbers)

#%%
cities.insert(8,"Karachi")
print(cities)
print(len(cities))
cities.index("Karachi")
print(cities)

#concatinate 2 lists
cities = cities + ["Lahore", "Islamabad", "Peshawar"]
print(cities)

#slicing lists
print(cities[2:])
print(cities[2:4])
print(cities[-1:])
print(cities[-4:-2])

#remove from list
del cities[3]
print(cities)
cities.remove("Islamabad")
print(cities)

