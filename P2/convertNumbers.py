"""Programa que procesa y convierte números a otro sistema"""
import sys
import time

def main():
    """Función principal"""
    # Iniciar el temporizador
    start_time = time.time()

    if len(sys.argv) < 2:
        print("Uso: python convertNumbers.py fileWithData1.txt [fileWithData2.txt ...]")
        sys.exit(1)

    output_filename = 'ConversionResults.txt'

    with open(output_filename, 'w',  encoding="utf-8") as output_file:
        for filename in sys.argv[1:]:
            # Escribir el nombre del archivo (sin extensión .txt) como encabezado
            output_file.write(f"NUMBER\t{filename.replace('.txt', '')}\tBIN\tHEX\n")
            try:
                with open(filename, 'r',  encoding="utf-8") as file:
                    for line_number, line in enumerate(file, start=1):
                        try:
                            # Eliminar espacios y convertir a entero
                            number = int(line.strip())
                            # Convertir a binario y hexadecimal
                            binary = to_binary(number)
                            hexa = to_hex(number)
                            # Escribir en el archivo de salida y en la pantalla
                            output_line = f"{line_number}\t{number}\t{binary}\t{hexa}\n"
                            print(output_line, end='')
                            output_file.write(output_line)
                        except ValueError:
                            print(f"Dato inválido en {line_number}: {line}")
            except FileNotFoundError:
                print(f"Archivo {filename} no encontrado.")
            # Espacio entre resultados de diferentes archivos
            output_file.write("\n")

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Escribir y mostrar el tiempo total de ejecución
    execution_time_line = f"\nTiempo total de ejecución: {elapsed_time:.2f} segundos\n"
    print(execution_time_line)
    with open(output_filename, 'a',  encoding="utf-8") as output_file:
        output_file.write(execution_time_line)

def to_binary(number):
    """Función para convertir a binario"""
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary or '0'

def to_hex(number):
    """Función para convertir a hexadecimal"""
    hex_chars = '0123456789ABCDEF'
    hexa = ''
    while number > 0:
        hexa = hex_chars[number % 16] + hexa
        number = number // 16
    return hexa or '0'

if __name__ == "__main__":
    main()
