import threading
import time
import random

def thread_function(thread_num):
    sleep_time = random.randint(1, 5)  # Tempo de espera aleatório entre 1 e 5 segundos
    print(f"Thread {thread_num} iniciou. Esperando {sleep_time} segundos.")
    time.sleep(sleep_time)
    print(f"Thread {thread_num} terminou.")

# Criando as cinco threads
threads = []
for i in range(5):
    thread = threading.Thread(target=thread_function, args=(i+1,))
    threads.append(thread)
    thread.start()

# Aguardando as threads terminarem
for thread in threads:
    thread.join()

print("Todas as threads terminaram.")