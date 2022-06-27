from multiprocessing import Event
import PySimpleGUI as sg

#aqui é a cor da janela
sg.theme("Green")

#aqui é o layout(caixas) da página, onde coloca os textos e botões
layout =[
        [sg.Text("Digite seu nome:"), sg.Input(key="-NAME-",do_not_clear=True,size=(20,1))],
        [sg.Text("Numero Documento:"), sg.Input(key="-PASSPORT_NUMBER-",do_not_clear=True,size=(10, 1))],
        [sg.Radio("Masculino", "RADIO", key='-MALE-'), sg.Radio("Feminino", "RADIO", key='-FEMALE-')],
        [sg.Input(key="-DEPARTURE-",size=(20)), sg.CalendarButton("Data de Saida", close_when_date_chosen=True,target="-DEPARTURE-", location=(0,0), no_titlebar=False)],
        [sg.Input(key="-ARRIVAL-",size=(20,1)), sg.CalendarButton("Data de Retorno", close_when_date_chosen=True,target="-ARRIVAL-", location=(0,0), no_titlebar=False)],
        [sg.Text("Escolha um destino:",size=(30, 1), font='Lucida', justification='left')],
        [sg.Listbox(values=['Sao Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Manaus', 'Rio Branco', 'Salvador', 'Brasilia', 'Fortaleza'], size=(40,5), select_mode='single', key='-DESTINATTION-')],
        [sg.Button("Reservar"), sg.Button("Visualizar Todos"),sg.Exit()]
]
        
# aqui é a janela
pysimplegui = sg.Window("Sistema de passagens", layout)

while True:
    event,values = pysimplegui.read()
    if event in (sg.WIN_CLOSED,'Exit'):
            break
    elif event == 'Reservar':
        sexo =""
        if values['-MALE-']:
                sexo='Masculino'
        else:
                sexo='Feminino'
        
        sg.popup("RESERVADO",values['-NAME-'], values['-DESTINATTION-'][0],sexo)


pysimplegui.close()
