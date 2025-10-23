lst = ["Gonçalo", 2004, "ActionScript", True] # lista
# arr = ["Aluno 1", "Aluno 2", "Aluno 3", "Aluno 4"] # lista


print(lst)
print(lst[0])
nome = lst[0]
# print(lst[12]) # -> IndexError: list index out of range

lst.append(123) # add sempre no final
print(lst)

print(lst.insert(1, 9999))
print(lst)


lst.remove(9999) ## removem por valor
print(lst)

lst.pop() # removem por index -> de vazio -> removem o ultimo
print(lst)


idx2 = lst.pop(2) # removem por index
print(idx2)
print(lst)


print(lst.insert(1, 9999))


"""
Criar lst
ler elm lst
add elm no fim
add elm no meio 
remove elm pelo valor
remove elm pelo idx no fim
remove elm pelo idx no meio
velocidade insert vs append

"""


print(len(lst))
print(lst.__len__())


print("--"*5)

lst2 = [1,2,3,3,3,4,1,2,3]

print(lst2.count(1))
print(lst2.count(3))
print(lst2.count(4))
print(lst2.count(99))

print("--"*5)


## count vs len



print(2 in lst2) # in verifica se o val a esq esta na coll a direita
print(99 in lst2)


lst2.extend([99,999,999, 9999])
print(lst2)

print("--"*5)
lst3 = lst2

print(lst2[0])
print(lst3[0])


lst3[0] = 12

print(lst3[0]) # 12
print(lst2[0]) # 12


print("--"*5)

print(lst2)

lst2.sort()
print(lst2)

lst2.sort(reverse=True)
print(lst2)


lst2.insert(1,123)
print(lst2)

lst2.insert(0,123)
print(lst2)

lst2.remove(123) ## remove a 1 vez que o valor aparece
print(lst2)


print(lst2.index(123))
lst2.insert(0,4)

print(lst2.index(4, 5, 8))