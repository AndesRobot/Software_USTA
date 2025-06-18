def Help_me_carry():
    #Help me carry

def Help_me_carry_2():
    #Help Me Carry 2

def Receptionist():
    #Receptionist

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
