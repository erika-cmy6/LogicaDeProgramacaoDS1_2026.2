"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:

def calcularpreco_final (preco_base, taxa_comdesconto,taxa_imp):
    resultado= preco_base *(1-taxa_comdesconto)*(1+ taxa_imp)
    return resultado

preco = float(input("digite o preço"))
txa1 = float(input("dessconto"))
txa2 = float(input("digite o preço"))
resultado1= calcularpreco_final(preco, txa1, txa2)
print(resultado1)