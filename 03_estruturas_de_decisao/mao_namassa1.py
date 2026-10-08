# TODO: implemente a expressao de validação 
media_aluno = 7.5
frequencia_percentual = 80

media_aluno = float(input("media do aluno"))
frequencia_porcentual = int(input("frequencia do aluno"))
media_final = media_aluno >= 6
frequencia_final = frequencia_porcentual >= 75 
resultado = media_final and frequencia_final
print("o alune foi aprovado?",resultado)