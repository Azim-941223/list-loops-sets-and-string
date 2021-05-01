# problem_12
lst = [('a', 1.2), ('b', 5), ('z', True), (5, False), (6, 'a')]
print(lst)



# problem_32
names = ('Azamat', 'Bektur', 'Arstan')
print(names[1])
print(names[2])
print(names[0])

# problem_11
data = []
data.append("Azamat")
data.append(1.5)
data.append(True)
data.append(5)
data.append(10000)
print(data)

# problem_0
name = ["Adam", "Azamat", "Nurlan", "Howard", "Donald"]
print(name)
x = " ".join(name)
print(x)

# problem_12
tuples = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print(tuples[0:3])
print(tuples[3:6])
print(tuples[6:9])
print(tuples[9:12])
print(tuples[12:15])

# problem_17
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
x = names.count("Jack")
print(x)


# problem_72
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
i = 1
for i in range(10):
    if i % 2 == 0:
        i += 1
        print(names.pop(i), end=" ")

        

# problem_1
a = []
for i in range(1):
    b = input("Enter your name: ")
    a.append(b)
    c = input("Enter your year of birth: ")
    a.append(c)
    d = input("Enter your favorite progremm. lan: ")
    a.append(d)
print(a)


