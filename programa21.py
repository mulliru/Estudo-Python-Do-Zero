# Exercicio Media

'''
faça um programa que recebe duas notas de 1 aluno
e diga se ele foi aprovado ou não
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
