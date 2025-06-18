# State machine for Challenge 3: Guest Reception

def q1():
    print("Q1: Start from starting point (starting_point)")
    while True:
        char = yield
        if char == 'a':
            yield from q1()
        elif char == 'b':
            yield from q2()
        else:
            break

def q2():
    print("Q2: Detect guest appearance (guest_appeared)")
    while True:
        char = yield
        if char == 'c':
            yield from q3()
        else:
            break

def q3():
    print("Q3: Ask initial questions (asking_initial_questions)")
    while True:
        char = yield
        if char == 'd':
            yield from q4()
        else:
            break

def q4():
    print("Q4: Guide to drinks area (guiding_to_drinks_area)")
    while True:
        char = yield
        if char == 'e':
            yield from q5()
        elif char == 'f':
            yield from q11()
        elif char == 'g':
            yield from q12()
        else:
            break

def q5():
    print("Q5: Show available drinks (showing_drinks)")
    while True:
        char = yield
        if char == 'h':
            yield from q6()
        else:
            break

def q6():
    print("Q6: Identify chosen drink (identifying_drink)")
    while True:
        char = yield
        if char == 'i':
            yield from q7()
        elif char == 'j':
            yield from q12()
        else:
            break

def q7():
    print("Q7: Guide to the living room (guiding_to_living_room)")
    while True:
        char = yield
        if char == 'u':
            yield from q8()
        elif char == 'k':
            yield from q11()
        else:
            break

def q8():
    print("Q8: Indicate assigned seat (indicating_seat)")
    while True:
        char = yield
        if char == 'l':
            yield from q9()
        else:
            break

def q9():
    print("Q9: Introduce to other guests (introducing_guests)")
    while True:
        char = yield
        if char == 'm':
            yield from q10()
        else:
            break

def q10():
    print("Q10: Wait for next guest (waiting_next_guest)")
    while True:
        char = yield
        if char == 'n':
            yield from q2()
        elif char == 'w':
            yield from q10()
        else:
            break

def q11():
    print("Q11: Detect obstacle (detecting_obstacle)")
    while True:
        char = yield
        if char == 'p':
            yield from q4()
        elif char == 'q':
            yield from q7()
        elif char == 'o':
            yield from q11()
        else:
            break

def q12():
    print("Q12: Handle lost guest (handling_lost_guest)")
    while True:
        char = yield
        if char == 's':
            yield from q2()
        elif char == 'r':
            yield from q12()
        else:
            break

def fsm():
    state = q1()
    next(state)
    while True:
        try:
            char = input("Press a key (a–t) or 'exit' to quit: ").lower()
            if char == 'exit':
                break
            state.send(char)
        except StopIteration:
            print("Invalid state or final state reached.")
            break

if _name_ == "_main_":
    fsm()












#codigo h

# Estado inicial
state = "WAIT_FOR_GUEST"

# Contador de invitados y su información para el propio robot en caso de que pregunten 
guest_counter = 0
guest_data = []


# Posición inicial simulada (puede ser coordenadas, aquí solo como referencia textual)
start_position = "punto_de_inicio"

while state != "END":
    match state:
        case "WAIT_FOR_GUEST":
            #  Esperar la llegada de un nuevo invitado.
            # Detectar si alguien se aproxima o si la puerta se abre.
            # preparar algun sistema de respuesta para dar un paso
            print("Esperando al invitado...")
            state = "GREET_GUEST"

        case "GREET_GUEST":
            # Saludar al invitado, hacer contacto visual y dar la bienvenida a la casa.
            print("Saludando al invitado.")
            state = "ASK_INFO"

        case "ASK_INFO":
            # Preguntar por el nombre, bebida favorita o cosa de interes que quiera.
            # Aquí usar reconocimiento de voz o cara para poder guardar la informacion
            print("Pidiendo información del invitado.")
            guest_data.append({
                "name": f"Invitado_{guest_counter+1}",
                "drink": "jugo",  # simulado
                "interest": "música"  # simulado
            })
            state = "GUIDE_TO_BEVERAGE"

        case "GUIDE_TO_BEVERAGE":
            # Comentario: Guiar al invitado hacia la mesa de bebidas.
            print("Guiando al invitado a la mesa de bebidas.")
            state = "ASK_FOR_INTEREST"

        case "ASK_FOR_INTEREST":
            # Preguntar si es de su gusto las bebidas disponibles, en caso de que le pregunten debe decir que solo estan disponibles estas dispuestas
            print("Verificando el interés en la bebida.")
            state = "GUIDE_TO_LIVINGROOM"

        case "GUIDE_TO_LIVINGROOM":
            # Navegar hacia la sala de estar con la persona evadiendo en caso de haber obstaculos y en caso de, decirle a la persona que tenga cuidado
            print("Llevando al invitado a la sala de estar.")
            state = "SEAT_GUEST"

        case "SEAT_GUEST":
            # Asignar asiento disponible y registrar posición. en caso de que el invitado cambie de posicion que lo registre
            guest_counter += 1
            print(f"Invitado {guest_counter} sentado.")
            if guest_counter == 2:
                state = "INTRODUCE_GUESTS"
            else:
                state = "WAIT_FOR_GUEST"

        case "INTRODUCE_GUESTS":
            # Presentar a los dos invitados entre sí con nombre, bebida e intereses
            print("Presentando invitados:")
            for g in guest_data:
                print(f"- {g['name']}, le gusta el {g['drink']} y le interesa la {g['interest']}.")
            state = "END"

        case "RETURN_TO_START":
            # Regresar a la posición de inicio al finalizar la tarea para esperar a otro invitado
            print(f"Regresando a la posición inicial: {start_position}")
            state = "END"

print("Tarea completida y ya dejen de webear.")

