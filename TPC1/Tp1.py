import os
import sys

# std = sys.stdin
# sys.stdin = open("../emd.csv", "r", encoding="UTF-8")

file = open("./emd.csv", "r", encoding="UTF-8")

lixo = file.readline()

lista = [0, 0]
desportos = set()
nomePeople = []
idades = dict()
while line := file.readline():
    person = line.split(",")

    nome = f"{person[3]} {person[4]}"
    nomePeople.append(nome)

    if person[12] == "true\n" or person[12] == "true":
        lista[0] = lista[0] + 1

    else:
        lista[1] = lista[1] + 1

    desporto = person[8]
    desportos.add(desporto.lower())

    key = f"{int(person[5]) // 5}"

    if key in idades:
        atual = idades.get(key)
        atual = atual + 1

        idades.update({key: atual})

    else:
        idades.update({key: 1})

sorted(desportos, key=None, reverse=False)

soma = lista[0] + lista[1]

print(
    f"Percentagem de atletas aptos: {lista[0] / soma * 100}%. Percentagem de atletas inaptos: {lista[1] / soma * 100}")
lista_ordenada = sorted(list(desportos))

print("Lista de desportos:")
print(lista_ordenada)

print(idades)

for idade in idades.keys():
    idadeI = int(idade) * 5
    idadeF = idadeI + 4
    print(f"Entre a idade {idadeI} e {idadeF} existem {idades.get(idade)} atletas")
