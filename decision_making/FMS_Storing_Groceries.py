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
