import threading
import time

def procesar(Dato):
    print("Arranca "+ Dato)
    time.sleep(5)
    print("Finalizo "+ Dato)

threading.Thread(target=procesar, args=('A')).start()
threading.Thread(target=procesar, args=('B')).start()
threading.Thread(target=procesar, args=('C')).start()

