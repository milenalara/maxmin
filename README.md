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

### Análise da complexidade assintótica pela aplicação do Teorema Mestre

## Documentação e links úteis

## Licença
Este projeto está licenciado sob a Licença MIT.