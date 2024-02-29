# TPC3 : Somador on/off


## Enunciado

Somador on/off: criar o programa em Python
Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

## Autor

- A96807
- Rafael Conde Peixoto

## Solução obtida 

Neste trabalho usei a função re.finditer com o *pattern* r"(on|off|=|-?\d+)" e com a flag re.I com o intuito de todas as combinações entre maiúsculas e minúsculas serem levadas em questão. Depois para cada um dos casos vai acontecer algo diferente.
O caso do *on* vai por a *flag* ***ativo*** a verdadeiro, *off* a falso. Se for um dígito ou mais vai incrementar uma variável *somatorio* e o *=* vai dar print a variável *somatorio*.
