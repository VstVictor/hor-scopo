#horóscopo simples

print('\n\t\t\t--Consultar Signo--\n\t')

dia = int(input('Informe o Dia: ').strip())
mes = int(input('Informe o mês: ').strip())

if (dia >= 20 and dia <= 31 and mes == 3) or (dia >= 1 and dia <= 19 and  mes == 4):
   print('Signo: Áries')
elif (dia >= 20 and dia <= 30 and mes == 4) or (dia >= 1 and dia <= 20 and mes == 5):
   print('Signo: Touro')
elif (dia >= 21 and dia <= 31 and mes == 5) or (dia >= 1 and dia <= 20 and mes == 6):
   print('Signo: Gêmeos')
elif (dia >= 22 and dia <= 30 and mes == 6) or (dia >= 1 and dia <= 22 and mes == 7):
   print('Signo: Câncer')
elif (dia >= 23 and dia <= 31 and mes == 7) or (dia >= 1 and dia <= 22 and mes == 8):
   print('Signo: Leão')
elif (dia >= 23 and dia <= 31 and mes == 8) or (dia >= 1 and dia <= 22 and mes == 9):
   print('Signo: Virgem')
elif (dia >= 23 and dia <= 30 and mes == 9) or (dia >= 1 and dia <= 22 and mes == 10):
   print('Signo: Libra')
elif (dia >= 23 and dia <= 31 and mes == 10) or (dia >= 1 and dia <= 21 and mes == 11):
   print('Signo: Escorpião')
elif (dia >= 22 and dia <= 30 and mes == 11) or (dia >= 1 and dia <= 21 and mes == 12):
   print('Signo: Sagitário')
elif (dia >= 22 and dia <= 31 and mes == 12) or (dia >= 1 and dia <= 19 and mes == 1):
   print('Signo: Capricórnio')
elif (dia >= 20 and dia <= 31 and mes == 1) or (dia >= 1 and dia <= 18 and mes == 2):
   print('Signo: Aquário')
elif (dia >= 19 and dia <= 29 and mes == 2) or (dia >= 1 and dia <= 20 and mes == 3):
   print('Signo: Peixes')
else:
   print('Inválido')