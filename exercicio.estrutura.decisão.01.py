#Escrever um programa que encontre o primeiro múltiplo de 26 a partir do
# número 300

n= 300
while(n < 10000):
 n = n + 1
if n % 26 == 0:
 print("Encontrei: ", n)
n = 20000  