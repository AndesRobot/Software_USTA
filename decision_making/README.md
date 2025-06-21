# Robot Decision Making Documentation

## Overview

**Decision Making System:**
- Responsible for robot decision-making processes
- Implemented through state machines (one per challenge)
- Corresponds to the skeleton of the robot's logical operation
- Integrates all other functions
- Already coded in Python

---

## Challenge 1: Help Me Carry

### State Definitions

|Estado	|Nombre	             |   Español	                                                            |     Ingles|
|-------|--------------------|------------------------------------------------------------------------|-----------------------------------------------------------|
|Q1	  |  waiting_person	     |   Estoy esperando a que se acerque una persona.	     |                   I am waiting for someone to approach.|
|Q2	  |  notifiying_reading	  |  Estoy listo para seguirte. Por favor, comienza a caminar cuando quieras.	|I’m ready to follow you. Please start walking when you're ready.|
|Q3	  |  following_person	  |  Siguiendo a la persona.	|Following the person..|
|Q4	  |  detecting_indication|	Me detuve. Esperando una indicación para continuar.	                    |I’ve stopped. Waiting for an indication to continue.|
|Q5	  |  recognition_bag	   |    Buscando la bolsa |	Searching for the  bag.|
|Q6	  |  navegation_to_bag	  |  Dirigiéndome hacia la bolsa seleccionada.	                        |    Navigating to the selected bag.|
|Q7	  |  picking_up_bag	     |   Recogiendo la bolsa con cuidado. Por favor, aléjate un poco.	      |  Picking up the bag carefully. Please stand back slightly.|
|Q8	  |  homing	              |  Regresando al punto de inicio con la bolsa.	                      |  Returning to the starting point with the bag.|
|Q9	  |  detecting_obstacles	|    Obstáculo detectado. Buscando nueva ruta.	                         |   Obstacle detected. Searching for an alternate path.|
|Q10	  |  delivering_bag	      |  Entregando la bolsa en la zona indicada.	                          |  Delivering the bag to the designated area.|
|Q11	  |  queuing	             |   Me estoy uniendo a la fila para regresar. Manteniendo distancia social.|	Joining the queue to return. Maintaining social distance.|


### Events

| Event | Description |
|-------|-------------|
| a | Persona no identificada |
| b | Persona identificada |
| c | La persona no esta al frente |
| d | Persona da orden |
| e | La persona no está al frente |
| f | Persona camina |
| g | Persona detenida |
| h | Persona camina |
| i | Indicación recibida |
| j | Bolsa no detectada |
| k | Bolsa detectada |
| l | Bolsa al alcance |
| m | Bolsa asegurada |
| n | Se llego a Home |
| o | Obstáculo detectado |
| p | Obstáculo evadido |
| q | Bolsa entregada |
| r | Primero en la fila |

### State Functions Required

| State | English Description | Required Functions |
|-------|--------------------|--------------------|
| Q1 | Wait for person | pose_estimation, object_detection, speech_recognition |
| Q2 | Indicate readiness | t2s, button |
| Q3 | Follow person | pose_estimation, speech_recognition, path_planning |
| Q4 | Wait for stopped person / Detect indication | pose_estimation, speech_recognition, path_planning |
| Q5 | Detect bag | object_detection, object_recognition |
| Q6 | Navigate to bag | path_planning, mapping, mobility_control |
| Q7 | Pick up bag | armcontrol, object_detection, pose_estimation |
| Q8 | Move to home | mobility_control, path_planning |
| Q9 | Detect obstacles | object_detection, mobility_control |
| Q10 | Deliver bag | armcontrol, pose_estimation, object_detection |
| Q11 | Queue up | speech_recognition, t2s, mobility_control |

---

## Challenge 2: General_purpose_service_robot

### State Definitions

