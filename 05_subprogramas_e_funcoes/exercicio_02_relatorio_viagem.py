"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:


def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    litros = distancia_km / consumo_kml
    custo = litros * preco_combustivel
    return custo


def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    custo = qtd_pessoas * dias * diaria_alimentacao
    return custo


# Programa principal
distancia = float(input("Distância da viagem em km: "))
consumo = float(input("Consumo do veículo em km/l: "))
preco = float(input("Preço do combustível: "))

pessoas = int(input("Quantidade de pessoas: "))
dias = int(input("Quantidade de dias: "))
diaria = float(input("Custo diário de alimentação por pessoa: "))

transporte = calcular_custo_transporte(distancia, consumo, preco)
alimentacao = calcular_custo_alimentacao(pessoas, dias, diaria)

total = transporte + alimentacao

print(f"Custo do transporte: R$ {transporte:.2f}")
print(f"Custo da alimentação: R$ {alimentacao:.2f}")
print(f"Custo total da viagem: R$ {total:.2f}")
