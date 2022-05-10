import preguntas as p


def print_pregunta(enunciado, alternativas):
    print(f'{enunciado}\n')
    letras = ['A', 'B', 'C', 'D']
    for letra, alternativa in zip(letras, alternativas):
        print(f'{letra}. {alternativa[0]}')

        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4
