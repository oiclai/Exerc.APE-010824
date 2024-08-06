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
