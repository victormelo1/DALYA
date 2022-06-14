from PySimpleGUI import PySimpleGUI as sg

lista = []
file = open("arquivo.txt", "r")
ler = file.read()
lista = ler.split()


print("[0] Coordenadores\n[1] Voluntarios")
resposta = int(input("Insira uma opção:"))

if resposta == 0: # abrir interface(netflix) dos coordenadores!
    sg.theme('DarkBlue4')
    layout = [
    [sg.Text('Usuario'), sg.Input(key = 'Usuario', size = (50, 100))],
    [sg.Text('Senha'), sg.Input(key = 'Senha', password_char = '*', 
    size = (50, 100))],
    [sg.Button('Entrar')]
    ]
#Janela
    janela = sg.Window('Bem-Vindo Coordenador(a)', layout)

#Ler eventos
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Entrar':
            for i in range(1):
                i = 0
                if valores['Usuario'] == lista[i] and valores['Senha'] == lista[i+1]:
                    print('Bem-vindo a Sou Grato!')
                elif valores['Usuario'] == lista[i+2] and valores['Senha'] == lista[i+3]:
                    print('Bem-vindo a Sou Grato!')
                elif valores['Usuario'] == lista[i+4] and valores['Senha'] == lista[i+5]:
                    print('Bem-vindo a Sou Grato!')
                elif valores['Usuario'] == lista[i+6] and valores['Senha'] == lista[i+7]:
                    print('Bem-vindo a Sou Grato!')
                elif valores['Usuario'] == lista[i+8] and valores['Senha'] == lista[i+9]:
                    print('Bem-vindo a Sou Grato!')
                elif valores['Usuario'] == lista[i+10] and valores['Senha'] == lista[i+11]:
                    print('Bem-vindo a Sou Grato!')
                elif valores['Usuario'] == lista[i+12] and valores['Senha'] == lista[i+13]:
                    print('Bem-vindo a Sou Grato!')
                else:
                    print("Usuario ou senha incorreto!")
    
elif resposta == 1: # abrir interface(netflix) dos coordenadores!
    sg.theme('DarkBlue4')
    layout = [
    [sg.Text('Usuario'), sg.Input(key = 'Usuario', size = (25, 1))],
    [sg.Text('Senha'), sg.Input(key = 'Senha', password_char = '*', 
    size = (25, 1))],
    [sg.Button('Entrar')]
    ]   
#Janela
    janela = sg.Window('Bem-Vindo Voluntario(a)', layout)

#Ler eventos
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Entrar':
            if valores['Usuario'] == 'Victor' and valores['Senha'] == '123':
                print('Bem-vindo a Sou Grato!')
                
                
                
                
                