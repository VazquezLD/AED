import random

jugadas = ('piedra', 'papel', 'tijera')

computadora = random.choice(jugadas)

jugador = (input('Ingrese piedra papel o tijeras: '))

if jugador == 'tijera' and computadora == 'papel':
    print('Ganaste! elegiste',jugador, 'y la computadora', computadora)

elif jugador == 'piedra' and computadora == 'tijera':
    print('Ganaste! elegiste',jugador, 'y la computadora', computadora)

elif jugador == 'papel' and computadora == 'piedra':
    print('Ganaste! elegiste',jugador, 'y la computadora', computadora)

elif jugador == computadora:
    print('Empate, ambos eligieron', jugador)

else:
    print('perdiste, la computadora eligio',computadora,'y vos elegiste', jugador)









