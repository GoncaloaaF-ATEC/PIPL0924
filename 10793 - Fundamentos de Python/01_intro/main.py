"""
tipos de dados
var
op?
in/out

if - elif - else

match -case ? <- py 3.10

while?
for?


"""
from unittest import case

"""
tipos de dados?

bool
int
str
flaot
    double
char


var
op?

int + int -> int
int - int -> int
int * int -> int
int / int -> float

 // -> div int

 % -> Mod (resto)

 str * int




"""

print(10//3)
print(10 // 3.0)
nome: str = "valor"
print(nome)

nome = 12

print(nome)


print(" nome " * 5)



print(" nome " + " str 2 ")

nome = "Gonçalo"
ano = 2025

print("Ola " + nome + " no ano de " + str(ano))
print("Ola" , nome , "no ano de" , ano)

print(f"Ola {nome} no ano de {ano}")

print("Ola {} no ano de {}".format(nome, ano)) # Evitar, não e boa pratica usa f""


# pedir ao usr um nome?
nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Adulto")
elif idade >= 12:
    print("Teenager")
else:
    print("Menor")


## faça uma app que recebe um num e diga o mes correspondente
# 1 - Jan
# 2 - Fev
# ....
# 12 - Dez
# outro valor - Mes invalido


mes = input("Digite seu mes: ")

"""
if mes == "1":
    print("Jan")
elif mes == "2":
    print("Feb")
elif mes == "3":
    print("Mar")
elif mes == "4":
    print("Apr")
elif mes == "5":
    print("May")
elif mes == "12":
    print("Dez")
else:
    print("mes invalido")
"""


match mes:
    case "1":
        print("Jan")
    case "2":
        print("Feb")
    case "3":
        print("Mar")
    case "4":
        print("Apr")
    case "5":
        print("May")
    case "12":
        print("Dez")
    case _:
        print("mes invalido")



## faça uma app que recebe um num e diga o dia da semana  correspondente
# 1 - dom
# 2 - seg
# ....
# 6 - sabado
# outro valor - dia invalido


print("--"*3,"loops", "--"*3)

num = 10
while num >= 0:
    print(num)
    num -= 1



"""

faça um programa que peça ao utilzador números ate inseri um valor negativo.

conte os valores inseridos 
calcule a media dos valores inseridos 

"""

"""
a += 5 # <- a = a + 5
a -= 5 # <- a = a - 5
a *= 5 # <- a = a * 5
a /= 5 # <- a = a / 5

"""

numVal = 0
soma = 0

while True:
    num = int(input("Digite um valor: "))

    if num < 0:
        break

    numVal += 1
    soma += num


print(f"inseriu {numVal} valores")
avg = soma / numVal

print(f"a media dos valore é: {avg}")


# range(5) -> 0, 1, 2, 3, 4         ->  range(n) -> todos os num int de 0 a n-1
# range(5, 10) -> 5, 6, 7, 8, 9     ->  range(m, n) -> todos os num int de m a n-1
# range(4, 11, 2) -> 4, 6, 8,  10   ->  range(m, n, s) -> todos os num int de m a n-1 com um step de s

range(4)    # 0 1 2 3
range(0, 4) # 0 1 2 3

range(4, 8) # 4, 5, 6, 7

range(12, 18, 2) # 12, 14, 16

print("--"*3,"for loops", "--"*3)

for i in range(4):
    print(i)

for i in range(4, 20, 2):
    print(i, end=" ")

print("")



"""
Nome: 
Turma:
Trabalho:
"""