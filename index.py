from time import sleep
print()
print(' '*5,'♫-♫-♫-♫-♫-♫-♫- Music -♪-♪-♪-♪-♪-♪-♪-♪')
print()
print(' '*12,'Olá. Bem Vindo a MUSIC ‼ \n')
cadastro = str(input('Deseja fazer um cadastro na music ? (sim/não)\n'))
if cadastro.lower() == 'sim':
    print('_'*80)
    print()
    nome = str(input('Digite seu nome: '))
    print('_'*80)
    print()
    print(' '*5 ,'Então vamos lá {}, crie seu nome de usuário e uma senha numérica.'.format(nome))
    print('_'*80)
    print()
    usuario = str(input('Usuário: ')) 
    while True:
        try:
            senha = int(input('Senha: '))  
            break
        except ValueError:
            print('Apenas números!')
    print('_'*80) 
    print()     
    print(' '*5,'Perfeito.Você está cadastrado.')
    print('_'*80)
    print()
    print(' '*2,'Vamos acessar sua conta.')    
    while True:
        usuCadastrado = str(input('Digite o usuário cadastrado: '))
        senhaCadastrada = int(input('Digite sua senha cadastrada: '))      
        if usuario.lower() == usuCadastrado.lower(): 
            if senha == senhaCadastrada:
                print('_'*80)
                print()
                print('Acesso liberado.')      
                break 
        elif usuario != usuCadastrado:
            if  senha != senhaCadastrada:
                print()
                print('Senha ou usuário inválidos!\n')
    print('_'*80)
    print()
    animacao = input('Precione a tecla enter para ver alguns gêneros musicais.')
    print()
    sleep(0.1)
    print(' '*1,'♫')
    sleep(0.1)
    print(' '*2,'♪')
    sleep(0.1)
    print(' '*3,'♫')
    sleep(0.1)
    print(' '*4,'♪')
    sleep(0.1)
    print(' '*5,'♫')
    sleep(1)  
    listaGeneros = ['Jazz','Axé','Blues','Country','Eletrônica','Forró','Funk','Gospel','Hip Hop', 'MPB', 'Música clássica', 'Pagode', 'Pop', 'Rap', 'Reggae', 'Rock', 'Samba', 'Sertanejo']
    for ls in (listaGeneros):
        print(' '*5,ls)
    print() 
    print('Agora que viu alguns dos gêneros. Queremos te conhecer melhor e mostrarmos à você algumas curiosidades.')
    print('_'*140)
    print()
    while True:
        try:
            nascimento = int(input('Digite o seu nascimento: '))
            print('_'*140)
            break
        except ValueError:
            print('Cuidado, não coloque qualquer outro tipo de caractere à não ser número.')
    
    if nascimento >= 2010:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu a eletrônica.')
    elif nascimento >= 2000:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o raggae.')
    elif nascimento >= 1995:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o rap.')
    elif nascimento >= 1985:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o funk.')
    elif nascimento >= 1975:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o axé.')
    elif nascimento >= 1965:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o hip hop.')  
    elif nascimento >= 1955:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o sertanejo.')  
    elif nascimento >= 1945:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o pagode.')  
    elif nascimento >= 1935:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o rock.')  
    elif nascimento >= 1925:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o samba.')  
    elif nascimento >= 1915:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o gospel.')
    elif nascimento >= 1900:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o forró.')
    
    resoluNascimento = (2019 - nascimento)
    print('Hoje com os seus {} anos, os genêros mais populares atualmente no Brasil, segundo as pesquisas são: Funk, Forró, Gospel e Sertanejo.'.format(resoluNascimento))
    print('_'*140)
elif cadastro.lower() == 'nao' or cadastro.lower() == 'não':
    print('OK, Até a proxima!')
