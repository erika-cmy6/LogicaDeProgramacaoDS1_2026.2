"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:

desconto = lambda valor: valor * 0.85

# Exemplo de utilização
preco_final = desconto(100)
print(f"Preço com desconto: R$ {preco_final:.2f}")
