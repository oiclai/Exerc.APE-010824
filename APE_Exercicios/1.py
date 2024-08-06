# Escreva um programa que leia um vetor A de N números inteiros (N será lido) e um outro inteiro K, construa e exiba um outro vetor B cujos elementos são os respectivos elementos de a multiplicados por K. Ex: A = [1,2,3], K = 5, B = [5,10,15].

N=int(input("Quantidade de elementos no Vetor A: "))
A=[]
for i in range(N):
    elemA=int(input(f"Elemento ({i+1}) do Vetor: "))
    A.append(elemA)
K=int(input("Elementos do vetor A serão multiplicados por: "))
B=[]
for elemA in A:
    elemB=(elemA)*K
    B.append(elemB)
print(A)
print(f"K = {K}, {B}")