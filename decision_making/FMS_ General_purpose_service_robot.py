def q1():
    print("Q1: Se detecta obstáculo")
    while True:
        char = yield
        if char == 'a':
            yield from q1()
        elif char == 'b':
            yield from q2()
        else:
            break

def q2():
    print("Q2: No se detecta obstáculo")
    while True:
        char = yield
        if char == 'c':
            yield from q1()
        elif char == 'd':
            yield from q2()
        elif char == 'm':
            yield from q3()
        else:
            break

def q3():
    print("Q3: Quieto")
    while True:
        char = yield
        if char == 'e':
            yield from q3()
        elif char == 'f':
            yield from q4()
        else:
            break

def q4():
    print("Q4: Se recibe orden")
    while True:
        char = yield
        if char == 'g':
            yield from q3()
        elif char == 'h':
            yield from q5()
        else:
            break

def q5():
    print("Q5: Ejecutando orden")
    while True:
        char = yield
        if char == 'i':
            yield from q6()
        elif char == 'z':
            yield from q1()
        else:
            break

def q6():
    print("Q6: Finalizando orden")
    while True:
        char = yield
        if char == 'j':
            yield from q7()
        elif char == 'z':
            yield from q1()
        else:
            break

def q7():
    print("Q7: Punto de instrucción")
    while True:
        char = yield
        if char == 'z':
            yield from q1()
        elif char == 'k':
            yield from q4()
        elif char == 'l':
            yield from q3()
        else:
            break

def fsm():
    state = q1()
    next(state)
    while True:
        try:
            char = input("Presiona una tecla (a-l, z) o 'exit' para salir: ").lower()
            if char == 'exit':
                break
            state.send(char)
        except StopIteration:
            print("Estado no válido o final alcanzado.")
            break

if __name__ == "__main__":
    fsm()
