"""
EXERCÍCIO 03: Conta do Nagoya Sushi House
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie um programa que:
1. Leia o valor total consumido no restaurante (em R$).
2. Aplique a taxa de 10% de serviço do garçom.
3. Exiba o valor final da conta a pagar com mensagem formatada.
"""

# TODO: Desenvolva o algoritmo abaixo:
total_consumido= float(input("consumo do restaurate"))
servico_garcon= total_consumido = 16.40
total_apagar = total_consumido + servico_garcon
print(f"o total a ser pago e R${total_apagar:.2f}")


