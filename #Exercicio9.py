#Exercicio9
peso_ideal = 0
Sexo= input("Digite seu sexo sendo m ou f ")
altura=float(input("Digite sua altura "))

if Sexo == 'm':
    peso_ideal = (72.7 * altura)-58
else:
    peso_ideal = (62.1*altura)-44.7
print(peso_ideal)