# Design-Patterns-Python

Exercicios, exemplos e testes com padrões de projetos em Python.

Este material servirá de referência para consultas futuras e/ou dúvidas.
Os exemplos são baseados na trilha do curso disponível no site da Alura.

##Cenário

No exemplo existe uma classe chamada orçamento.py, está classe recebe o valor do orçamento.

A classe calculador_de_impostos.py é utilizada para calcular o imposto em cima do valor do orçamento. Sendo que
há a possibilidade de existir vários impostos.

Como criar uma estratégia para calcular o valor do orçamento para cada tipo de imposto que existe e poderá vir a existir.


O código importa um módulo com os vários impostos, mas toda vez que um imposto for adicionado deverá ser alterado o código da calculadora.

##Solução

Aplicar o padrão Strategy.