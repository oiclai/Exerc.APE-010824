# Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
# • Os números que estão nos índices pares;
# • Os números que estão nos índices ímpares.
vetor=[]
for i in range(10):
    elem=int(input(""))
    vetor.append(elem)
par=[]
impar=[]
for i in range(10):
    if i%2==0:
        par.append(vetor[i])
    else:
        impar.append(vetor[i])
print(par)
print(impar)

# SEM O USO DE OUTROS VETORES:
'''
PARES:
for i in range(10):
    if (i%2==0):
        print(vetor[i])
        
OU

for i in range(0,10,2):
    print(vetor[i])

IMPARES:
for i in range(10):
    if (i%2!=0):
        print(vetor[i])

OU

for i in range(1,10,2):
    print(vetor[i])
'''
