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
