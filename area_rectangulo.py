'''operadorA = 3
operadorB = 5
suma = operadorA + operadorA
print(f"El resultado de la suma es:  {suma}")
'''
#Calcular el area y el perimetro de un rectangulo

'''
alto = 10
ancho = 10
triangulo = alto * ancho 
print(f"El area del triangulo es: {triangulo} " )
'''



altoArea = int(input("Escribe la altura del rectangulo:  "))
anchoArea = int(input("Escribe el ancho del rectangulo:  "))
areaRectangulo = altoArea * anchoArea
perimetroRectangulo = (altoArea + anchoArea) * 2
print(f"El resultado del area del rectangulo es: {areaRectangulo}")
print(f"El resultado del perimetro del rectangulo es: {perimetroRectangulo}")


import sys, math

def hash_fraction(m, n):
    """Compute the hash of a rational number m / n.

    Assumes m and n are integers, with n positive.
    Equivalent to hash(fractions.Fraction(m, n)).

    """
    P = sys.hash_info.modulus
    # Remove common factors of P.  (Unnecessary if m and n already coprime.)
    while m % P == n % P == 0:
        m, n = m // P, n // P

    if n % P == 0:
        hash_value = sys.hash_info.inf
    else:
        # Fermat's Little Theorem: pow(n, P-1, P) is 1, so
        # pow(n, P-2, P) gives the inverse of n modulo P.
        hash_value = (abs(m) % P) * pow(n, P - 2, P) % P
    if m < 0:
        hash_value = -hash_value
    if hash_value == -1:
        hash_value = -2
    return hash_value

def hash_float(x):
    """Compute the hash of a float x."""

    if math.isnan(x):
        return object.__hash__(x)
    elif math.isinf(x):
        return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
    else:
        return hash_fraction(*x.as_integer_ratio())

def hash_complex(z):
    """Compute the hash of a complex number z."""

    hash_value = hash_float(z.real) + sys.hash_info.imag * hash_float(z.imag)
    # do a signed reduction modulo 2**sys.hash_info.width
    M = 2**(sys.hash_info.width - 1)
    hash_value = (hash_value & (M - 1)) - (hash_value & M)
    if hash_value == -1:
        hash_value = -2
    return hash_value














