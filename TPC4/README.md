# TPC4 : Analisador léxico

## Enunciado

Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:
- 'Select id, nome, salario From empregados Where salario >= 820'

## Autor

- A96807
- Rafael Conde Peixoto

## Solução obtida 

Começei por analisar os exemplos presentes no ["github dadeaz-ply"](https://github.com/dabeaz/ply/tree/master/example/BASIC) e parti dai cheguei a 10 tokens:

- PR : palavras reservadas
- Name : campos
- OP : operações
- PV : ;
- ALL : *
- COMMA : ,
- INT : inteiros
- FLOAT : float
- NL : nova linha
- LPAREN : \(
- RPAREN : \)

Para terminar faltava apenas definir o regex de cada token. 