import threading

def thread_function(name, start, end):
    for i in range(start, end + 1):
        print(f"{name}: {i}")

# Criando as threads
thread1 = threading.Thread(target=thread_function, args=("Thread 1", 1, 5))
thread2 = threading.Thread(target=thread_function, args=("Thread 2", 1, 5))

# Iniciando as threads
thread1.start()
thread2.start()

# Aguardando as threads terminarem
thread1.join()
thread2.join()

print("Programa encerrado.")