from pytube import YouTube
import PySimpleGUI as sg
import telas as t


sg.theme('reddit')
while True:
    tela_entrada = t.Tela_login()
    event, values = tela_entrada.read()
    if event == 'baixar':
        print('obs')
        try:
            link = (values['link'])
            local = (values['local'])
            print (link)
            print (local)
            yt = YouTube(link)

            while True:
                print('fff')
                Tela_info = t.Tela_informações()
                eventos, valores = Tela_info.read()
                if eventos == 'cancelar':
                    Tela_info.close()
                    break
                    
                else:
                    Tela_info.close()
                    stream = yt.streams.get_by_itag(22)
                    stream.download(output_path=(local))
                    sg.popup('Download realizado com sucesso')
                    break
        except:
            sg.popup_error('ERRO! Vídeo não encontrado')
    else:
        print('Deu errado')
    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'sair') and sg.popup_yes_no('Tem certeza que deseja sair?') == 'Yes':
        break
    

tela_entrada.close()

# link = 'https://youtube.com/shorts/KdyRo7ZWXMw?feature=share'
# local = 'D:\\'
# yt = YouTube(link)
# print(yt.title)
# yt.streams.first().download(filename=('Video baixado'))