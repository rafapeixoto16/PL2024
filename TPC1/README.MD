# TPC1 : Análise de um dataset

1. Proibido usar o módulo CSV;
2. Ler o dataset, processá-lo e criar os seguintes resultados:
    - Lista ordenada alfabeticamente das modalidades desportivas;
    - Percentagens de atletas aptos e inaptos para a prática desportiva;
    - Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...   

## Autor

- A96807
- Rafael Conde Peixoto

### Solução adquirida 

Para a resolução deste optei por ler linha a linha do csv. Usei a função split (separar sempre que aparece uma virgula) para separar a string em uma lista.
Ja para a distribuição de atletas por escalão etário eu usei um dicionario, onde a chave é um inteiro (divisão inteira entre a idade de cada individuo e o intervalo de 5 anos).
Para a percentagens de atletas aptos e inaptos para a prática desportiva usei uma lista de tamanho 2 onde a posição 0 representa o numero de atletas atpos e a posição 1 o numero de atletas inaptos.
E para terminar usei um set com as modalidades desportivas.No fim do parsing do csv é ordenado alfabeticamente.
Todas estas estruturas são atualizadas a cada linha (menos o set se ja possuir as modalidade desportiva)