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
                print("Clasificando objetos por grupos...")
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
                #if almaceno todos dice esto
                print("Tarea completada. Todos los objetos han sido almacenados correctamente.")
                ##else if almaceno # cantidad de objetos
                print("Tarea incompleta. # cantidad de objetos han sido almacenados correctamente.")
                state = "END"
    
    print("Tarea de almacenamiento completada correctamente.")

def Clean_the_Table():
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

def Enhanced_General_Purpose_Service_Robot():
    print("Robot: Hola, estoy listo para ayudarte. Por favor, dime qué necesitas.")
    
    entrada_usuario = "Tengo sed"
    print(f"Usuario: {entrada_usuario}")
    
    if "hambre" in entrada_usuario.lower():
        necesidad = "snack"
        accion = "llevar comida"
    elif "frío" in entrada_usuario.lower():
        necesidad = "manta"
        accion = "llevar manta"
    elif "sed" in entrada_usuario.lower():
        necesidad = "botella"
        accion = "llevar bebida"
    else:
        print("Error: No se pudo interpretar la intención del usuario.")
        print("Robot: Lo siento, ¿podrías repetir lo que necesitas?")
        return

    print(f"Razonamiento: necesidad detectada = {necesidad}, acción = {accion}")
    print("Navegación: dirigiéndose al lugar donde podría estar el objeto...")

    objetos_detectados = ["manta", "snack", "botella"]
    print(f"Detección de objetos: elementos encontrados = {objetos_detectados}")
    
    if necesidad in objetos_detectados:
        print(f"Objeto encontrado: {necesidad}")
        print(f"Brazo robótico: tomando el objeto {necesidad}")
        print("Navegación: regresando con el operador...")
        print(f"Entrega: {necesidad} entregado al operador")
        print("Robot: Aquí tienes, avísame si necesitas algo más.")
    else:
        print("Error: El objeto necesario no se encuentra disponible.")
        print("Robot: No pude encontrar lo que necesitas, ¿quieres que lo intente de nuevo?")
    
    print("Tarea completada: Robot de servicio general finalizado\n")

def Restaurant():
    print("Robot: Bienvenido al restaurante, ¿qué deseas ordenar?")
    
    entrada_cliente = "Quisiera jugo de naranja"
    print(f"Cliente: {entrada_cliente}")
    
    menu_disponible = ["soda", "jugo de naranja", "agua"]
    pedido = "jugo de naranja"
    
    if pedido not in menu_disponible:
        print(f"Error: {pedido} no está en el menú.")
        print("Robot: Lo siento, ese producto no está disponible. Por favor, elige otro.")
        return

    print(f"Pedido recibido: {pedido}")
    print("Navegación: yendo a la cocina...")

    objetos_en_cocina = ["jugo de naranja", "jugo de manzana", "soda"]
    print(f"Objetos detectados en cocina: {objetos_en_cocina}")
    
    if pedido in objetos_en_cocina:
        print(f"Producto encontrado: {pedido}")
        print("Brazo robótico: tomando el producto...")
        print("Navegación: volviendo con el cliente...")
        print(f"Entrega: {pedido} entregado correctamente.")
        print("Robot: Aquí tienes tu jugo de naranja, que lo disfrutes.")
    else:
        print("Error: No se encontró el objeto solicitado.")
        print("Robot: No pude localizar el producto, inténtalo de nuevo más tarde.")
    
    print("Tarea completada: Escenario restaurante finalizado\n")

def Give_Me_a_Hand():
    print("Robot: Estoy listo para ayudarte, dime qué objeto necesitas que traiga.")
    
    solicitudes = ["control remoto", "libro", "vaso"]
    ubicaciones = {"control remoto": "sala", "libro": "dormitorio", "vaso": "cocina"}
    objetos_disponibles = {
        "sala": ["control remoto", "cojín"],
        "dormitorio": ["libro", "lámpara"],
        "cocina": ["vaso", "plato"]
    }

    for objeto in solicitudes:
        print(f"\nUsuario: Por favor, tráeme el {objeto}")
        ubicacion = ubicaciones.get(objeto)
        
        if not ubicacion:
            print(f"Error: No se conoce la ubicación del objeto {objeto}")
            print("Robot: Lo siento, no estoy entrenado para buscar ese objeto.")
            continue

        print(f"Navegación: yendo a la {ubicacion} para buscar el {objeto}")
        encontrados = objetos_disponibles.get(ubicacion, [])
        print(f"Escaneo en {ubicacion}: objetos vistos = {encontrados}")
        
        if objeto in encontrados:
            print(f"Objeto encontrado: {objeto}")
            print("Brazo robótico: recogiendo el objeto...")
            print("Navegación: regresando con el operador...")
            print(f"Entrega: {objeto} entregado correctamente")
            print(f"Robot: Aquí tienes el {objeto}")
        else:
            print(f"Error: No encontré el {objeto} en la {ubicacion}")
            print("Robot: No pude encontrarlo, ¿deseas que intente con otro?")
    
    print("\nRobot: ¿Necesitas algo más?")
    print("Usuario: No, gracias.")
    print("Tarea completada: Dame una mano finalizado\n")

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
