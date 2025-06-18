# Máquina de estados para el reto 5: Restaurant

def q1():
    print("Q1: Mantenerse quieto (remaining_idle)")
    while True:
        char = yield
        if char == 'a':
            yield from q2()
        else:
            break

def q2():
    print("Q2: Observar clientes en la fila (watching_queue)")
    while True:
        char = yield
        if char == 'b':
            yield from q2()
        elif char == 'c':
            yield from q3()
        else:
            break

def q3():
    print("Q3: Navegar hacia la mesa del cliente (going_to_customer_table)")
    while True:
        char = yield
        if char == 'd':
            yield from q2()
        elif char == 'e':
            yield from q4()
        else:
            break

def q4():
    print("Q4: Tomar pedido (taking_order)")
    while True:
        char = yield
        if char == 'f':
            yield from q2()
        elif char == 'g':
            yield from q5()
        else:
            break

def q5():
    print("Q5: Confirmar pedido (confirming_order)")
    while True:
        char = yield
        if char == 'h':
            yield from q6()
        else:
            break

def q6():
    print("Q6: Ir a la cocina (returning_to_kitchen)")
    while True:
        char = yield
        if char == 'i':
            yield from q7()
        else:
            break

def q7():
    print("Q7: Recoger el pedido (picking_up_order)")
    while True:
        char = yield
        if char == 'j':
            yield from q8()
        else:
            break

def q8():
    print("Q8: Llevar pedido al cliente (delivering_order)")
    while True:
        char = yield
        if char == 'k':
            yield from q9()
        elif char == 'p':
            yield from q10()
        else:
            break

def q9():
    print("Q9: Finalizar turno (ending_shift)")
    while True:
        char = yield
        if char == 'n':
            yield from q2()
        else:
            break

def q10():
    print("Q10: Solicitar instrucciones humanas (requesting_instructions)")
    while True:
        char = yield
        if char == 'o':
            yield from q10()
        elif char == 'q':
            yield from q8()
        else:
            break

def q11():
    print("Q11: Gestionar obstáculos (handling_obstacle)")
    while True:
        char = yield
        if char == 'r':
            yield from q11()
        elif char == 's':
            yield from q10()
        elif char == 't':
            yield from q2()
        else:
            break

# Controlador principal FSM
def fsm():
    state = q1()
    next(state)
    while True:
        try:
            char = input("Presiona una tecla (a–t) o 'exit' para salir: ").lower()
            if char == 'exit':
                break
            state.send(char)
        except StopIteration:
            print("Estado no válido o final alcanzado.")
            break

if __name__ == "__main__":
    fsm()


# codigo h

state = "MOVE_TO_KITCHEN"

# Simulación de detección y ubicación de objetos
table_objects = ["tenedor", "cuchillo", "plato", "vaso1", "vaso2"]
dishwasher_tab = "pastilla"
wiping_object = "esponja"
start_position = "entrada"
person_position = "persona_juez"

while state != "END":
    match state:
        case "MOVE_TO_KITCHEN":
            print("Moviéndose a la cocina...")
            state = "DETECT_TABLE_OBJECTS"

        case "DETECT_TABLE_OBJECTS":
            print("Detectando objetos en la mesa...")
            print(f"Objetos detectados: {table_objects}")
            state = "OPEN_DISHWASHER"

        case "OPEN_DISHWASHER":
            print("Abriendo la puerta del lavavajillas...")
            print("Extrayendo bandeja si es necesario...")
            state = "PLACE_DISHES"

        case "PLACE_DISHES":
            for obj in table_objects:
                if obj in ["tenedor", "cuchillo", "plato"]:
                    print(f"Colocando {obj} en el lavavajillas.")
                else:
                    print(f"Colocando {obj} (vaso) en el basurero.")
            state = "INSERT_TAB"

        case "INSERT_TAB":
            print(f"Colocando la {dishwasher_tab} en su ranura.")
            state = "WIPE_TABLE"

        case "WIPE_TABLE":
            print(f"Usando {wiping_object} para limpiar el área donde estaba la bebida.")
            state = "RETURN_TO_START"

        case "RETURN_TO_START":
            print(f"Regresando a la posición inicial: {start_position}")
            state = "REPORT_TO_PERSON"

        case "REPORT_TO_PERSON":
            print(f"Dirigiéndose a {person_position} para reportar finalización.")
            print("Mesa limpiada. Todos los objetos fueron colocados correctamente.")
            state = "END"

print("Tarea finalizada.")
