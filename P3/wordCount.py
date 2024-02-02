"""Programa que cuanta cuantas veces aparece una palabra en un archivo de texto"""
import sys
import time

def main():
    """Función principal"""
    # Iniciar el temporizador
    start_time = time.time()

    # Revisar si se ha dado el nombre del archivo como argumento
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    file_label = filename.replace('.txt', '')  # Remover la extensión '.txt' para el encabezado
    output_filename = 'WordCountResults.txt'

    try:
        with open(filename, 'r', encoding="utf-8") as file:
            word_counts = count_words(file)

            # Escribir los encabezados y los resultados en la pantalla y en el archivo
            with open(output_filename, 'w', encoding="utf-8") as output_file:
                header = f"Row Labels\tCount of {file_label}\n"
                print(header, end='')
                output_file.write(header)

                for word, count in word_counts.items():
                    line = f"{word}\t{count}\n"
                    print(line, end='')
                    output_file.write(line)
    except FileNotFoundError:
        print(f"Archivo {filename} no encontrado.")
        sys.exit(1)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Escribir y mostrar el tiempo total de ejecución
    execution_time_line = f"\nTiempo total de ejecución: {elapsed_time:.2f} segundos\n"
    print(execution_time_line)
    with open(output_filename, 'a', encoding="utf-8") as output_file:
        output_file.write(execution_time_line)

def count_words(file):
    """Función para contar cuantas veces aparece la palabra"""
    word_counts = {}
    for line in file:
        # Separar las palabras por espacios
        words = line.strip().split()
        for word in words:
            # Contar cada palabra
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    return word_counts

if __name__ == "__main__":
    main()
