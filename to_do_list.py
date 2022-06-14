from PySimpleGUI import PySimpleGUI as sg

#Criando Layout
def criar_nova_tarefa():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout = linha, key = 'container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]
    
    return sg.Window('To Do List', layout = layout, finalize = True)

#Criar Janela
janela = criar_nova_tarefa()

#Criar regras dessa janela
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == 'Nova Tarefa':
        janela.extend_layout(janela['container'],[[sg.Checkbox(''), sg.Input('')]])
    elif eventos == 'Resetar':
        janela.close()
        janela = criar_nova_tarefa()
   
    
        
  
  
  
  
  
  
  
  
  
  
       