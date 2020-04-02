# Introduzindo o jogo
import sys 
import time
import random
print('Seja bem vindo ao Lahiry\'s Cassino!')
time.sleep(1)
print('Está pronto para uma partida de Craps?')
time.sleep(1)
ready = input('Se quiser jogar digite "sim", se não, digite "não": ')
while ready != 'sim' and ready != 'não':
    ready = input('Se quiser jogar digite "sim", se não, digite "não": ')