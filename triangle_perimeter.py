def triangle_perimeter(a, b, c):
    """
    Calcola il perimetro di un triangolo dati i tre lati.

    Args:
        a (float): Lunghezza del primo lato.
        b (float): Lunghezza del secondo lato.
        c (float): Lunghezza del terzo lato.

    Returns:
        float: Il perimetro del triangolo.

    Raises:
        ValueError: Se uno dei lati è <= 0 o se i lati non formano un triangolo valido.
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("I lati del triangolo devono essere maggiori di zero.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("I lati forniti non formano un triangolo valido.")
    return a + b + c


if __name__ == "__main__":
    # Esempi di utilizzo
    print(triangle_perimeter(3, 4, 5))   # 12
    print(triangle_perimeter(5, 5, 5))   # 15 (triangolo equilatero)
    print(triangle_perimeter(6, 8, 10))  # 24
