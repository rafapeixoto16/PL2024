# TPC4 : Máquina de Vendin

## Enunciado

Pediram-te para construir um programa que simule uma máquina de vending.
A máquina tem um stock de produtos: uma lista de triplos, nome do produto, quantidade e preço.
stock = [
 {"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
 ...
]
Podes persistir essa lista num ficheiro em JSON que é carregado no arranque do programa e é atulizado
quando o programa termina.
A seguir apresenta-se um exemplo de uma interação com a máquina, assim que esta é ligada, para que possas perceber o tipo de comandos que a máquina aceita:
>>maq: 2024-03-08, Stock carregado, Estado atualizado.
>>maq: Bom dia. Estou disponível para atender o seu pedido.
>> LISTAR
maq:
cod | nome | quantidade |  preço
A23 água 0.5L 8 0.7
...
>> MOEDA 1e, 20c, 5c, 5c .
maq: Saldo = 1e30c
>> SELECIONAR A23
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Saldo = 60c
>> SELECIONAR A23
maq: Saldo insufuciente para satisfazer o seu pedido
maq: Saldo = 60c; Pedido = 70c
>> ...
...
maq: Saldo = 74c
>> SAIR
maq: Pode retirar o troco: 1x 50c, 1x 20c e 2x 2c.
maq: Até à próxima

Use a imaginação e criatividade e tente contemplar todos os cenários, por exemplo, produto inexistente ou
stock vazio. Como extra pode adicionar um comando para adicionar alguns produtos ao stock existente
(produtos novos ou já existentes)

## Autor

- A96807
- Rafael Conde Peixoto

## Solução obtida 

Para este tpc utilizei as bibliotecas json e ply. A biblioteca *json* foi utilizada para carregar e guardar o estado dos itens (produtos). 
Primeiramente dou *load* dos itens de um ficheiro *json*. Para isso verifico se cada item tem pelo menos estes campos:

- cod: código que identifica o produto
- nome: nome do produto
- quant: quantidade disponível do produto
- preco: preço do produto

Caso algum dos itens não possua um dos campos ele não vai ser utilizado.

Para a gestão dos itens estou a usar ply para guardar as variveis (lista de produtos, dinheiro atual e estado do programa).
Neste programa temos as seguintes funcionalidades implementadas:

- Selecionar (ID produto)
- Listar
- Moeda (moedas: 5c 2e …)
- Saldo 
- Stock (ID produto) (quantidade)
- Sair

O comando moeda não esta a verificar se a moedas inseridas são validas, isto é, como esta agora é possível adicionar moedas de 7€ por exemplo. Para isto era apenas necessário verificar se a moeda pertence a uma lista. Já no troco estou a retornar as moedas de forma correta. 

O comando *stock* serve para reabastecer produtos que já existam. 
O resto dos comando funcionam com foi estabelecido no enunciado

