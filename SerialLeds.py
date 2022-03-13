import pyfirmata
import time
board = pyfirmata.Arduino('COM3')

while True:
    #Leds Rojos
    board.digital[5].write(1)
    board.digital[8].write(1)
    time.sleep(.4)
    board.digital[5].write(0)
    board.digital[8].write(0)

    #Leds Verdes
    board.digital[9].write(1)
    board.digital[6].write(1)
    time.sleep(.4)
    board.digital[9].write(0)
    board.digital[6].write(0)

    #Leds Amarillos
    board.digital[10].write(1)
    board.digital[7].write(1)
    time.sleep(.4)
    board.digital[10].write(0)
    board.digital[7].write(0)
