# Seleção Simultânea doMaior e do Menor Elementos (MaxMin Select)

Este é um trabalho desenvolvido para a disciplina de Fundamentos de Projeto e Análise de Algoritmos, ministrada pelo professor João Paulo Aramuni em 2025/1 no bacharelado em Engenharia de Software da PUC Minas.

Consiste na implementação em Python de um algoritmo de seleção simultânea do maior e do menor elementos (MaxMin Select) de uma sequência de números, utilizando a abordagem de divisão e conquista.

O arquivo `main.py` contém o código com a implementação.

## Como rodar o projeto
Abra o diretório contem o arquivo no seu terminal de linha de comando e execute `python main.py` ou `python3 main.py` (à depender da versão do Python instalada na sua máquina).

## Explicação das funções

A função `maxMinSelect(numbers)` recebe como parâmetro um array de números e retorna um array de dois elementos, no formato [max, min]: o elemento no index 0 é o maior número e o elemento no index 1 é o menor número.

O algoritmo utiliza como estratégia a recursividade para dividir repetidamente o array original em dois subconjuntos de tamanho igual, até chegar na condição de parada, que é quando o array tem tamanho 1, ou seja, um único elemento. Ao chegar na condição de parada, as chamadas recursivas retornam fazendo uma comparação entre o maior elemento de cada subgrupo. 

No fim, o maior número e o menor do array passado inicialmente são retornados.

## Saída da Execução

```
Numbers: [1, 2, 3, 4, 5]
        Max:5
        Min:1
Numbers: [5, 4, 3, 2, 1]
        Max:5
        Min:1
Numbers: [22, 31, 0, 4, 55]
        Max:55
        Min:0
Numbers: [22, 31, -55, 0, 4, 55]
        Max:55
        Min:-55
```

## Relatório técnico

### Análise da complexidade assintótica pelo método de contagem de operações

1) Número de chamadas recursivas
Consideraremos aqui *n* o número de elementos do array de input (`len(numbers)`). A cada chamada de recursão, o algoritmo realiza duas chamadas recursivas para cada valor de n.

O número total de chamadas é proporcional ao número de nós dessa árvore, que cresce
exponencialmente com n.

O Total de chamadas recursivas: *2<sup>n</sup>*

2) Operações por chamada
Cada chamada realiza:
- uma divisão para encontrar o elemento no meio do array (1)
- duas comparações para encontrar o máximo e o mínimo (2)

Temos então um número fixo de 3 operações por chamada.

3) Total de operações

O total de operações é proporcional ao número de chamadas recursivas * o número de operações por chamada. Portanto: 3 * 2<sup>n</sup>

Usando a notação Big O, temos que a complexidade assintótica é O(2<sup>n</sup>).

### Análise da complexidade assintótica pela aplicação do Teorema Mestre

A fórmula do Teorema Mestre é 

T(n) = a * T(n/b) + f(n)

Em que:
- a = o número de subproblemas gerados na recorrência,
- b = o fator pelo qual o tamanho do problema é reduzido em cada nível da recursão
- f(n) = o custo do trabalho feito fora das chamadas recursivas

Assim, temos que a nossa fórmula é:

T(n) = 2T(n/2) + O(1)

p = log<sub>b</sub>a
p = log<sub>2</sub> = 1

Neste caso, como o custo da recursão domina, temos o caso 1:

T(n) = Θ(n<sup>log<sub>b</sub>a</sup>)

Ou seja:

T(n) = Θ(n<sup>1</sup>) = Θ(n)

## Documentação e links úteis
Progressão Geométrica: https://www.todamateria.com.br/progressao-geometrica/ 
Teorema MEstre: https://pt.wikipedia.org/wiki/Teorema_mestre_(an%C3%A1lise_de_algoritmos)

## Licença
Este projeto está licenciado sob a Licença MIT.