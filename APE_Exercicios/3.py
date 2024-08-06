# Escreva um programa que leia um vetor V contendo N elementos inteiros (N será lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver, informe em que posição (índice). Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K aparece.

V=[]
posicoes=[]
qtdK=0
N=int(input("Quantidade de elementos no vetor: "))
for i in range(N):
    elemV=int(input(f"Elemento ({i+1}) do vetor V: "))
    V.append(elemV)
K=int(input("A procura do número: "))
for i in range(N):
    if V[i]==K:
        qtdK+=1
        posicoes.append(i)
if qtdK==0:
    print(f"Não tem o Número Procurado")
else:
    print(f"Tem, {qtdK} vez(es). Posições: {posicoes}")
