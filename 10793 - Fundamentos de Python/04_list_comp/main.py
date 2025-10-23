"""
var
tipos de dados
op com var
in/out

condições
    if
    match-case

range

loops
    for
    while

func

listas
    criar
    add fim
    add incio meio
    remover ultimo
    remover inicio meio
    aceder a um elem
    list slicing [1:10]
    ordenar listas


    list comp
    juntar duas listas

    iterar listas
        simples
        enumerate
        zip
"""

lst = [1,2,3,4,5,6,7,8,9, 10]


nova_lista = []


for i in lst:
    if i % 2 == 0:
        nova_lista.append(i)

print(nova_lista)


nova_lista2 = list(lst)
print(nova_lista2)


"""

nova_lista = [exp for item in lista]

"""
lst = [1,2,3,4,5,6,7,8,9, 10]

"""
for i in lst:
    if i % 2 == 0:
        nova_lista.append(i)

"""

nova_lista3 = [item for item in lst]


print(nova_lista3)


"""

nova_lista = [exp for item in lista if condição]

"""


nova_lista4 = [item * 2 for item in lst if item % 2 == 0]

print(nova_lista)
print(nova_lista4)


print("-------")

def dobro(x):
    return x * 2

nova_lista5 = [dobro(num) for num in lst if num % 2 == 0]


print(nova_lista5)
print("-------")
print(lst)

lst.extend(nova_lista5)

print(lst)

print("----itr listas ---")


for i in lst:
    print(i, end=" ")

print("")



print("----enumerate-----")
cidades = ["Lisboa","Porto","Coimbra", "Braga", "Faro",
           "Aveiro","Évora","Funchal","Viseu","Leiria"
]

for cidade in enumerate(cidades):
    print(f"idx {cidade[0]}: {cidade[1]}")

print("------")
for idx, cidade in enumerate(cidades):
    print(f"idx {idx}: {cidade}")


print("------")

t = ("nome", "Turma", "Nota")
a, b, c = t

print(c)

nova_var = 1,4,1

print(type(nova_var))

cidades = ["Lisboa","Porto","Coimbra", "Braga", "Faro",
           "Aveiro","Évora","Funchal","Viseu","Leiria"
]
populacoes = [
    545_000, 232_000, 143_000, 193_000, 67_000,
    78_000, 56_000, 106_000, 99_000, 129_000
]

for i in range(cidades.__len__()):
    print(cidades[i], populacoes[i])

print("----- zip -----")


for i in zip(cidades, populacoes):
    print(i)
print("----")


for cidade, pop in zip(cidades, populacoes):
    print(f"{cidade} tem {pop} habitantes")

print("---Listas len diferentes---")

cidades = ["Lisboa","Porto","Coimbra", "Braga", "Faro",
           "Aveiro","Évora","Funchal","Viseu","Leiria",
           "Sintra", "Almada"
]
populacoes = [
    545_000, 232_000, 143_000, 193_000, 67_000,
    78_000, 56_000, 106_000, 99_000, 129_000
]

"""
for i in range(cidades.__len__()):
    print(cidades[i], populacoes[i])

"""


for cidade, pop in zip(cidades, populacoes):
    print(f"{cidade} tem {pop} habitantes")


"""
Dict 
set

"""
