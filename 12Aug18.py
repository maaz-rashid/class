for item in range(2,11):
    for num in range(1,11):
        print(f"{item}x{num}={item*num}")
    print("-"*10)

[print(f"{a}x{j}={a*j}") for a in range(2,11) for j in range(1,11)]

if 2 in [1,2,3,4,5]:
    print("exists")
else:
    print("doesn't exists")

customer_29876 = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}
for vals in customer_29876.values():
    print(vals)
    
# for item in customer_29876.items():
#     print(item.)
#     print(item.v)

new_dict = {1:1,2:2,3:3,1:2}
for vals in new_dict.values():
    print(vals)

new_dict[4] = 4
for vals in new_dict.values():
    print(vals)


values = {1:1,2:2,3:3,4:4,5:5}

# for (k,v) in values:
#     print(k)
#     print(v)

{x:x**2 for x in range(10)}

#  dict1 = dict([(2,[2:3,3:4]),(3,[1,2,3,4,5]),(4,"string")])

aTupple = (2,3,4,5,["nasir","husain"])
aTupple[-1][1] = "maaz"
print(aTupple)