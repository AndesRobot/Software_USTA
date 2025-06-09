def q1():
    print("Q1: Stay still")
    while True:
        char = yield
        if char == 'a': 
            yield from q2()
        else:
            break

def q2():
    print("Q2: Receive command")
    while True:
        char = yield
        if char == 'b':  # Event: Person gives command
            yield from q3()
        else:
            break

def q3():
    print("Q3: Execute command")
    while True:
        char = yield
        if char == 'c':  # Event: Command received
            yield from q4()
        else:
            break

def q4():
    print("Q4: Complete command")
    while True:
        char = yield
        if char == 'd':  # Event: Navigation to instruction point
            yield from q5()
        else:
            break

def q5():
    print("Q5: Reach instruction")
    while True:
        char = yield
        if char == 'e':  # Event: Instruction point reached
            yield from q6()
        elif char == 'f':  # Event: Object detected
            yield from q1()
        else:
            break

def q6():
    print("Q6: Detect obstacles")
    while True:
        char = yield
        if char == 'g':  # Event: Object avoided
            yield from q5()
        else:
            break

def fsm():
    state = q1()
    next(state)
    while True:
        try:
            char = input("Press a key (a–g) or 'exit' to quit: ").lower()
            if char == 'exit':
                break
            state.send(char)
        except StopIteration:
            print("Invalid state or final state reached.")
            break

if _name_ == "_main_":
    fsm()
