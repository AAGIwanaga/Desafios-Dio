LIMITE_SAQUES = 3
LIMITE = 500


class Main: #CRIAÇÃO DA FUNÇÃO PRINCIPAL, QUE CONTERÁ AS DEMAIS FUNÇÕES



    menu_2 = ''


    def __init__(self, saldo = 10000, extrato = 0, numero_saques = 0, tentativas = 0, lista_usuario = []):
        self.saldo = saldo
        self.extrato = extrato
        self.numero_saques = numero_saques
        self.menu01 = {}
        self.menu02 = {}
        self.tela01 = {}
        self.tentativas = tentativas
        self.lista_usuario = lista_usuario
        self.ver_lista_usuario = {}
    

    def extracao_dados(self, filtro_chave_1, filtro_chave_2, lista, dicio): # VARRE OS DICIONÁRIOS DA LISTA 'menu' E RETORNA 2 VALORES EM UM NOVO DICIONÁRIO
                                                                    # 'filtro_chave_1' = TEXTO CONTIDO DA CHAVE, QUE SERÁ A NOVA CHAVE DENTRO DO DICIONÁRIO 'menu'
                                                                    # 'filtro_chave_2' = TEXTO CONTIDO DA CHAVE, QUE SERÁ O VALOR DA NOVA CHAVE DENTRO DO DICIONÁRIO 'menu'
                                                                    # 'novo_dicio' = VARIÁVEL QUE RECEBERÁ NOVA RELAÇÃO DE DICIONÁRIOS
        
        for item in lista: # SEPARA CADA UM DOS ITEMS DA LISTA 'menu' (CADA ITEM É 1 DICIONÁRIO)

            for chave00, valor00 in item.items(): # NOMEIA A RELAÇÃO CHAVE/VALOR DE DENTRO DE CADA ITEM DE DENTRO DO DICIONÁRIO 

                if chave00 == filtro_chave_1: # SE A 'key' DENTRO DO DICIONÁRIO 'item.menu' FOR IGUAL AO TEXTO DO PARAMETRO 1, 'filtro_chave_1', 
                    chave_extraido = valor00 # TRANSFERE O 'value' PARA A VARIÁVEL 'chave_extraido'
                elif chave00 == filtro_chave_2: # SE A 'key' DENTRO DO DICIONÁRIO 'item.menu' FOR IGUAL AO TEXTO DO PARAMETRO 2, 'filtro_chave_2', 
                    valor_extraido = valor00 # TRANSFERE O 'value' PARA A VARIÁVEL 'valor_extraido'
                else:
                    pass

            #dicio = novo_dicio # CRIA UMA VARIÁVEL PARA O PARAMETRO 3, 'novo_dicio'
            dicio.update({chave_extraido : valor_extraido}) #INCLUI A RELAÇÃO 'chave_extraido' E 'valor_extraido' COMO NOVO ITEM NESTE NOVO DICIONÁRIO

    def opcao_deposito(self): #CRIAÇÃO DA FUNÇÃO DE DEPÓSITO

        valor_depot = input('Informe o valor a ser depositado: ') # EXIBE E PEDE PARA INSERIR DADOS

        try: # O CÓDIGO IRÁ VERIFICAR
            valor_depot = float(valor_depot) # CASO O QUE FOI DIGITADO SEJA UM VALOR 'float'
            return valor_depot #RETORNA O PRÓPRIO VALOR

        except: #CASO NÃO SEJA UM VALOR 'float'
            valor_depot = str(valor_depot) #VERIFICAÇÃO SE É 'string'
            pass 

        finally: 
            if isinstance(valor_depot, str) is True: # CASO O 'input' DIGITADO SEJA UMA 'string'
                print('Caractere informado é "str"') # RETORNA UMA MENSAGEM DE ERRO
                self.tentativas += 1
                return
            else:
                #CASO O 'input' SEJA UM VALOR, CONTINUARÁ PARA O CÓDIGO SEGUINTE
                #valor = float(input('Informe o valor a ser depositado: '))
                if valor_depot > 0: # SE VALOR INSERIDO FOR MAIOR DO QUE 0
                    self.saldo += valor_depot # ADICIONA O VALOR INPUTADO NA VARIÁVEL ''saldo''
                    #self.extrato += f'Depósito: R$ {valor: .2f}' # A VARIÁVEL 'extrato' ADICIONA O VALOR A VARIÁVEL 'extrato'
                    self.extrato += round(valor_depot, 2) # VALOR DEPOSITADO ESTÁ SENDO ADICIONADO À VAR 'extrato'
                    print(f'Depósito: R$ {valor_depot}')

                elif valor_depot == 0: #CASO O VALOR INSERIDO SEJA EXATAMENTE ZERO
                    print('Não pode depositar 0') # RETORNA A MENSAGEM DE ERRO
                    self.tentativas += 1
                    #opcao_deposito()

                else: # CASO NÃO SEJA NENHUMA DAS ALTERNATIVAS ANTERIORES, OU SEJA, FOI INSERIDO UM VALOR NEGATIVO
                    print('\nNão é possível depositar um valor negativo,\nPortanto, o valor está sendo convertido para positivo\n') # EXIBE A MENSAGEM DE ERRO
                    valor_depot = abs(valor_depot) #O VALOR É CONVERTIDO PARA POSITIVO
                    self.saldo += valor_depot # O VALOR INPUTADO É ADICIONADO À VARIÁVEL ''saldo''
                    self.extrato += round(valor_depot, 2)# VALOR DEPOSITADO ESTÁ SENDO ADICIONADO À VAR 'extrato'
                    print(f'Depósito: R$ {valor_depot}')

    def opcao_sacar(self): # CRIADA A FUNÇÃO PARA A OPÇÃO DE SACAR DINHEIRO
        valor = float(input('Informe o valor do Saque: ')) # PEDE PARA INSERIR O VALOR DO SAQUE

        if valor > self.saldo: # VALIDAÇÃO SE O VALOR DIGITADO É MAIOR DO QUE O 'SALDO' DISPONIVEL
            print('Saldo insuficiente') #CASO POSITIVO, EXIBE A MENSAGEM DE ERRO
            self.tentativas += 1
            return

        elif valor > LIMITE: # CASO O VALOR SEJA MAIOR DO QUE O LIMITE PERMITIDO (R$ 500,00)
            print('Saque excedeu o limite') #EXIBE OUTRA MENSAGEM DE ERRO
            self.tentativas += 1
            return

        elif self.numero_saques >= LIMITE_SAQUES: # CASO A QUANTIDADE LIMITE DE SAQUES TENHA SIDO FEITA (3)
            print('Quantidade máxima de saques diário foi alcançada.\nGentileza voltar amanhã') #EXIBE OUTRA MENSAGEM DE ERRO
            self.tentativas += 1
            #print(self.numero_saques)
            return

        elif valor > 0: #CASO NENHUMA DAS CONDIÇÕES ANTERIORES SEJA ATENDIDA
            self.saldo -= valor # O VALOR INSERIDO É SUBTRAÍDO DA VARIÁVEL 'valor'
            #self.extrato -= round(valor, 2) # O EXTRATO É ATUALIZADO E EXIBIDO
            print(f'Saque: R$ {round(valor, 2)}')
            print(f'Saldo Atualizado: R$ {self.saldo}')
            self.numero_saques += 1 # A VARIÁVEL 'numero_saques' RECEBE MAIS UM CONTADOR

        else: # CASO ESTA ÚLTIMA CONDIÇÃO NÃO SEJA POSSÍVEL TAMBÉM
            print('O valor informado é invalido') # EXIBE A MENSAGEM
            self.tentativas += 1

    def opcao_extrato(self): #FUNÇÃO CRIADA PARA EXIBIR O EXTRATO, APENAS EXIBE UMA DAS MENSAGENS A SEGUIR

        print(f'''
        ============= EXTRATO =============
        Não foram realizadas movimentações.''' if not self.extrato else self.extrato)

        print(f'''
        Saldo: R$ {round(self.saldo, 2)}
        ===================================
        ''')

    def opcao_sair(self): #OPÇÃO DESTINADA A FINALIZAR O SISTEMA
        print('''
        =========================================
        Obrigado por utilizar os nossos serviços.
        Agradecemos a preferência.
        Volte sempre!
        =========================================
        ''')
        
    def opcao_invalida(self): #FUNÇÃO CRIADA PARA CASO TENHA INSERIDO ALGO DIFERENTE DAS LETRAS DA 'key' DO DICIONÁRIO
        print('Operação inválida, favor selecionar novamente a operação desejada')

    ''' 
    1 - LOGIN
        1.1 - INSERIR DADOS DO LOGIN
        1.2 - TEM LOGIN
            1.1.1 - PREENCHER INFORMAÇÕES DE LOGIN E SEGUIR PARA ETAPA 2
                1.1.1.1 - nome, 
                1.1.1.2 - data de nascimento, 
                1.1.1.3 - cpf e 
                1.1.1.4 - endereço
        1.2 - NÃO TEM LOGIN
            1.2.1 CRIAR E ARMAZENAR USUÁRIO - PREENCHER FORMULÁRIO COM INFOS, E RETORNAR PARA ETAPA 1
            
    2 - VALIDAÇÃO DAS INFORMAÇÕES
        2.1 - VALIDAR SE ENCONTRA INFOS DO USUÁRIO
            2.2.1 -INFORMAÇÕES ERRADAS -> VOLTAR PARA ETAPA 1.1.1
            2.2.2 - NÃO EXISTE -> ETAPA 1.2.1
        2.2 - INFORMAÇÕES OK -> ETAPA 3

    3 - CONTA CORRENTE
        3.1 - TEM CONTA CORRENTE (ARMAZENADO DENTRO DE UMA LISTA)
            3.1.1 - SELECIONAR CONTA DESEJADA
        3.2 - NÃO TEM CONTA CORRENTE
            3.2.1 - CADASTRAR CONTA CORRENTE
                3.2.1.1 - AGENCIA (SEMPRE "0001")
                3.2.1.2 - NRO CONTA (SEQUENCIAL INICIANDO POR 1)
                3.2.1.3 - USUÁRIO
            3.3 - RETORNAR PARA 3.1

    4 - SEGUIR PARA PRÓXIMA -> 'Tela inicial'

    '''
    def login(self):
        cpf = input('Insira o CPF do usuário: ')

        self.extracao_dados('CPF', 'Nome', lista_usuario, self.ver_lista_usuario)

        for chave04, valor04 in self.ver_lista_usuario.items():
            if cpf not in self.ver_lista_usuario.keys():
                print('Cadastrar usuário')
                return

            elif chave04 == cpf:
                print(f'Seja bem vindo, {valor04}')
                print('Tela inicial')

    def cadastro(self):
        nome = input('Digite o seu nome completo: ')
        

        
    def usuario(self, nome, data_nasc, cpf, endereco, logradouro, nro, bairro, cidade, sigla_estado):
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf # CADA CPF SÓ PODE TER UM ÚNICO USUÁRIO
        self.logradouro =logradouro
        self.nro = nro
        self.bairro = bairro
        self.cidade = cidade
        self.sigla_estado = sigla_estado
        self.endereco = print(f'{logradouro}, {nro} - {bairro} - {cidade}/{sigla_estado}')

        #def conta_corrente(self, ag, num_cont, usuario):
        #    self.ag = ag # NÚMERO DA AGENCIA FIXADO EM '0001'
        #    self.num_cont = num_cont # NÚMERO SEQUENCIAL, INICIADO EM 1
        #    self.num_usuario = num_usuario #O USUÁRIO PODE TER MAIS DE UMA CONTA, MAS UMA CONTA PERTENCE A SOMENTE UM USUÁRIO

    def verific_conta(self):
        self.extracao_dados('CPF', 'Data de Nascimento', lista_usuario, self.ver_lista_usuario)
        
        for chave03, valor03, in self.ver_lista_usuario.items():
            print(f' {chave03} : {valor03}')
        
        #print(self.lista_usuario)

    global lista_usuario
    lista_usuario = [
        {'Nome' : 'André Arthur Gusmão Iwanaga', 'Data de Nascimento' : '20071991', 'CPF' : '38379419812', 'Endereço' : ''},
        {'Nome' : 'asda', 'Data de Nascimento' : 'dfas', 'CPF' : '123123', 'Endereço' : ''},
        {'Nome' : 'asdfgvds', 'Data de Nascimento' : '123123', 'CPF' : 'asdfasdf', 'Endereço' : ''}
    ]

    global MENU
    MENU = [
        {'Opção' : 'd',  'Relação' : 'Depositar', 'Função' : opcao_deposito},
        {'Opção' : 's',  'Relação' : 'Sacar', 'Função' : opcao_sacar},
        {'Opção' : 'e',  'Relação' : 'Extrato', 'Função' : opcao_extrato},
        {'Opção' : 'q',  'Relação' : 'Sair', 'Função' : opcao_sair}
    ]

    def tela_inicial(self): # NOVA FUNÇÃO PARA EXIBIR A TELA INICIAL
        self.extracao_dados('Opção', 'Relação', MENU, self.menu01) # CRIA UMA NOVA VARIÁVEL PARA A FUNÇÃO 'extracao_dados'
        print('Dentre as seguintes opções: ') #EXIBE A MENSAGEM

        for chave01, valor01 in self.menu01.items(): # FAZ UMA VARREDURA DOS ITEMS DO DICIONÁRIO 'menu01'
            print(f' [{chave01}] : {valor01}') #EXIBE A RELAÇÃO DELES

        entrada = input('Digite a letra entre colchetes: ') #EXIBE A MENSAGEM PEDINDO PARA O USUÁRIO FAZER UMA SELEÇÃO

        #def switch_tela(): #FUNÇÃO DESTINADA A ALTERAR A PAGINA A SER EXIBIDA DE ACORDO COM OS INPUTS
        self.extracao_dados('Opção', 'Função', MENU, self.tela01)


        if entrada not in self.tela01.keys():
            self.tentativas += 1
            if self.tentativas > 3:
                print(f'Quantidade de tentativas excedida. \n {self.opcao_sair()}')
                return

            else:
                print('A opção escolhida não está disponível.\n Tente novamente.') # RETORNA UMA MENSAGEM DE ERRO
                #self.tentativas += 1
                #print(self.tentativas)
                self.tela_inicial()
                return
            
        else:
            for chave02, valor02 in self.tela01.items():
                if entrada == 'q':
                    self.opcao_sair()
                    return

                elif chave02 == entrada:
                    self.tela01[chave02](self)
                    #print(self.tentativas)
                    self.tela_inicial()
                    break

                else:
                    pass

            
p1 = Main()

p1.login()