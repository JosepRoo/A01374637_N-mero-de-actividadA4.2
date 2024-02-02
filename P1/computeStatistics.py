"""Programa que procesa estadísticas de un archivo"""
import sys
import time

def main():
    """Función principal"""
    start_time = time.time()

    #Verificar que se haya proporcionado al menos un archivo
    if len(sys.argv) < 2:
        print("Uso: python computeStatistics.py archivoConDatos1.txt [archivoConDatos2.txt ...]")
        sys.exit(1)

    #Crear o abrir el archivo de salida 'StatisticsResults.txt'
    with open('StatisticsResults.txt', 'w', encoding="utf-8") as output_file:
        #Escribir el encabezado de la primera columna 'TC'
        output_file.write('TC')

        #Escribir los nombres de los archivos como encabezados de las columnas
        for filename in sys.argv[1:]:
            column_name = filename.replace('.txt', '')
            output_file.write(f'\t{column_name}')
        output_file.write('\n')

        #Inicializar listas para las estadísticas
        counts, means, medians = ['COUNT'], ['MEAN'], ['MEDIAN']
        modes, sds, variances =  ['MODE'], ['SD'], ['VARIANCE']

        #Procesar cada archivo y calcular estadísticas
        for filename in sys.argv[1:]:
            stats = process_file(filename)
            if stats:
                counts.append(str(len(stats['data'])))
                means.append(f"{stats['Mean']:.2f}")
                medians.append(f"{stats['Median']:.2f}")
                modes.append(f"{stats['Mode']}")
                sds.append(f"{stats['Standard Deviation']:.2f}")
                variances.append(f"{stats['Variance']:.2f}")
            else:
                #Si hubo un error, rellenar con 'N/A'
                counts.append('N/A')
                means.append('N/A')
                medians.append('N/A')
                modes.append('N/A')
                sds.append('N/A')
                variances.append('N/A')

        #Escribir las estadísticas en el archivo de salida
        output_file.write('\t'.join(counts) + '\n')
        output_file.write('\t'.join(means) + '\n')
        output_file.write('\t'.join(medians) + '\n')
        output_file.write('\t'.join(modes) + '\n')
        output_file.write('\t'.join(sds) + '\n')
        output_file.write('\t'.join(variances) + '\n')

    #Imprimir en consola el contenido del archivo de resultados
    with open('StatisticsResults.txt', 'r', encoding="utf-8") as result_file:
        print(result_file.read())

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTiempo total de ejecución: {elapsed_time:.2f} segundos")

    with open('StatisticsResults.txt', 'a',  encoding="utf-8") as output_file:
        output_file.write(f"\nTiempo total de ejecución: {elapsed_time:.2f} segundos")

def process_file(filename):
    """Función para procesar archivo"""
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            data = [float(line.strip()) for line in file if line.strip().isdigit()]
    except FileNotFoundError:
        print(f"Archivo {filename} no encontrado.")
        return None
    except ValueError:
        print(f"Dato inválido en el archivo {filename}.")
        return None

    #Calcular estadísticas
    statistics = {
        'data': data,
        'Mean': mean(data),
        'Median': median(data),
        'Mode': mode(data),
        'Variance': variance(data),
        'Standard Deviation': standard_deviation(data)
    }

    return statistics

def mean(data):
    """Función para calcular media"""
    return sum(data) / len(data) if data else 0

def median(data):
    """Función para calcular mediana"""
    data.sort()
    n = len(data)
    mid = n // 2
    return (data[mid] + data[~mid]) / 2 if n % 2 == 0 else data[mid]

def mode(data):
    """Función para calcular moda"""
    frequency = {x: data.count(x) for x in data}
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    return modes[0] if len(modes) == 1 else modes

def variance(data):
    """Función para calcular varianza"""
    mu = mean(data)
    return sum((x - mu) ** 2 for x in data) / (len(data) - 1) if data else 0

def standard_deviation(data):
    """Función para calcular desviación standard"""
    return variance(data) ** 0.5

if __name__ == "__main__":
    main()
