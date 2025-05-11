def is_prime(n):
    if n < 0:
        return "Os números negativos non están permitidos"  # Mensaje para números negativos
    if n <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Si es divisible por cualquier número, no es primo
    return True  # Si no es divisible por ninguno, es primo


def cubic(n):
    return n**3  # Retorna el cubo de n


def say_hello(name):
    return f"Ola, {name}"  # Devuelve un saludo con el nombre