|Estado	|	Nombres |	Español	 | Ingles |
|--|--------|----------|---------|
|Q1	 |	remaining_idle|	Estoy esperando instrucciones.|	I am waiting for instructions.|
|Q2|	receiving_command|	Por favor, dime qué tarea debo realizar.|	Por favor, dime qué tarea debo realizar.|
|Q3	|	executing_command	|Ejecutando la orden recibida. Por favor, mantente atento.	|Executing the received command. Please stay alert.|
|Q4|	finishing_command|	He terminado la orden. ¿Necesitas algo más?|	I have finished the command. Do you need anything else?|
|Q5|	reaching_instruction|	Estoy llegando al punto de instrucción.	|I am approaching the instruction point.|
|Q6|	detecting_obstacles|	Hay un obstáculo en mi camino. Buscando ruta alternativa.	|There is an obstacle in my path. Looking for an alternate route.|



### Events

| Event | Description |
|-------|-------------|
| a | Puertas abiertas |
| b | Persona da orden |
| c | Orden recibida |
| d | Navegacion al punto de instrucción |
| e | Punto de instrucción alcanzado |
| f | Objeto detectado en trayecto |
| g | Objeto evadido |

### State Functions Required

| State | English Description | Required Functions |
|-------|--------------------|--------------------|
| Q1 | Remain idle | t2s, speech_recognition |
| Q2 | Receive command | speech_recognition, t2s |
| Q3 | Execute command | mobility_control, path_planning, object_detection, armcontrol |
| Q4 | Complete command | t2s |
| Q5 | Reach instruction point | mobility_control, path_planning |
| Q6 | Detect obstacles | object_detection, mobility_control, pose_estimation |

---

## Challenge 3: Receptionist

### State Definitions

| State | Description (Spanish) | Technical Name |
|-------|----------------------|----------------|
| Q1 | Iniciar desde el punto de inicio | starting_point |
| Q2 | Detectar aparición de invitado | guest_appeared |
| Q3 | Realizar preguntas iniciales | asking_initial_questions |
| Q4 | Guiar hacia el área de bebidas | guiding_to_drinks_area |
| Q5 | Mostrar bebidas disponibles | showing_drinks |
| Q6 | Identificar bebida elegida | identifying_drink |
| Q7 | Guiar a la sala de estar | guiding_to_living_room |
| Q8 | Indicar asiento asignado | indicating_seat |
| Q9 | Presentar al resto de invitados | introducing_guests |
| Q10 | Esperar al siguiente invitado | waiting_next_guest |
| Q11 | Detectar obstáculo | detecting_obstacle |
| Q12 | Confirmar ausencia de obstáculos | no_obstacle_detected |
| Q13 | Manejar invitado perdido | handling_lost_guest |

### Events

| Event | Description |
|-------|-------------|
| a | Sistema listo / punto de inicio |
| b | Invitado detectado |
| c | Se completan preguntas iniciales |
| d | Confirmación para guiar al área de bebidas |
| e | Área de bebidas alcanzada |
| f | Bebida identificada |
| g | Confirmación para ir a la sala de estar |
| h | Invitado ubicado en sala de estar |
| i | Asiento identificado |
| j | Presentación completada |
| k | Invitado se pierde antes de llegar |
| l | Invitado se pierde en trayecto |
| m | Invitado no responde |
| n | Obstáculo detectado |
| o | Obstáculo evadido |
| p | Trayectoria despejada |
| q | Invitado reencontrado |
| r | Reinicio por error |
| s | Interrupción inesperada |
| t | Retorno al punto de inicio |

### State Functions Required

| State | English Description | Required Functions |
|-------|--------------------|--------------------|
| Q1 | Start from starting point | mobility_control |
| Q2 | Detect guest appearance | object_detection, pose_estimation, face_recognition |
| Q3 | Ask initial questions | speech_recognition, t2s |
| Q4 | Guide to the beverage area | path_planning, mobility_control |
| Q5 | Show available drinks | t2s, object_recognition |
| Q6 | Identify selected drink | object_detection, object_recognition, pose_estimation |
| Q7 | Guide to the living room | path_planning, mobility_control |
| Q8 | Indicate assigned seat | pose_estimation, t2s |
| Q9 | Introduce the rest of the guests | t2s, speech_recognition |
| Q10 | Wait for the next guest | mobility_control, t2s |
| Q11 | Detect obstacle | object_detection, pose_estimation |
| Q12 | Handle lost guest | mobility_control, object_detection, t2s |

