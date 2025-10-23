"""
S1
git - Bonus

tipos de dados

var
op var

if
switch-case

range
while
for

"""


"""
Hoje S2

funcs 

arrays e listas


"""

def ola_mundo():
    print("Ola Mundo")


ola_mundo()
ola_mundo()


def ola_mundo2(nome):
    print(f"Ola Mundo, {nome}")


ola_mundo2("Gonçalo")
ola_mundo2("Joao")



def ola_mundo3(nome, idade:int):
    print(F"Ola Mundo, {nome.upper()}, {idade}")


ola_mundo3("Carlos", 20)

def ola_mundo4(nome:str, idade:int):
    print(F"Ola Mundo, {nome}, {idade}")

ola_mundo4("Carlos", 20)


ola_mundo4(41, 20)

v = 10
print(v)
v = "Gonçalo"
print(v)
v = True

def ola_mundo5(nome:str, idade:int):
    return f"Ola Mundo, {nome}, {idade}"


msg = ola_mundo5("Carlos", 20)
msg2 = ola_mundo5("Joao", 20)

print("--"*10)
print(msg)
print("--"*10)
print(msg2)


def ola_mundo6(nome:str, idade:int) -> str:
    return f"Ola Mundo, {nome}, {idade}"


msg3 = ola_mundo6("Joao", 20)
print(msg3)



# Faça um Programa que leia três números e mostre o maior deles.
# var
# op com var
# condições

"""
v1
v2
v3


v1 > v2 and v1 > v3
v2 > v1 and v2 > v3
v3 > v2 and v3 > v1


"""


print("---"*5)
def ola_mundo7(nome:str, idade:int) -> str:
    return f"Ola Mundo, {nome}, {idade}"


msg3 = ola_mundo7(nome="Joao", idade=20)
print(msg3)


msg3 = ola_mundo7(idade=20, nome="Joao")
print(msg3)



print("---"*5)


def ola_mundo8(nome:str, idade:int = 18) -> str:
    return f"Ola Mundo, {nome}, {idade}"


msg3 = ola_mundo8(nome="Joao")
print(msg3)


msg3 = ola_mundo8("Joao")
print(msg3)


msg3 = ola_mundo8("Joao", 25)
print(msg3)

print("---"*5)
def ola_mundo9(nome:str="Sem nome", idade:int = 18) -> str:
    return f"Ola Mundo, {nome}, {idade}"


msg3 = ola_mundo9("Joao", 25)
print(msg3)


msg3 = ola_mundo9(idade=25)
print(msg3)


msg3 = ola_mundo9("Rita")
print(msg3)

msg3 = ola_mundo9(nome="Rita")
print(msg3)


print("---"*5)

x = 2
def demo():
    x = 10

demo()

print(x)


"""

:
    x = 10
    :
    print(x) -> 10
    x = 20
        :
        print(x) -> 20
    
    print(x) -> 20
    
print(x) -> 10
    
"""


print("---"*5)

def soma(a, b):
    return a + b


print(soma(1, 2))

print(soma(soma(1, 2), soma(1, 2)))