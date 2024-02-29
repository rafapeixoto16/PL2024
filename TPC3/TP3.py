import re

ola = open("ficheiro","r",encoding="utf-8").read()

somatorio = 0
ativo = False

for elemento in re.finditer("(on|off|=|-?\d+)", ola, re.I):
    if elemento.group(1).lower() == "on":
        ativo = True

    if elemento.group(1).lower() == "off":
        ativo = False

    if elemento.group(0) == "=":
        print(somatorio)

    if elemento.group(1).isdigit() and ativo:
        somatorio += int(elemento.group(1))