---

## Challenge 4: Storing Groceries

### State Definitions

| State | Description (Spanish) | Technical Name |
|-------|----------------------|----------------|
| Q1 | Mantenerse quieto | remaining_idle |
| Q2 | Navegar hacia la mesa | navigating_to_table |
| Q3 | Seleccionar objeto | selecting_object |
| Q4 | Transportar a zona de almacenamiento | transporting_to_storage |
| Q5 | Almacenar objeto | storing_object |
| Q6 | Verter cereal | pouring_cereal |
| Q7 | Finalizar tarea | finishing_task |
| Q8 | Detectar obstáculo | detecting_obstacle |

### Events

| Event | Description |
|-------|-------------|
| a | Puerta abierta (inicio del reto) |
| b | Mesa alcanzada |
| c | Repetir navegación |
| d | Error en selección de objeto |
| e | Objeto seleccionado |
| f | Error en transporte de objeto |
| g | Objeto almacenado |
| h | Objeto en su lugar |
| i | Tarea completada |
| j | Cereal vertido |
| k | Se encontró obstáculo |
| l | Obstáculo evitado |
| m | Obstáculo evitado |
| n | Orden de verter cereal |
| o | Objeto almacenado |

### State Functions Required

| State | English Description | Required Functions |
|-------|--------------------|--------------------|
| Q1 | Remain idle | mobility_control |
| Q2 | Navigate to the table | path_planning, mobility_control |
| Q3 | Select object | object_detection, object_recognition |
| Q4 | Transport to storage area | mobility_control, pose_estimation, path_planning |
| Q5 | Store object | armcontrol, object_detection, pose_estimation |
| Q6 | Pour cereal | armcontrol, pose_estimation |
| Q7 | Complete task | t2s, speech_recognition |
| Q8 | Detect obstacle | object_detection, mobility_control |

---

## Challenge 5: Clean the Table

### State Definitions

| State | Description (Spanish) | Technical Name |
|-------|----------------------|----------------|
| Q1 | Mantenerse quieto | remaining_idle |
| Q2 | Ir a la mesa | going_to_table |
| Q3 | Mirar mesa | looking_at_table |
| Q4 | Clasificar objeto | classifying_object |
| Q5 | Recoger objeto | picking_object |
| Q6 | Navegar a destino | navigating_to_destination |
| Q7 | Depositar objeto | dropping_object |
| Q8 | Verificar objetos en la mesa | verifying_table_items |
| Q9 | Completar tarea | completing_task |
| Q10 | Detectar obstáculo | detecting_obstacle |

### Events

| Event | Description |
|-------|-------------|
| a | Puerta abierta (inicio del reto) |
| b | No se llego a la mesa |
| c | Se llego a la mesa |
| d | Mesa analizada |
| e | Objeto clasificado |
| f | Objeto recogido correctamente |
| g | Objeto listo para ser depositado |
| h | Objeto depositado |
| i | Quedan objetos en la mesa |
| j | Mesa vacía (tarea completada) |
| k | Se detectó un obstáculo |
| l | Error al clasificar objeto |
| m | Error al recoger objeto |
| n | Error al navegar |
| o | Error general del sistema |
| p | Objeto no encontrado en el destino |
| q | Tarea finalizada |
| r | Ya no hay obstaculo |
| s | Objeto no encontrado en clasificación |
| t | Se encontro obstaculo |

### State Functions Required

| State | English Description | Required Functions |
|-------|--------------------|--------------------|
| Q1 | Remain idle | mobility_control |
| Q2 | Go to the table | path_planning, mobility_control, pose_estimation |
| Q3 | Look at the table | pose_estimation, object_detection |
| Q4 | Classify object | object_recognition, object_detection |
| Q5 | Pick up object | armcontrol, object_detection, pose_estimation |
| Q6 | Navigate to destination | path_planning, mobility_control, pose_estimation |
| Q7 | Drop object | armcontrol, pose_estimation |
| Q8 | Verify objects on the table | object_detection, pose_estimation |
| Q9 | Complete task | t2s, speech_recognition |
| Q10 | Detect obstacle | object_detection, mobility_control |

