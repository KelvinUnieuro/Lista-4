import threading

# Variável global
global_var = 0

def thread_function():
    global global_var
    for _ in range(100):
        global_var += 1

# Criando as threads
thread1 = threading.Thread(target=thread_function)
thread2 = threading.Thread(target=thread_function)

# Iniciando as threads
thread1.start()
thread2.start()

# Aguardando as threads terminarem
thread1.join()
thread2.join()

print(f"Valor final da variável global: {global_var}")