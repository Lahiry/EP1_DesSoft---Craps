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

# Perguntando se o jogador quer ver as regras    
if ready == 'sim':
    print('Gostaria de ver as regras?')
    time.sleep(1)
    regras = input('Digite "sim" para ver as regras ou "não" para começar a jogar: ')
    while regras != 'sim' and regras != 'não':
        regras = input('Digite "sim" para ver as regras ou "não" para começar a jogar: ')
if ready == 'não':
    print('Obrigado pela sua visita! Volte sempre!')
    sys.exit()