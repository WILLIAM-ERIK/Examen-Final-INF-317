import multiprocessing
from decimal import Decimal, getcontext

def calculate_pi(start, end):
    getcontext().prec = 1000  # Precisión de los cálculos
    pi = Decimal(0)

    for i in range(start, end):
        numerator = Decimal((-1) ** i)
        denominator = Decimal(2 * i + 1)
        pi += numerator / denominator

    return pi

if __name__ == '__main__':
    num_processes = multiprocessing.cpu_count()  # Número de procesadores disponibles
    num_terms = 1000000  # Número total de términos para calcular π
    chunk_size = num_terms // num_processes  # Tamaño de cada bloque para cada proceso

    pool = multiprocessing.Pool(processes=num_processes)
    results = pool.starmap(calculate_pi, [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_processes)])
    pool.close()
    pool.join()

    pi = sum(results) * 4
    print(f'Valor de pi: {pi}')
