"""
EXERCÍCIO 03: Gerador de Alertas da Cagece
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Desenvolva um procedimento `emitir_alerta_fatura(nome_cliente, valor, data_vencimento)`
que imprima a mensagem:
"Prezado(a) [nome], sua fatura da Cagece no valor de R$ [valor] vence no dia [data]."
"""

# TODO: Desenvolva o procedimento abaixo:


def emitir_alerta_fatura(nome_cliente, valor, data_vencimento):
    print(f"Prezado(a) {nome_cliente}, sua fatura da Cagece no valor de R$ {valor:.2f} vence no dia {data_vencimento}.")

# Chamando o procedimento
emitir_alerta_fatura("Maria", 125.50, "20/10/2026")
