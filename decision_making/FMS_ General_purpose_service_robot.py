ef q1():
    print("Q1: Mantenerse quieto")
    while True:
        char = yield
        if char == 'a': 
            yield from q2()
        else:
            break

def q2():
    print("Q2: Recibir orden")
    while True:
        char = yield
        if char == 'b':  # Evento: Persona da orden
            yield from q3()
        else:
            break

def q3():
    print("Q3: Ejecutar orden")
    while True:
        char = yield
        if char == 'c':  # Evento: Orden recibida
            yield from q4()
        else:
            break

def q4():
    print("Q4: Finalizar orden")
    while True:
        char = yield
        if char == 'd':  # Evento: Navegación al punto de instrucción
            yield from q5()
        else:
            break

def q5():
    print("Q5: Llegar a instrucción")
    while True:
        char = yield
        if char == 'e':  # Evento: Punto de instrucción alcanzado
            yield from q6()
        elif char == 'f':  # Evento: Objeto detectado
            yield from q1()
        else:
            break

def q6():
    print("Q6: Detectar obstáculos")
    while True:
        char = yield
        if char == 'g':  # Evento: Objeto evadido
            yield from q5()
        else:
            break

def fsm():
    state = q1()
    next(state)
    while True:
        try:
            char = input("Presiona una tecla (a–g) o 'exit' para salir: ").lower()
            if char == 'exit':
                break
            state.send(char)
        except StopIteration:
            print("Estado no válido o final alcanzado.")
            break

if __name__ == "__main__":
    fsm()
