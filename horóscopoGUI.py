import PySimpleGUI as psg

def consultar_signo(dia, mes):
    if (dia >= 20 and dia <= 31 and mes == 3) or (dia >= 1 and dia <= 19 and  mes == 4):
        return 'Áries'
    elif (dia >= 20 and dia <= 30 and mes == 4) or (dia >= 1 and dia <= 20 and mes == 5):
        return 'Touro'
    elif (dia >= 21 and dia <= 31 and mes == 5) or (dia >= 1 and dia <= 20 and mes == 6):
        return 'Gêmeos'
    elif (dia >= 22 and dia <= 30 and mes == 6) or (dia >= 1 and dia <= 22 and mes == 7):
        return 'Câncer'
    elif (dia >= 23 and dia <= 31 and mes == 7) or (dia >= 1 and dia <= 22 and mes == 8):
        return 'Leão'
    elif (dia >= 23 and dia <= 31 and mes == 8) or (dia >= 1 and dia <= 22 and mes == 9):
        return 'Virgem'
    elif (dia >= 23 and dia <= 30 and mes == 9) or (dia >= 1 and dia <= 22 and mes == 10):
        return 'Libra'
    elif (dia >= 23 and dia <= 31 and mes == 10) or (dia >= 1 and dia <= 21 and mes == 11):
        return 'Escorpião'
    elif (dia >= 22 and dia <= 30 and mes == 11) or (dia >= 1 and dia <= 21 and mes == 12):
        return 'Sagitário'
    elif (dia >= 22 and dia <= 31 and mes == 12) or (dia >= 1 and dia <= 19 and mes == 1):
        return 'Capricórnio'
    elif (dia >= 20 and dia <= 31 and mes == 1) or (dia >= 1 and dia <= 18 and mes == 2):
        return 'Aquário'
    elif (dia >= 19 and dia <= 29 and mes == 2) or (dia >= 1 and dia <= 20 and mes == 3):
        return 'Peixes'
    else:
        return 'Inválido'

layout = [
    [psg.Text('Consultar Signo')],
    [psg.Text('Informe o Dia:'), psg.InputText(key='dia')],
    [psg.Text('Informe o Mês:'), psg.InputText(key='mes')],
    [psg.Button('Consultar'), psg.Button('Limpar'), psg.Button('Sair', button_color=('white', 'red'))],
    [psg.Text('', size=(20, 1), key='resultado')],
]

janela = psg.Window('Consulta de Signo', layout)

while True:
    evento, valores = janela.read()

    if evento == psg.WIN_CLOSED or evento == 'Sair':
        break
    elif evento == 'Consultar':
        try:
            dia = int(valores['dia'].strip())
            mes = int(valores['mes'].strip())
            resultado = consultar_signo(dia, mes)
            janela['resultado'].update(f'Signo: {resultado}')
        except ValueError:
            psg.popup_error('Informe valores numéricos para Dia e Mês.')
    elif evento == 'Limpar':
        janela['dia'].update('')
        janela['mes'].update('')
        janela['resultado'].update('')
        janela['dia'].set_focus()

janela.close()
