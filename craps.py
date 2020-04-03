# Importando bibliotecas necessárias
import sys 
import time
import random
# Introduzindo o jogo
time.sleep(1)
print('Seja bem vindo ao Lahiry\'s Cassino!')
time.sleep(2)
print('Está pronto para uma partida de Craps?')
time.sleep(1)
ready = input('Se quiser jogar digite "sim", se não, digite "não": ')
while ready != 'sim' and ready != 'não':
    ready = input('Se quiser jogar digite "sim", se não, digite "não": ')


# Perguntando se o jogador quer ver as regras    
if ready == 'sim':
    time.sleep(1)
    print('Gostaria de ver as regras?')
    time.sleep(1)
    regras = input('Digite "sim" para ver as regras ou "não" para começar a jogar: ')
    while regras != 'sim' and regras != 'não':
        regras = input('Digite "sim" para ver as regras ou "não" para começar a jogar: ')
# Saindo do cassino caso o jogador não queira mais jogar
if ready == 'não':
    time.sleep(1)
    print('Obrigado pela sua visita! Volte sempre!')
    time.sleep(1)
    sys.exit()


# Mostrando as regras do Craps caso o usuário queira
if regras == 'sim':
    time.sleep(1)
    print("""\
    
Regras do Craps:
    O jogo acontece por meio de rodadas sucessivas, onde você deve decidir 
    apostar ou sair do jogo, ou automaticamente sair se acabaram todas suas fichas. 
    Neste jogo uma rodada pode ter duas fases, começando com uma chamada de “Come Out” 
    e conforme o resultado, passar para a fase de “Point”. Você pode fazer vários tipos 
    de apostas conforme a fase. O lançamento de dois dados de 6 lados é feito de modo 
    aleatório para o jogo. Conforme a fase do jogo, você terá diferentes opções de apostas
    e poderá fazer apostas de mais de um tipo por vez.


    Os tipos de apostas são as seguintes:


    Pass Line Bet –  Se a soma dos dados lançados for 7 ou 11, você ganha (por exemplo:
    se apostou 10 fichas, mantem as 10 e recebe mais 10). Já se os dados somarem 2, 3 ou 12,
    (chamado de craps) você perde (ou seja, se apostou 10 fichas, não recebe nada e perde essas 10).
    Já se a soma dos dados der 4, 5, 6, 8, 9 ou 10, o jogo muda para a fase de “Point” e o objetivo 
    muda. A aposta já feita continua valendo, porém, o valor tirado se torna o Point e para você
    ganhar agora, a soma do novo lançamento dos dados deve ser igual ao do Point. Se a
    nova soma dos dados é a mesma do que foi guardado no Point, você ganha o mesmo
    valor que apostou. Se sair uma soma de valor 7, você perde tudo. Caso saia qualquer
    outro número, se mantem na fase de “Point” sem perder ou ganhar, e continua o lançamento 
    de dados até um veredito, quando sair ou o número do Point, ou o 7, terminando essa
    rodada e deixando começar uma nova em “Come Out”.


    Field – Nesta aposta se  os dados derem 5, 6, 7 ou 8, você perde tudo, já se derem 
    3, 4, 9, 10, ou 11,  você ganha o mesmo valor que apostou. Já se a soma for 2, você 
    ganha o dobro do que apostou (se apostou 10 fichas, fica com as 10 e ganha mais 20). 
    Finalmente se sai 12 nos dados você ganha o triplo (se apostou 10 fichas, fica com as
    10 e ganha mais 30).


    Any Craps – Nesta aposta se o sdados derem 2, 3 ou 12, você ganha sete vezes o que apostou, 
    caso contrário perde a aposta.


    Twelve –  Nesta aposta se o dados derem 12, você ganha trinta vezes o que apostou, ou perde
    a aposta.

""")
    time.sleep(1)
    # Perguntando se o jogador está pronto para começar a jogar
    pronto = input('Digite "pronto" quando quiser começar: ')
    while pronto != "pronto":
        pronto = input('Digite "pronto" quando quiser começar: ')


