from random import randint
from time import sleep



DEFAULT_ATK =  {
    'Ataque Especial': 300,
    'Ataque Ariscado': 200,
    'Ataque Magico De Gelo': 100
}


class Jogador:
    def __init__(self, nome):

        self.level = 6
        self.xp = 0
        self.dano  = (self.level // 2) * 10
        self.usu_dano_max = self.dano + 10
        self.usu_dano_min = self.dano

        self.habilidades = DEFAULT_ATK
       
        self.botões_habilidades = { '1' : 'Ataque Ariscado',
                                   '2' : 'Ataque Magico De Gelo',
                                   '3' : 'Ataque Especial'}

        self.pontos_de_habilidades = 10
        self.hp = (self.level // 2) * 500
        self.nome = nome
        self.contagem_de_atake_especial = 2
    
    def regenera_hp(self):
        self.hp = (self.level // 2) * 500
    
    def _atacar(self, botao):

        nome_abilidade = self.botões_habilidades[botao]
        valor_abilidade = self.habilidades[nome_abilidade]
        dano_total = self.calcula_dano(valor_abilidade)
        print(f'{nome_abilidade} dano: {dano_total}')

        return dano_total

    def _verificador_pontos(self, pontos):
        if pontos < 5 :
            return False
        else:
            return True


    def atacar_player(self, botao, player_alvo):
        dano_total = self._atacar(botao)
        player_alvo.hp -= dano_total

    def calcula_dano(self, dano_base):
        valor_jogador = randint(self.usu_dano_min, self.usu_dano_max)
        return valor_jogador + dano_base
            
    def add_habilidade(self, nome_habilidade, dano_habilidade, botão , player ):
        
        if botão in player.botões_habilidades or nome_habilidade in player.habilidades  :
            return menu()

        else:
            player.habilidades.update({nome_habilidade : dano_habilidade})
            player.botões_habilidades.update({botão : nome_habilidade})


player1 = Jogador('joao')
player2 = Jogador('LUCAS')

def cont_especial_atk(player , verifica=False):
    if verifica :

        if player.contagem_de_atake_especial <= 0:
            return False
        else :
            return True
    else: 
        player.contagem_de_atake_especial -= 1
        
        if player.contagem_de_atake_especial <= 0:
            return False
        else :
            return True

 
def interface(player):
        cont_ataque_especial = cont_especial_atk(player , True)
        
        print(f'{player.nome} Sua vez de atacar !!')
        print(f'Menu De skils')
        print('-'*20)

        for botao, habilidade in player.botões_habilidades.items():
            
            msg_padrao = f'[{botao}] {habilidade}'

            if botao == '3' and not cont_ataque_especial :
                print(msg_padrao)
            else:      

                print(msg_padrao)

        print('-'*20)

        while True:
            Input = input('===> : ')

            if Input == '3' and not cont_ataque_especial:
                print('você não tem mais power para esse poder')
            elif Input == '3' and cont_ataque_especial:
                cont_ataque_especial = cont_especial_atk(player)
                return Input
            else: 
                return Input

def verifica_hp_player(player):
    return player.hp <= 0 

def interface_habilidades (player):
    
        if 'exploção de fogo' in player.habilidades:
            pass
        else:
            print('[1] exploção de fogo')
        if 'golpe de fogo' in player.habilidades:
            pass
        else:
            print('[2] golpe de fogo')
        
        Input = input(str('===> : '))
        
        if Input == '1':
            while True:
                botao = input(str('Qual botão vai ativar a habilidade : '))
                if botao in player.botões_habilidades:
                    print('Esse botão já esta acupado')
                else:    
                    player.add_habilidade('exploção de fogo', 300 ,botao, player)
                    return 

        if Input == '2':
            while True:
                botao = input(str('Qual botão vai ativar a habilidade : '))
                if botao in player.botões_habilidades:
                    print('Esse botão já esta acupado')
                else:    
                    player.add_habilidade('golpe de fogo', 250 ,botao, player)
                    return 

def painel_status (player):
    print(' -'*20)
    print(f'Nome :  {player.nome} ')
    print(f'Level :  {player.level} ')
    print(f'Dano :  {player.dano} ')
    print('-'*20,' ')
    print('Painel de skilsm')

    for habilidade , dano_base in player.habilidades.items():
        print(f' {habilidade} : dano base {dano_base}')
    print('-'*20)

def menu():
    print('''
[0] Para sair do jogo
[1] Entrar em uma partida
[2] Adicionar uma habilidade
[3] Mostar estatos do player''')

    Input = input(str('===> : '))

    if Input == '0':
        print("Vlw flw!")
        return

    if Input == '1':
        while True :

            if verifica_hp_player(player1):
                print(f'{player1.nome} Você perdeu !!')
                player1.regenera_hp()
                player2.regenera_hp()
                break
            if verifica_hp_player(player2):
                print(f'{player2.nome} Você perdeu !!')
                player2.regenera_hp()
                player1.regenera_hp()
                break

            Input = interface(player1)
            
            player1.atacar_player(Input,player2)
            Input = interface(player2)
            player2.atacar_player(Input,player1)
        menu()

    if Input == '2':

        
        while True:
            player = input('Qual nome do player : ')
            
            if player != player1.nome and player != player2.nome :
                print('Não á nem um player com esse nome !')
            
            if player == player1.nome:
                verifica_pontos = player1._verificador_pontos(player1.pontos_de_habilidades)
                if verifica_pontos:
                    interface_habilidades(player1)
                    break
                else:
                    print('Sem pontos')
                    break
            if player == player2.nome:
                verifica_pontos = player2._verificador_pontos(player2.pontos_de_habilidades)
                if verifica_pontos :
                    interface_habilidades(player2)
                    break
                else:
                    print('Sem pontos')
                    break
        
    if Input == '3':
        player = input('Qual nome do player : ')
        if player != player1.nome and player != player2.nome :
            print('Não á nem um player com esse nome !')
        else:
            if player == player1.nome:    
                painel_status(player1)
            if player == player2.nome:
                painel_status(player2)   
              
    menu()
        
menu()