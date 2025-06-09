def q1():
    print("Q1: Waiting for person (waiting_person)")
    while True:
        char = yield
        if char == 'a':
            yield from q1()
        elif char == 'b':
            yield from q2()
        else:
            break

def q2():
    print("Q2: Indicating readiness (notifying_reading)")
    while True:
        char = yield
        if char == 'c':
            yield from q1()
        elif char == 'd':
            yield from q3()
        else:
            break

def q3():
    print("Q3: Following person (following_person)")
    while True:
        char = yield
        if char == 'g':
            yield from q4()
        elif char == 'f':
            yield from q3()
        else:
            break

def q4():
    print("Q4: Wait for stopped person / Detect indication (detecting_indication)")
    while True:
        char = yield
        if char == 'h':
            yield from q3()
        elif char == 'i':
            yield from q5()
        elif char == 'e':
            yield from q1()
        else:
            break

def q5():
    print("Q5: Detect bag (recognition_bag)")
    while True:
        char = yield
        if char == 'k':
            yield from q6()
        elif char == 'j':
            yield from q4()
        else:
            break

def q6():
    print("Q6: Navigate to bag (navegation_to_bag)")
    while True:
        char = yield
        if char == 'l':
            yield from q7()
        else:
            break

def q7():
    print("Q7: Pick up bag (picking_up_bag)")
    while True:
        char = yield
        if char == 'm':
            yield from q8()
        else:
            break

def q8():
    print("Q8: Move to home (homing)")
    while True:
        char = yield
        if char == 'o':
            yield from q9()
        elif char == 'n':
            yield from q10()
        else:
            break

def q9():
    print("Q9: Detect obstacles (detecting_obstacles)")
    while True:
        char = yield
        if char == 'p':
            yield from q8()
        else:
            break

def q10():
    print("Q10: Deliver bag (delivering_bag)")
    while True:
        char = yield
        if char == 'q':
            yield from q11()
        else:
            break

def q11():
    print("Q11: Queueing (queueing)")
    while True:
        char = yield
        if char == 'r':
            yield from q1()
        else:
            break

def fsm():
    state = q1()
    next(state)
    while True:
        try:
            char = input("Press a key (a–r) or 'exit' to quit: ").lower()
            if char == 'exit':
                break
            state.send(char)
        except StopIteration:
            print("Invalid state or final state reached.")
            break

if _name_ == "_main_":
    fsm()
