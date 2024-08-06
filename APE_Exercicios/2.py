# Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.

V=[]
qtdK=0
for i in range(30):
    elemV=int(input(f"Elemento ({i+1}) do Vetor: "))
    V.append(elemV)
K=int(input("Procura do elemento: "))
for elemV in V:
      if elemV==K:
           qtdK+=1
print(qtdK)

# outra alternativa:
''' 
import random 
numeros=[0]*30
qtdK=0
for i in range(len(numeros)): 
    numeros[i]=random.randit(1,100) # numero aleatorio entre 1 a 100 (incluindo ambos)
k=int(input("Chute: "))
for i in range(len(numeros)):
    if (numeros[i])==k:
        qtdk+=1
print(numeros)
print(qtdk)
'''
