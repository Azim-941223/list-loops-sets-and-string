# problem_31
words= "Google создаст специальную команду для поиска багов в особо важных приложениях."
count = words.count("")
print(count)

# problem_25
word_s = "У вас есть строка 'Запуск Ethereum 2.0 состоится 1 декабря. На депозитный контракт внесено более 524 288 ETH'"
y = word_s.split()
for i in y:
    print(i,type(i))


# problem_11
w = 'хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
print(w.title())

# problem_2
txt = "GitHub"
simbol = input("Введите символ: ")
a = txt.join("")
print(a())

# problem_5
txt = "Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем"
print(txt)
b = txt.replace("е", "3")
print(b)

# problem_0
a = "Какое то предложение для того что бы сделать задание по Python"
slen= len(a)
lowerCaseStr = a.lower()
upperCaseStr = a.upper()
cutlen = slen - (slen//2)
printStr = lowerCaseStr[:cutlen] + upperCaseStr[cutlen:]
print(printStr)

# problem_1
a = (17*3) < (12*5)
b = str(a)
print(b)