---

## Challenge 6: Enhanced General Purpose Service Robot

### State Definitions

| State | Description (Spanish) | Technical Name | Next States |
|-------|----------------------|----------------|-------------|
| Q1 | Mantenerse quieto | remaining_idle | Q1 |
| Q2 | Mirar la arena | scanning_arena | Q2, Q3, Q5, Q7 |
| Q3 | Detectar basura en el piso | detecting_trash | Q3, Q4 |
| Q4 | Botar basura | disposing_trash | Q2, Q4 |
| Q5 | Detectar objeto fuera de lugar | detecting_displaced_object | Q5, Q6 |
| Q6 | Colocar objeto en su lugar | placing_object | Q2, Q6 |
| Q7 | Detectar persona que necesita ayuda | detecting_person_request | Q7, Q8 |
| Q8 | Entender orden | understanding_command | Q8, Q9 |
| Q9 | Ejecutar orden | executing_command | Q9, Q10 |
| Q10 | Orden ejecutada | command_completed | Q2 |
| Q11 | Detectar obstáculo | obstacle_detected | Q11 |

### Events

| Event | Description |
|-------|-------------|
| a | Puerta abierta (inicio del reto) |
| b | No se detecta nada |
| c | Se detectó basura |
| d | Se detectó objeto fuera de lugar |
| e | Persona solicita ayuda |
| f | Basura identificada |
| g | Basura no identificada |
| h | Basura botada |
| i | Objeto fuera de lugar detectado |
| j | Objeto no encontrado |
| k | Objeto colocado correctamente |
| l | Objeto no pudo ser colocado |
| m | Persona identificada claramente |
| n | No se identificó bien la orden |
| o | Orden comprendida |
| p | Orden ejecutada |
| q | Problema solucionado |
| r | Obstáculo no detectado |
| s | Obstáculo detectado |
| t | Obstáculo evadido |

### State Functions Required

| State | English Description | Required Functions |
|-------|--------------------|--------------------|
| Q1 | Remain idle | mobility_control |
| Q2 | Scan the arena | pose_estimation, object_detection |
| Q3 | Detect trash on the floor | object_detection, object_recognition |
| Q4 | Dispose of trash | mobility_control, armcontrol |
| Q5 | Detect misplaced object | object_detection, object_recognition |
| Q6 | Place object in correct location | armcontrol, pose_estimation |
| Q7 | Detect person who needs help | pose_estimation, speech_recognition |
| Q8 | Understand command | speech_recognition |
| Q9 | Execute command | mobility_control, path_planning |
| Q10 | Command completed | mobility_control, path_planning |
| Q11 | Detect obstacle | object_detection, mobility_control |

---

## Challenge 7: Restaurant

### State Definitions

| State | Description (Spanish) | Technical Name | Next States |
|-------|----------------------|----------------|-------------|
| Q1 | Mantenerse quieto | remaining_idle | Q1 |
| Q2 | Observar clientes en la fila | watching_queue | Q2, Q3 |
| Q3 | Navegar hacia la mesa del cliente | going_to_customer_table | Q3, Q4, Q11 |
| Q4 | Tomar pedido | taking_order | Q5 |
| Q5 | Confirmar pedido | confirming_order | Q6 |
| Q6 | Ir a la cocina | returning_to_kitchen | Q7, Q11 |
| Q7 | Recoger el pedido | picking_up_order | Q8 |
| Q8 | Llevar pedido al cliente | delivering_order | Q9, Q11 |
| Q9 | Finalizar turno | ending_shift | Q2 |
| Q10 | Solicitar instrucciones humanas | requesting_instructions | Q2, Q10 |
| Q11 | Gestionar obstáculos | handling_obstacle | Q3, Q6, Q8 |

### Events

