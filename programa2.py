import time
import random
def procesar(Dato):
    print("Comenzando a procesar "+ Dato)
    time.sleep(random.randint(0,5))
    print("Fin de procesamiendo de "+ Dato)

procesar('A')
procesar('B')
procesar('C')

