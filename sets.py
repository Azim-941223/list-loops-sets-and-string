# problem_0
dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
dates_of_birth.remove(6)
print(dates_of_birth)

# problem_1
dates = {1,2,3}
numb = {4,5,6}
nu = {7,8,9}
dates.union(numb,nu)
print(dates)

# problem_2
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_2 ^ farm_1)
a = farm_1.difference(farm_2)
print(a)

# problem_3
exemple = {"cow", "horse", "donkey", "cat", "dog"}
exemple.add("elephent")
print(exemple)
exemple.pop()
print(exemple)

# problem_000
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu.update({'besh_barmak': 130})
menu.update({'lagman': 135})
menu.pop('borsh')
print(menu)

# problem_10
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu.update({'drinks': ['Coca-cola','Sprite','Fanta']})
print(menu)

# problem_31
name = {}
for i in range(3):
    user = input("Enter name: ")
    password = int(input("Enter password:"))
    name.update({user:password})
print(name)

# problem_27
a_dict = {"Azamat":"Manager", "Leila": "Teacher", "Kevin": "Programmer", "David": "Policeman", "Honor": "Fighter"}
for key in a_dict:
    print("Hi",key, "Good prodession", a_dict[key])