| Event | Description |
|-------|-------------|
| a | Inicio del turno |
| b | No hay clientes |
| c | Cliente identificado llamando o haciendo señas |
| d | Interacción no válida con cliente |
| e | Cliente listo para ordenar |
| f | Pedido mal tomado o cliente cambia de opinión |
| g | Confirmación del pedido |
| h | Pedido listo para entrega |
| i | Llegada correcta al cliente |
| j | Cliente no encontrado / cambio de ubicación |
| k | Pedido servido exitosamente |
| l | Error al entregar el pedido |
| m | Pedido entregado completamente |
| n | Cliente satisfecho / turno completado |
| o | Robot requiere ayuda o intervención del humano |
| p | Asistencia no resuelta / repetir consulta |
| q | Asistencia resuelta |
| r | Obstáculo no detectado |
| s | Trayecto hacia cliente bloqueado |
| t | Obstáculo evadido correctamente |

### State Functions Required

| State | English Description | Required Functions |
|-------|--------------------|--------------------|
| Q1 | Remain idle | mobility_control |
| Q2 | Observe clients in the line | pose_estimation, object_detection, speech_recognition |
| Q3 | Navigate to the customer's table | path_planning, mobility_control, pose_estimation |
| Q4 | Take order | speech_recognition, t2s, object_detection, button |
| Q5 | Confirm order | t2s, speech_recognition |
| Q6 | Go to the kitchen | path_planning, mobility_control |
| Q7 | Pick up the order | armcontrol, object_detection, pose_estimation |
| Q8 | Deliver order to the customer | mobility_control, path_planning, pose_estimation |
| Q9 | End shift | t2s, mobility_control |
| Q10 | Request human instructions | speech_recognition, t2s, button |
| Q11 | Handle obstacles | object_detection, mobility_control, pose_estimation |

---

## Challenge 8: Give Me a Hand

### State Definitions

| State | Description (Spanish) | Technical Name | Next States |
|-------|----------------------|----------------|-------------|
| Q1 | Mantenerse quieto | remaining_idle | Q1, Q2 |
| Q2 | Navegar hasta el operador | navigating_to_operator | Q2, Q3, Q10 |
| Q3 | Recibir objeto | receiving_object | Q3, Q4 |
| Q4 | Interpretar orden | interpreting_command | Q4, Q5, Q10 |
| Q5 | Solicitar confirmación | requesting_confirmation | Q5, Q6, Q4 |
| Q6 | Navegar al destino | navigating_to_target | Q6, Q7, Q10 |
| Q7 | Colocar objeto | placing_object | Q7, Q8 |
| Q8 | Volver con el operador | returning_to_operator | Q8, Q9, Q10 |
| Q9 | Orden finalizada | task_completed | Q2 |
| Q10 | Gestionar obstáculos | handling_obstacle | Q6, Q8, Q10 |

### Events

| Event | Description |
|-------|-------------|
| a | Inicio del reto |
| b | Robot se activa para ir al operador |
| c | El robot localiza al operador correctamente |
| d | Error al navegar al operador |
| e | Operador prepara objeto |
| f | Robot recibe objeto exitosamente |
| g | Ambigüedad en la instrucción |
| h | Instrucción comprendida parcialmente |
| i | Se requiere confirmación adicional |
| j | Confirmación recibida |
| k | Navegación hacia el destino iniciada |
| l | Se encuentra un obstáculo durante la navegación |
| m | Llegada al destino confirmada |
| n | Objeto depositado |
| o | Obstáculo detectado durante el regreso |
| p | Error en la colocación del objeto |
| q | Objeto no colocado correctamente |
| r | Orden no comprendida |
| s | Orden reconocida correctamente |
| t | Objeto entregado correctamente |
| u | Instrucción completa / ciclo exitoso |
| v | Reintento de navegación al operador |
| w | Reintento para interpretar la orden |
| x | Error general del sistema |

---

## Implementation Notes

- All state machines are implemented in Python
- Each challenge requires specific combinations of robot functions
- State transitions are event-driven
- The system integrates multiple subsystems including:
  - Mobility control
  - Path planning
  - Object detection and recognition
  - Pose estimation
  - Speech recognition and text-to-speech
  - Arm control
  - Mapping
  - Face recognition
  - Button interface
