def q1():
    print("Q1: Remaining idle")
    while True:
        char = yield
        if char == 'a':
            yield from q2()
        elif char == 'n':
            yield from q6()
        else:
            break

def q2():
    print("Q2: Navigating to table")
    while True:
        char = yield
        if char == 'b':
            yield from q3()
        elif char == 'c':
            yield from q2()
        elif char == 'k':
            yield from q8()
        else:
            break

def q3():
    print("Q3: Selecting object")
    while True:
        char = yield
        if char == 'd':
            yield from q3()
        elif char == 'e':
            yield from q4()
        else:
            break

def q4():
    print("Q4: Transporting to storage")
    while True:
        char = yield
        if char == 'f':
            yield from q4()
        elif char == 'g':
            yield from q5()
        elif char == 'n':
            yield from q8()
        else:
            break

def q5():
    print("Q5: Storing object")
    while True:
        char = yield
        if char == 'o':
            yield from q7()
        else:
            break

def q6():
    print("Q6: Pouring cereal")
    while True:
        char = yield
        if char == 'j':
            yield from q7()
        else:
            break

def q7():
    print("Q7: Finishing task")
    while True:
        char = yield
        if char == 'i':
            yield from q1()
        else:
            break

def q8():
    print("Q8: Detecting obstacle")
    while True:
        char = yield
        if char == 'l':
            yield from q2()
        elif char == 'm':
            yield from q4()
        else:
            break

def fsm():
    state = q1()
    next(state)
    while True:
        try:
            char = input("Press a key (a–o) or 'exit' to quit: ").lower()
            if char == 'exit':
                break
            state.send(char)
        except StopIteration:
            print("Invalid state or end reached.")
            break

if __name__ == "__main__":
    fsm()










#codigo h

# Estado inicial
state = "MOVE_TO_TEST_LOCATION"

# Posiciones simuladas
start_position = "punto_de_inicio"
cabinet_position = "frente_al_gabinete"
table_position = "mesa_de_objetos"
person_position = "persona_juez"

# Lista de objetos detectados
detected_objects = []
cabinet = {}

while state != "END":
    match state:
        case "MOVE_TO_TEST_LOCATION":
            print("Moviéndose al área de prueba...")
            state = "DETECT_TABLE_OBJECTS"

        case "DETECT_TABLE_OBJECTS":
            print("Detectando objetos en la mesa...")
            detected_objects = ["manzana", "naranja", "plátano", "cereal_box"]
            state = "CLASSIFY_OBJECTS"

        case "CLASSIFY_OBJECTS":
            print("Clasificando objetos por similitud...")
            cabinet = {
                "frutas": ["manzana", "naranja", "plátano"],
                "cereales": ["cereal_box"]
            }
            state = "OPEN_CABINET_DOOR"

        case "OPEN_CABINET_DOOR":
            print("Intentando abrir la puerta del gabinete...")
            # Simulamos que el robot tiene exito al hacer su tarea de wea
            state = "STORE_OBJECTS"

        case "STORE_OBJECTS":
            for categoria, objetos in cabinet.items():
                for obj in objetos:
                    print(f"Moviendo {obj} al estante de {categoria}.")

        case "RETURN_TO_START":
            print(f"Regresando a la posición inicial: {start_position}")
            state = "REPORT_TO_PERSON"

        case "REPORT_TO_PERSON":
            # El robot navega por la sala para decir que su tarea fue hecha con exito informando al respecto
            print(f"Dirigiéndose a la persona en {person_position} para informar.")
            print("Tarea completada. Todos los objetos han sido almacenados correctamente.")
            state = "END"

print("Fin de la secuencia. Robot listo para nueva tarea.")

print("Tarea de almacenamiento completada correctamente.")

