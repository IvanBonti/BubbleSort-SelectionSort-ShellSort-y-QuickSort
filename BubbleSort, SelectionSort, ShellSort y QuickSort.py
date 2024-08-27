import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns

# Implementación de los algoritmos de ordenamiento

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Función para medir tiempos de ejecución

def measure_time(sort_function, array):
    start_time = time.time()
    sort_function(array.copy())  # Usar copia para no alterar el array original
    end_time = time.time()
    return end_time - start_time

# Longitudes de los arreglos
sizes = [1024, 4096, 16384, 131072]

# Repeticiones
repetitions = 10

# Diccionario para almacenar los tiempos de cada algoritmo
timings = {
    'BubbleSort': {size: [] for size in sizes},
    'SelectionSort': {size: [] for size in sizes},
    'ShellSort': {size: [] for size in sizes},
    'QuickSort': {size: [] for size in sizes}
}

# Medir tiempos para cada tamaño de arreglo y cada algoritmo
for size in sizes:
    for _ in range(repetitions):
        array = np.random.randint(0, 1000000, size=size)
        
        timings['BubbleSort'][size].append(measure_time(bubble_sort, array))
        timings['SelectionSort'][size].append(measure_time(selection_sort, array))
        timings['ShellSort'][size].append(measure_time(shell_sort, array))
        timings['QuickSort'][size].append(measure_time(lambda x: quick_sort(x), array))

# Graficar los histogramas de los tiempos

plt.figure(figsize=(20, 15))
sns.set(style="whitegrid")

for i, size in enumerate(sizes):
    plt.subplot(2, 2, i + 1)
    plt.title(f"Sorting Times for Array of Size {size}")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency")
    sns.histplot(timings['BubbleSort'][size], kde=True, label='BubbleSort', color='blue')
    sns.histplot(timings['SelectionSort'][size], kde=True, label='SelectionSort', color='orange')
    sns.histplot(timings['ShellSort'][size], kde=True, label='ShellSort', color='green')
    sns.histplot(timings['QuickSort'][size], kde=True, label='QuickSort', color='red')
    plt.legend()

plt.tight_layout()
plt.show()
