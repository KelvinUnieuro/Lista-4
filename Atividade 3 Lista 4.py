import threading
import queue
import random
import time

# Fila para armazenar os números aleatórios
num_queue = queue.Queue()

def producer_thread():
    while True:
        num = random.randint(1, 100)
        num_queue.put(num)
        print(f"Produzido: {num}")
        time.sleep(1)

def consumer_thread():
    while True:
        num = num_queue.get()
        print(f"Consumido: {num}")
        time.sleep(2)

# Criando e iniciando as threads
producer = threading.Thread(target=producer_thread)
consumer = threading.Thread(target=consumer_thread)

producer.start()
consumer.start()