# -*- coding: utf-8 -*-
"""Mult_matriz.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M0yQYlhiyktHIAccNUgUaZLjBrXVDM6g

Testando a Multiplicação  de  Matrizes de forma paralela

1.Medir o tempo da versão serial;
2. Desenvolver a versão paralela baseada em threads /linhas;
3.Fazer o gráfico de tempo de execução por tamnho das matrizes;
"""

# importações Iniciais
import numpy as np
import time
import matplotlib.pyplot as plt

"""Exemplo 1
C= A.B

A(100,100)

B(100,100)
"""

# Criando s matrizes
dim=100
C=np.zeros((dim,dim))
A=np.random.rand(dim,dim)
B=np.random.rand(dim,dim)

# calculando o tempo Serial
start=time.time()

#C=A.dot(B)

for i in range(100):
  for j in range(100):
    for k in range(100):
      C[i,j]+=A[i,k]*B[k,j]
end=time.time()
print("Tempo Seria: {}".format(end-start))

"""Resultados:
dim= 100

Tempo Seria(numPy): 0.0045299530029296875
Tempo Seria(loop): 0.8743231296539307
"""

# Versão  Paralela:
"""A=[[3,5],[1,2]]
B=[[2,-5],[-1,3]]
C=[[-9,-9],[0,0]]"""
def task(a,b,c,lin):
 # a matriz sobre a qual as linhas(lin) serão destacadas
 # b matriz sobre a qual as colunas serão destacadas
 # c matriz resultado
   for col in range(len(b[0])):
     for i in range(len(a[0])):
      c[lin][col]+=a[lin][i]*b[i][col]
   return
task(A,B,C,0)
print(C)