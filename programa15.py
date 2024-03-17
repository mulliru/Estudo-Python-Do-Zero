#Exercicio

'''
Faça um programa que recebe a altura e o peso do usuario
e calcule o seu IMC utilizando a formula abaixo
'''

peso = float(input("Informe o seu peso:"))
altura = float(input("Informe a sua altura:"))

IMC = peso / (altura**2)
print(f"Seu IMC é de {IMC:.2f}")  #dessa forma ele deixa só duas casas decimais