def choose_level(n_pregunta, p_level):
    if n_pregunta <= p_level:
        level = 'basicas'
    elif n_pregunta <= 2 * p_level:
        level = 'intermedias'
    else:
        level = 'avanzadas'
    return level


if __name__ == '__main__':
    # verificar resultados
    print(choose_level(1, 1))  # básicas
    print(choose_level(2, 1))  # intermedias
    print(choose_level(3, 1))  # avanzadas
    print(choose_level(4, 2))
    print(choose_level(5, 2))
    print(choose_level(6, 2))
    print(choose_level(7, 3))
