from pytube import YouTube
import PySimpleGUI as sg
def Tela_login():
    layout = [  [sg.Text('Adicione o link do vídeo que deseja baixar')],
                [sg.InputText(k='link')],
                [sg.Text('O vídeo será salvo em:')],
                [sg.InputText("D:\\" , k='local')],
                [sg.Button('Baixar', k='baixar'), sg.Button('Sair', k='sair')]
            ]

    return sg.Window('Download Vídeo YouTube', layout) 


def Tela_informações():
    tela_entrada = Tela_login()
    event, values = tela_entrada.read()
    lk = (values['link'])
    you = YouTube(lk)
    layout = [ [sg.Text(f'Deseja baixar {you.title}')],
            [sg.Button('baixar', k='bx'), sg.Button('Sair', k='cancelar')]
        ]

    return sg.Window('Download Vídeo YouTube', layout) 