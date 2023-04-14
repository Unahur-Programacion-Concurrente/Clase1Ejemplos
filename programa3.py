import time
import random
import threading

def procesar(Dato):
    print("Comenzando a procesar "+ Dato)
    time.sleep(5)
    print("Fin de procesamiendo de "+ Dato)

procesar('A')
threading.Thread(target=procesar, args=('B')).start()
procesar('C')
