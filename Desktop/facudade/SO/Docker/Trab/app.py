import threading
import random
import time

# Função para verificar se um número é primo
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Função que cada thread executará
def check_primes(thread_id):
    start = random.randint(1, 50000)  
    end = random.randint(start, start + random.randint(10000, 50000))  # Definindo intervalos aleatórios
    numbers = random.sample(range(start, end), 500)  # 500 números aleatórios dentro do intervalo

    print(f"* Thread {thread_id} iniciando | Intervalo: {start}-{end} | Analisando {len(numbers)} números.")

    start_time = time.time()
    primes = [n for n in numbers if is_prime(n)]
    execution_time = time.time() - start_time

    sleep_time = random.uniform(0.5, 3.0)  # Simula carga aleatória
    time.sleep(sleep_time)

    print(f"# Thread {thread_id} finalizou em {execution_time:.2f}s (+ {sleep_time:.2f}s de delay) | {len(primes)} números primos encontrados.")
    print(f"@ Thread {thread_id} Primos: {primes}\n")

# Criando e iniciando múltiplas threads
NUM_THREADS = 6  # Número de threads a serem criadas
threads = []

print(" Iniciando processamento com threads...\n")
for i in range(NUM_THREADS):
    thread = threading.Thread(target=check_primes, args=(i,))
    threads.append(thread)
    thread.start()

# Aguardar todas as threads finalizarem
for thread in threads:
    thread.join()

print("\n Todos os cálculos foram finalizados!")
