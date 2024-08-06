# Escreva um programa que receba um vetor V de N números inteiros (N será lido), determine e exiba o maior e o menor elemento deste vetor e seus respectivos índices. Obs: suponha a inexistência de valores repetidos.
V=[]
N=int(input(""))
maior=menor=n1=int(input(""))
V.append(n1)
for i in range(N-1):
    num=int(input(""))
    V.append(num)
    if num>maior:
        maior=num
    elif num<menor:
        menor=num
for i in range(N):
    if V[i]==maior:
        print(f"Maior Número, Índice: {maior}, {i}")
    if V[i]==menor:
        print(f"Menor Número, Índice: {menor}, {i}")
'''
TENTATIVA DE COLOCAR NUMEROS ALEATORIOS QUE NAO SE REPITAM
import random
numeros=list(range(1,20,2)) # GERAR O VETOR
random.shuffle(numeros) # EMBARALHAR
'''
