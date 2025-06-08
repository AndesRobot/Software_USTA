
## 🧠 FSM – Help Me Carry

Este reto simula la asistencia del robot para llevar una bolsa desde un vehículo hasta una ubicación de inicio, sorteando obstáculos y siguiendo instrucciones humanas. A continuación se describen los estados y sus respectivas transiciones:

### Estados y Transiciones

- **Q1** → `Identificando persona` (tecla `a`)
- **Q2** → `Persona identificada` (tecla `b`)
- **Q3** → `Persona camina` (tecla `c`)
- **Q4** → `Persona se detiene` (tecla `d`)
- **Q5** → `Se recibe indicación` (tecla `e`)
- **Q6** → `Identificar bolsa` (tecla `f`)
- **Q7** → `Recoger bolsa` (tecla `g`)
- **Q8** → `Regresar con bolsa` (tecla `h`)
- **Q9** → `Se detecta obstáculos` (tecla `i`)
- **Q10** → `Se evitan obstáculos` (tecla `j`)
- **Q11** → `Se detecta cosas pequeñas` (tecla `k`)
- **Q12** → `Entregar bolsa` (tecla `l`)
- **Q13** → `Regresando al estado inicial` (tecla `m`)

#### Transiciones adicionales:
`n`, `o`, `p`, `q`, `r`, `s`, `t`, `u`, `v`, `w`, `x`

### 🧭 Tabla de Estados 

Cofificacion del reto uno para la creación de las maquinas de estado

| Estado |Estado| Nombre | 
|-----|---|--------|
| Q1 | Esperar persona | waiting_person |
| Q2 | Indicar que esta listo | notifiying_reading |
| Q3 | Seguir persona | following_person |
| Q4 | Esperar persona detenida / Detectar indicación | detecting_indication |
| Q5 | Detectar bolsa | recognition_bag |
| Q6 | Navegar a bolsa | navegation_to_bag |
| Q7 | Recoger bolsa | picking_up_bag |
| Q8 | Avanzar a home | homing |
| Q9 | Detectar obstaculos | detecting_obstacles |
| Q10 | Entregar bolsa | delivering_bag |
| Q11 | Hacer fila | queuing |




### 🎯 Tabla de Eventos

Eventos para que suceda cada estado mostrado anteriomente

| Evento | Descripción                |
|--------|----------------------------|
| a      | Persona no identificada    |
| b      | Persona identificada       |
| c      | La persona no está al frente |
| d      | Persona da orden           |
| e      | La persona no está al frente |
| f      | Persona camina             |
| g      | Persona detenida           |
| h      | Persona camina             |
| i      | Indicación recibida        |
| j      | Bolsa no detectada         |
| k      | Bolsa detectada            |
| l      | Bolsa al alcance           |
| m      | Bolsa asegurada            |
| n      | Se llegó a Home            |
| o      | Obstáculo detectado        |
| p      | Obstáculo evadido          |
| q      | Bolsa entregada            |
| r      | Primero en la fila         |

### Diagrama FSM

![FSM_HelpMeCarry](FMS_Help_me_carry.png)

---



---

## 🟣 Reto 2 – FSM: General Purpose Service Robot

## 🤖 FSM – General Purpose Service Robot


Este reto representa un robot multifuncional que puede ejecutar diferentes órdenes emitidas por un operador humano, desde reconocer obstáculos hasta entregar objetos y regresar al punto de instrucción.

### Estados y Transiciones

- **Q1** → `Se detecta obstáculo` (tecla `a` o `b`)
- **Q2** → `No se detecta obstáculo` (tecla `c` o `d`)
- **Q3** → `Quieto` (tecla `e` o `f`)
- **Q4** → `Se recibe orden` (tecla `g` o `h`)
- **Q5** → `Ejecutando orden` (tecla `i` o `z`)
- **Q6** → `Finalizando orden` (tecla `j` o `z`)
- **Q7** → `Punto de instrucción` (tecla `k`, `l` o `z`)

### Diagrama FSM

![FSM_GeneralPurpose](General_purpose_service_robot.png)

---


### 🧭 Tabla de Estados 

| Estado |Estado| Nombres  |
|--------|--------|-|
| Q1 | Mantenerse quieto | remaining_idle |
| Q2 | Recibir orden | receiving_command |
| Q3 | Ejecutar orden | executing_command |
| Q4 | Finalizar orden | finishing_command |
| Q5 | Llegar a instrucción | reaching_instruction |
| Q6 | Detectar obstaculos | detecting_obstacles |

### 🎯 Tabla de Eventos 

| Evento | Descripción                        |
|--------|------------------------------------|
| a      | Puertas abiertas                   |
| b      | Persona da orden                   |
| c      | Orden recibida                     |
| d      | Navegación al punto de instrucción |
| e      | Punto de instrucción alcanzado     |
| f      | Objeto detectado en trayecto       |
| g      | Objeto evadido                     |

---

## 🧩 Código de ejemplo (FSM – Help Me Carry)

Este es un fragmento de la implementación para `Help Me Carry`, en donde cada estado espera una tecla correspondiente para hacer una transición:

```python
def q1():
    print("Q1: Esperar persona (waiting_person)")
    while True:
        char = yield
        if char == 'a':
            yield from q1()
        elif char == 'b':
            yield from q2()
        else:
            break
```

### ¿Qué hace este código?
- Muestra el estado actual (por consola).
- Espera que el usuario presione una tecla (`a`, `b`, etc.).
- Si la entrada corresponde a una transición válida, salta al estado siguiente.

Este patrón se replica para cada estado descrito en el FSM.

---



---

## 📁 Estructura del Proyecto



```
decision_making/
├── FMS_Help_me_carry.py
├── FMS_General_purpose_service_robot.py
├── FMS_Help_me_carry.png
├── General_purpose_service_robot.png
└── README.md
```

Cada archivo `.py` contiene el FSM correspondiente al reto, y las imágenes son diagramas de las máquinas de estado.

---

