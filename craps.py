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


# Mostrando as regras do Craps caso o usuário queira
if regras == 'sim':
    print("""\
    
Regras do Craps:
    O jogo acontece por meio de rodadas sucessivas, onde você deve decidir 
    apostar ou sair do jogo, ou automaticamente sair se acabaram todas suas fichas. 
    Neste jogo uma rodada pode ter duas fases, começando com uma chamada de “Come Out” 
    e conforme o resultado, passar para a fase de “Point”. Você pode fazer vários tipos 
    de apostas conforme a fase. O lançamento de dois dados de 6 lados é feito de modo 
    aleatório para o jogo. Conforme a fase do jogo, você terá diferentes opções de apostas
    e poderá fazer apostas de mais de um tipo por vez.


    Os tipo de apostas são as seguintes:


    Pass Line Bet – Esta aposta só pode ser feita na fase de “Come Out”. Se a soma dos
    dados lançados for 7 ou 11, você ganha (por exemplo: se apostou 10 fichas, mantem
    as 10 e recebe mais 10). Já se os dados somarem 2, 3 ou 12, (chamado de craps) você
    perde (ou seja, se apostou 10 fichas, não recebe nada e perde essas 10). Já se a soma
    dos dados der 4, 5, 6, 8, 9 ou 10, o jogo muda para a fase de “Point” e o objetivo muda. 
    A aposta já feita continua valendo, porém, o valor tirado se torna o Point e para você
    ganhar agora, a soma do novo lançamento dos dados deve ser igual ao do Point. Se a
    nova soma dos dados é a mesma do que foi guardado no Point, você ganha o mesmo
    valor que apostou. Se sair uma soma de valor 7, você perde tudo. Caso saia qualquer
    outro número, se mantem na fase de “Point” sem perder ou ganhar, e continua o lançamento 
    de dados até um veredito, quando sair ou o número do Point, ou o 7, terminando essa
    rodada e deixando começar uma nova em “Come Out”.


    Field – Esta aposta pode ser feita em qualquer fase do jogo. Nesta aposta se 
    os dados derem 5, 6, 7 ou 8, você perde tudo, já se derem 3, 4, 9, 10, ou 11, 
    você ganha o mesmo valor que apostou. Já se a soma for 2, você ganha o dobro do
    que apostou (se apostou 10 fichas, fica com as 10 e ganha mais 20). Finalmente se 
    sai 12 nos dados você ganha o triplo (se apostou 10 fichas, fica com as 10 e ganha mais 30).


    Any Craps – Esta aposta pode ser feita em qualquer fase do jogo. Nesta aposta se o
    dados derem 2, 3 ou 12, você ganha sete vezes o que apostou, caso contrário perde a aposta.


    Twelve – Esta aposta pode ser feita em qualquer fase do jogo. Nesta aposta se o dados
    derem 12, você ganha trinta vezes o que apostou, ou perde a aposta.

""")
    pronto = input('Digite "pronto" quando quiser começar: ')
    while pronto != "pronto":
        pronto = input('Digite "pronto" quando quiser começar: ')


# Iniciando o jogo
if regras == 'não' or pronto == 'pronto':
    time.sleep(1)
    print('Vamos começar o jogo')
    time.sleep(1)
    print('Lembre-se que pode sair quando quiser digitando "sair" ao invés do tipo de aposta')
    time.sleep(1)
    fichas = int(input('Quantas fichas deseja comprar?: '))
    time.sleep(1)
    comeout = True


# Fase Come Out   
if comeout == True:
    time.sleep(1)
    print('Fase: Come Out')
    time.sleep(1)
    print('Suas fichas: {0}'.format(fichas))
    time.sleep(1)
    bet = int(input('Quantas fichas você quer apostar?: '))
    time.sleep(1)
    aposta = input('Que tipo de aposta você quer fazer?: ')
    while aposta != 'Pass Line Bet' and aposta != 'Field' and aposta != 'Any Craps'and aposta != 'Twelve':
        aposta = input('Que tipo de aposta você quer fazer?: ')
