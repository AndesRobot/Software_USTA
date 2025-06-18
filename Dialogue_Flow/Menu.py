def Help_me_carry():
    #Help me carry

def Help_me_carry_2():
    #Help Me Carry 2

def Receptionist():
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
            # Esperar la llegada de un nuevo invitado.
            # Detectar si alguien se aproxima.
            print("Esperando al invitado...")
            state = "GREET_GUEST"

        case "GREET_GUEST":
            # Saludar al invitado, hacer contacto visual y dar la bienvenida a la casa.
            print("Saludando al invitado.")
            state = "ASK_INFO"

        case "ASK_INFO":
            # Preguntar por el nombre, bebida favorita o cosa de interes que quiera.
            # Aquí usar asignación de ID para poder guardar la informacion
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

print("Tarea completada.")

def Storing_Groceries():
    #Storing Groceries

def Clean_the_Table():
    #Clean the Table

def Enhanced_General_Purpose_Service_Robot():
    #Enhanced General Purpose Service Robot

def Restaurant():
    #Restaurant

def Give_Me_a_Hand():
    #Give Me a Hand

def show_menu():
    print("\n=== MAIN MENU ===")
    print("1. Run Help_me_carry")
    print("2. Run Help_me_carry_2")
    print("3. Run Receptionist")
    print("4. Run Storing_Groceries")
    print("5. Run Clean_the_Table")
    print("6. Run Enhanced_General_Purpose_Service_Robot")
    print("7. Run Restaurant")
    print("8. Run Give_Me_a_Hand")
    print("0. Exit")

def main():
    while True:
        show_menu()
        choice = input("Select an option: ")

        match choice:
            case "1":
                Help_me_carry()
            case "2":
                Help_me_carry_2()
            case "3":
                Receptionist()
            case "4":
                Storing_Groceries()
            case "5":
                Clean_the_Table()
            case "6":
                Enhanced_General_Purpose_Service_Robot()
            case "7":
                Restaurant()
            case "8":
                Give_Me_a_Hand()
            case "0":
                print("👋 Exiting the program...")
                break
            case _:
                print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
