target_number = int(input("Introduzca un número: "))

if target_number < 0:
    print("Por favor, ingrese un número no negativo.")
else:
    fibonacci_sequence = [0, 1]

    while target_number >= fibonacci_sequence[-1]:
        if target_number == fibonacci_sequence[-1]:
            print(f"El valor {target_number} es parte de la secuencia de Fibonacci.")
            break
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        if target_number < fibonacci_sequence[-1]:
            print(f"Hemos superado el límite indicado. {target_number} no es parte de la secuencia de Fibonacci.")
            break
