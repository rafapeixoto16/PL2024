import datetime
import re
import ply.lex as lex
import json


def carregaJson():
    file = open("stock.json", "r", encoding="utf-8").read()

    dics = json.loads(file)

    return dics


def saveJson(lista):
    string = {
        "stock": lista
    }

    file = open("stock.json", "w", encoding="utf-8")
    json.dump(string,file, indent=4)
    file.close()


tokens = ['LISTAR', 'MOEDA', 'SALDO', 'SELECIONAR', 'TROCO', 'SAIR','STOCK']


def t_LISTAR(t):
    r"(?i)Listar"
    print("|\tcod\t|nome|\tquantidade|\tpreço"
          "---------------------------------")

    stock = t.lexer.itens
    for item in stock:
        print("\t " + item["cod"] + "\t | " + item["nome"] + "\t |" + str(item["quant"]) + "\t |" + str(
            item["preco"]) + " €")


def t_SELECIONAR(t):
    r"(?i)selecionar\s+(A\d+)"
    for itemCod in re.finditer("(A\d+)", t.value):
        for i in range(len(t.lexer.itens)):
            if t.lexer.itens[i]["cod"] == itemCod.group():
                if t.lexer.itens[i]["quant"] <= 0:
                    print("maq: De momento o item encontra-se sem stock")
                else:
                    custo = t.lexer.itens[i]["preco"]
                    custo = custo * 100
                    if t.lexer.money - custo >= 0:
                        t.lexer.itens[i]["quant"] -= 1
                        t.lexer.money -= custo
                    else:
                        print("maq: Insira moedas para comprar o item")


def t_STOCK(t):
    r"(?i)stock\s+(A\d+)\s+(\d+)"
    itemCod = re.findall("(A\d+)",t.value)
    quantity = re.findall("(\s+\d+)", t.value)

    encontrei = False
    for i in range(len(t.lexer.itens)):
        if t.lexer.itens[i]["cod"] == itemCod[0]:
            encontrei = True
            t.lexer.itens[i]["quant"]+= int(quantity[0])
            quantityStocked = t.lexer.itens[i]["quant"]
            print(f"maq: Stock item {itemCod[0]} abastecido {quantityStocked}")
    if not encontrei:
        print("maq: Um item com esse codigo não existe")


def t_MOEDA(t):
    r"(?i)moeda\s+(\d[c|e|E|C],?.?\s*)+"
    for moeda in re.finditer(r"(\d+)([c|e])", t.value, re.I):
        if "e" in moeda.group(2).lower():
            euro = int(moeda.group(1))
            euro *= 100
            t.lexer.money += euro
        else:
            centimos = int(moeda.group(1))
            t.lexer.money += centimos


def t_SALDO(t):
    r"(?i)SALDO"
    euros = t.lexer.money // 100
    centimos = t.lexer.money % 100
    print("maq: "+str(euros) + "€ e " + str(centimos) + " centimos")


def t_TROCO(t):
    r"(?i)troco"
    moeda2e = t.lexer.money // 200
    t.lexer.money -= (moeda2e*200)
    moeda1e = t.lexer.money // 100
    t.lexer.money -=(moeda1e *100)
    moeda50c = t.lexer.money // 50
    t.lexer.money -= (moeda50c *50)
    moeda20c = t.lexer.money // 20
    t.lexer.money -= (moeda20c *20)
    moeda10c = t.lexer.money // 10
    t.lexer.money -= (moeda10c*10)
    moeda5c = t.lexer.money // 5
    t.lexer.money -= (moeda5c*5)
    moeda2c = t.lexer.money // 2
    t.lexer.money -= (moeda2c*2)
    moeda1c = t.lexer.money // 1
    t.lexer.money -= (moeda1c)

    print(f"maq: Troco em moedas:\n 2€-{moeda2e},\n 1€-{moeda1e},\n 0.50€-{moeda50c},\n 0.20€-{moeda20c},"
          f"\n 0.10€-{moeda10c},\n 0.05€-{moeda5c},\n 0.02€-{moeda2c},\n 0.01€-{moeda1c}")


def validaDic(dics):
    dicValido = []

    for item in dics["stock"]:
        if "cod" in item.keys() and "nome" in item.keys() and "quant" in item and "preco" in item:
            dicValido.append(item)

    return dicValido


def t_SAIR(t):
    r"(?i)sair"
    saveJson(t.lexer.itens)
    t.lexer.stop = 0


def t_error(t):
    # print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)


t_ignore = '\t '

lexer = lex.lex()
lexer.stop = 1
lexer.money = 0

lexer.itens = carregaJson()
lexer.itens = validaDic(lexer.itens)

print("maq: " + str(
    datetime.datetime.now().date()) + ", Stock carregado, Estado atualizado.\n"
                                      "maq: Bom dia. Estou disponível para atender o seu pedido.")
print()
while lexer.stop:
    string = input()
    lexer.input(string)
    for tok in lexer:
        print(tok.type, tok.value, tok.lineno, tok.lexpos)