# Iniciando o jogo
if regras == 'não' or pronto == 'pronto':
    time.sleep(1)
    print('Vamos começar o jogo')
    time.sleep(2)
    print('Lembre-se que pode sair quando quiser digitando "sair" ao invés do tipo de aposta')
    time.sleep(2)
    print('Se quiser ver os tipos de apostas que podem ser feitas digite "?"')
    time.sleep(2)
    # Verificando se fichas é um número inteiro
    fichas = 'x'
    while not isinstance(fichas, int):
        try:
            fichas = int(input('Quantas fichas deseja comprar?: '))
        except ValueError:
            print('?????')
            time.sleep(1)
    time.sleep(1)
    comeout = True


# Fase Come Out   
if comeout == True:
    aposta = "x"
    # Continuar o jogo até que o jogador perca todas suas fichas ou decida sair
    while fichas != 0 and aposta != "sair":
        Point = False
        print('Fase: Come Out')
        time.sleep(1)
        print('Suas fichas: {0}'.format(fichas))
        time.sleep(1)
        # Apostas múltiplas
        aposta = input('Que tipos de aposta você quer fazer?: ')
        while 'Pass Line Bet' not in aposta and 'Field' not in aposta and 'Any Craps' not in aposta and 'Twelve' not in aposta:
            # Apostas disponíveis (?)        
            if aposta == "?":
                if comeout == True:
                    time.sleep(1)
                    print('Apostas: Pass Line Bet, Field, Any Craps e Twelve')
                    aposta = input('Que tipos de aposta você quer fazer?: ')
            # Desistência
            if aposta == "sair":
                print('Obrigado por jogar! Você saiu com {0} fichas!'.format(fichas))
                print('Volte sempre!')
                sys.exit()
            time.sleep(1)




        # Apostando diferentes quantidades em diferentes apostas
        # Aposta em Pass Line Bet
        if "Pass Line Bet" in aposta:
            # Verificando se pass_line_bet_bet é um número inteiro
            pass_line_bet_bet = 'x'
            while not isinstance(pass_line_bet_bet , int): 
                try:
                    pass_line_bet_bet = int(input('Quantas fichas você quer apostar em Pass Line Bet?: '))
                except ValueError:
                    print('?????')
                    time.sleep(1)
            # Checando se o jogador pode fazer a aposta
            while pass_line_bet_bet > fichas:
                time.sleep(1)
                print('Você não tem tantas fichas!')
                time.sleep(1)
                print('Suas fichas: {0}'.format(fichas))
                time.sleep(1)
                # Verificando se pass_line_bet_bet é um número inteiro
                pass_line_bet_bet = 'x'
                while not isinstance(pass_line_bet_bet , int): 
                    try:
                        pass_line_bet_bet = int(input('Quantas fichas você quer apostar em Pass Line Bet?: '))
                    except ValueError:
                        print('?????')
                        time.sleep(1)
            fichas -= pass_line_bet_bet


        # Aposta em Field
        if "Field" in aposta:
            # Verificando se field_bet é um número inteiro
            field_bet = 'x'
            while not isinstance(field_bet , int): 
                try:
                    field_bet = int(input('Quantas fichas você quer apostar em Field?: '))
                except ValueError:
                    print('?????')
                    time.sleep(1)
            # Checando se o jogador pode fazer a aposta
            while field_bet > fichas:
                time.sleep(1)
                print('Você não tem tantas fichas!')
                time.sleep(1)
                print('Suas fichas: {0}'.format(fichas))
                time.sleep(1)
                # Verificando se field_bet é um número inteiro
                field_bet = 'x'
                while not isinstance(field_bet , int): 
                    try:
                        field_bet = int(input('Quantas fichas você quer apostar em Field?: '))
                    except ValueError:
                        print('?????')
                        time.sleep(1)
            fichas -= field_bet


        # Aposta em Any Craps
        if "Any Craps" in aposta:
            # Verificando se any_craps_bet é um número inteiro
            any_craps_bet = 'x'
            while not isinstance(any_craps_bet , int): 
                try:
                    any_craps_bet = int(input('Quantas fichas você quer apostar em Any Craps?: '))
                except ValueError:
                    print('?????')
                    time.sleep(1)
            # Checando se o jogador pode fazer a aposta
            while any_craps_bet > fichas:
                time.sleep(1)
                print('Você não tem tantas fichas!')
                time.sleep(1)
                print('Suas fichas: {0}'.format(fichas))
                time.sleep(1)
                # Verificando se any_craps_bet é um número inteiro
                any_craps_bet = 'x'
                while not isinstance(any_craps_bet , int): 
                    try:
                        any_craps_bet = int(input('Quantas fichas você quer apostar em Any Craps?: '))
                    except ValueError:
                        print('?????')
                        time.sleep(1)
            fichas -= any_craps_bet
 

        # Aposta em Twelve
        if "Twelve" in aposta:
            # Verificando se twelve_bet é um número inteiro
            twelve_bet = 'x'
            while not isinstance(twelve_bet , int): 
                try:
                    twelve_bet = int(input('Quantas fichas você quer apostar em Twelve?: '))
                except ValueError:
                    print('?????')
                    time.sleep(1)
            # Checando se o jogador pode fazer a aposta
            while twelve_bet > fichas:
                time.sleep(1)
                print('Você não tem tantas fichas!')
                time.sleep(1)
                print('Suas fichas: {0}'.format(fichas))
                time.sleep(1)
                # Verificando se twelve_bet é um número inteiro
                twelve_bet = 'x'
                while not isinstance(twelve_bet , int): 
                    try:
                        twelve_bet = int(input('Quantas fichas você quer apostar em Twelve?: '))
                    except ValueError:
                        print('?????')
                        time.sleep(1)
            fichas -= twelve_bet
            



        # Lançamento de dados para todas apostas feitas
        d1 = [1,2,3,4,5,6]
        d2 = [1,2,3,4,5,6]
        dado_1 = ["⚀","⚁","⚂","⚃","⚄","⚅"]
        dado_2 = ["⚀","⚁","⚂","⚃","⚄","⚅"]
        # Somando os números aleatórios tirados para cada dado
        soma = random.choice(d1) + random.choice(d2)
        time.sleep(1)
        # Mecânica de lançamento dos dados
        print('Lançando dados:')
        time.sleep(1)
        print(random.choice(dado_1), random.choice(dado_2))
        time.sleep(1)
        print(random.choice(dado_1), random.choice(dado_2))
        time.sleep(1)
        print(random.choice(dado_1), random.choice(dado_2))
        time.sleep(1)
        # Informando o resultado dos dados
        print('A soma do lançamento dos dados é {0}'.format(soma))




        # Aposta Pass Line Bet   
        if "Pass Line Bet" in aposta:
            time.sleep(1)
            print('Aposta: Pass Line Bet')
            # Jogador ganhou a aposta
            if soma == 7 or soma == 11:
                time.sleep(1)
                print('Você ganhou a aposta e conseguiu {0} fichas!'.format(pass_line_bet_bet))
                fichas += pass_line_bet_bet + pass_line_bet_bet
            # Jogador perdeu a aposta
            if soma == 2 or soma == 3 or soma == 12:
                time.sleep(1)
                print('Você não ganhou a aposta e perdeu {0} fichas.'.format(pass_line_bet_bet)) 
                # Fichas acabaram
                if fichas < 1:
                    time.sleep(1)
                    print('Suas fichas acabaram!')
                    time.sleep(1)
                    print('Obrigado por jogar e volte sempre!')
                    sys.exit()
            # Jogador passou para fase Point
            if soma == 4 or soma == 5 or soma == 6 or soma == 8 or soma == 9 or soma == 10:
                time.sleep(1)
                print('Você passou para a fase Point!')
                Point = True
            
    
        # Fase Point
        if Point == True:
            point = soma
            time.sleep(1)
            print('Fase: Point')
            time.sleep(1)
            print('Suas fichas: {0}'.format(fichas))
            time.sleep(1)
            # Informando o Point
            print('O Point da fase é {0}'.format(point))
            time.sleep(1)
            dados_point = random.choice(d1) + random.choice(d2)
            # Lançando dados até um veredito
            while dados_point != point and dados_point != 7:
                print('Lançando dados:')
                time.sleep(1)
                print(random.choice(dado_1), random.choice(dado_2))
                time.sleep(1)
                print(random.choice(dado_1), random.choice(dado_2))
                time.sleep(1)
                print(random.choice(dado_1), random.choice(dado_2))
                time.sleep(1)
                print('Você tirou {0} nos dados, continue jogando!'.format(dados_point))
                dados_point = random.choice(d1) + random.choice(d2)
            # Jogador acertou o point
            if dados_point == point:
                time.sleep(1)
                print('Lançando dados:')
                time.sleep(1)
                print(random.choice(dado_1), random.choice(dado_2))
                time.sleep(1)
                print(random.choice(dado_1), random.choice(dado_2))
                time.sleep(1)
                print(random.choice(dado_1), random.choice(dado_2))
                time.sleep(1)
                print('Você acertou o Point e ganhou {0} fichas!'.format(pass_line_bet_bet))
                time.sleep(1)
                fichas += pass_line_bet_bet + pass_line_bet_bet
            # Jogador perdeu a aposta
            if dados_point == 7:
                time.sleep(1)
                print('Lançando dados:')
                time.sleep(1)
                print(random.choice(dado_1), random.choice(dado_2))
                time.sleep(1)
                print(random.choice(dado_1), random.choice(dado_2))
                time.sleep(1)
                print(random.choice(dado_1), random.choice(dado_2))
                time.sleep(1)
                print('Você tirou 7 nos dados e perdeu {0} fichas!'.format(pass_line_bet_bet))
                time.sleep(1)
                # Fichas acabaram
                if fichas < 1:
                    time.sleep(1)
                    print('Suas fichas acabaram!')
                    time.sleep(1)
                    print('Obrigado por jogar e volte sempre!')
                    sys.exit()
    
            


        # Aposta Field
        if "Field" in aposta:
            time.sleep(1)
            print('Aposta: Field')
            # Jogador perdeu a aposta
            if soma == 5 or soma == 6 or soma == 7 or soma == 8:
                time.sleep(1)
                print('Você não ganhou a aposta e perdeu {0} fichas!.'.format(field_bet))
                # Fichas acabaram
                if fichas < 1:
                    time.sleep(1)
                    print('Suas fichas acabaram!')
                    time.sleep(1)
                    print('Obrigado por jogar e volte sempre!')
                    sys.exit()
            # Jogador ganhou a aposta
            if soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
                time.sleep(1)
                print('Você ganhou a aposta e conseguiu {0} fichas!'.format(field_bet))
                fichas += field_bet + field_bet
            # Jogador ganhou a aposta x2
            if soma == 2:
                time.sleep(1)
                print('Você ganhou a aposta e conseguiu {0} fichas!'.format(field_bet*2))
                fichas += (field_bet*2) + field_bet
            # Jogador ganhou a aposta x3
            if soma == 12:
                time.sleep(1)
                print('Você ganhou a aposta e conseguiu {0} fichas!'.format(field_bet*3))
                fichas += (field_bet*3) + field_bet



        # Aposta Any Craps
        if "Any Craps" in aposta:
            time.sleep(1)
            print('Aposta: Any Craps')
            # Jogador ganhou a aposta
            if soma == 2 or soma == 3 or soma == 12:
                time.sleep(1)
                print('Você ganhou a aposta e conseguiu {0} fichas!'.format(any_craps_bet*7))
                fichas += (any_craps_bet*7) + any_craps_bet
            # Jogador perdeu a aposta
            else:
                time.sleep(1)
                print('Você não ganhou a aposta e perdeu {0} fichas.'.format(any_craps_bet))
                # Fichas acabaram    
                if fichas < 1:
                    time.sleep(1)
                    print('Suas fichas acabaram!')
                    time.sleep(1)
                    print('Obrigado por jogar e volte sempre!')
                    sys.exit()


        # Aposta Twelve
        if "Twelve" in aposta:
            time.sleep(1)
            print('Aposta: Twelve')
            # Jogador ganhou a aposta (12)
            if soma == 12:
                time.sleep(1)
                print('Você ganhou a aposta e conseguiu {0} fichas!'.format(twelve_bet*30))
                fichas += (twelve_bet*30) + twelve_bet
            # Jogador perdeu a aposta
            else:
                time.sleep(1)
                print('Você não ganhou a aposta e perdeu {0} fichas.'.format(twelve_bet))
                # Fichas acabaram    
                if fichas < 1:
                    time.sleep(1)
                    print('Suas fichas acabaram!')
                    time.sleep(1)
                    print('Obrigado por jogar e volte sempre!')
                    sys.exit()