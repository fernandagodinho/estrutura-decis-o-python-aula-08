import random
numero = random.randint(1,5)
chute = int(input('Entre com um valor entre 10 e 19: '))
if chute == numero:
 print('Parabéns, acertou!')
else:
 print('Não foi desta vez.')