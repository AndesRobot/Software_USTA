def Help_me_carry():
    # Task: Help Me Carry
    # 300 pts - follow the operator
    # 200 pts - avoid obstacles
    # 100 pts - pick up the bag
    # 200 pts - return
    # 300 pts - join the line (optional)

    # Follow the operator
    print("[Node_pose_estimation] Searching for the operator...")
    # Will confirm with object_detection node
    # Publishing: /pose_estimation (std_msgs/Bool) -> True
    # Publishing: /object_detection (custom_msgs/ObjectRequest) -> Person
    print("[Node_pose_estimation] Assigning ID to detected operator")
    # Subscribed: /pose_estimation (custom_msgs/OperatorID) 
    print("[Node_TTS] I can start following you now")
    # Publishing: /TTS (std_msgs/String) → "I can start following you now"
    #Node_mobility_control
    print("[Node_path_planning] Following the operator at 1 meter distance")
    # Subscribed: /path_planning
    # Avoid obstacles
    print("[Node_path_planning] Adjusting trajectory to avoid obstacles")
    # Possibly better to use Lidar
    print("[Node_path_planning] Detecting obstacles in the environment")

    # Pick up the bag
    print("[Node_object_detection] Detecting cart and bag")
    print("[Node_armcontrol] Picking up the bag from the cart")

    # Return
    print("[Node_path_planning] Returning to the initial position")
    print("[Node_path_planning] Adjusting trajectory to avoid obstacles")
    print("[Node_path_planning] Detecting obstacles in the environment")
    print("[Node_armcontrol] Placing the bag on the ground")

    # Join the line (optional)
    print("[Node_pose_estimation] Detecting if there is a line")
    print("[Node_path_planning] Positioning at the end of the line")

    print("[LOG] ✅ Task completed: Help Me Carry")


def General_Purpose_Service_Robot():
    # Task: General Purpose Service Robot
    # 3 structured tasks x 400 pts = 1200 pts
    # Bonus: tasks given by non-expert user (3x100 pts)

    print("[Node_TTS] Hello, I’m ready to help you. Please tell me what you need.")

    user_commands = [
        "Give Pepito in the kitchen the knife that is in the living room",
        "I'm cold",
        "Take a pen to Juan"
    ]

    for user_input in user_commands:
        print(f"[Node_STT] User: {user_input}")

        # Simulate semantic parsing by LLM
        if "knife" in user_input:
            obj = "knife"
            origin = "living room"
            destination = "kitchen"
        elif "cold" in user_input:
            obj = "blanket"
            origin = "closet"
            destination = "user"
        elif "pen" in user_input:
            obj = "pen"
            origin = "desk"
            destination = "Juan"
        else:
            print("[Node_LLM] Could not interpret the command correctly")
            continue

        print(f"[Node_LLM] Object: {obj}, Origin: {origin}, Destination: {destination}")
        print(f"[Node_path_planning] Navigating to {origin}")
        print(f"[Node_object_detection] Searching for {obj}")
        print(f"[Node_armcontrol] Picking up {obj}")
        print(f"[Node_path_planning] Taking {obj} to {destination}")
        print(f"[Node_armcontrol] Delivering {obj} to {destination}")

    print("[LOG] ✅ Task completed: General Purpose Service Robot")


def Receptionist():
    guests = []
    gathered_interests = []

    # --- GUEST 1 ---
    print("[Node_object_detection] Guest detected at the entrance")
    print("[Node_armcontrol] Opening the door for the guest")
    print("[Node_TTS] Welcome, what is your name?")
    name1 = "Guest_1"
    print(f"[Node_STT] Detected name: {name1}")

    print("[Node_TTS] Would you please join me at the drink table?")
    print("[Node_path_planning] Guiding the guest to the drink table")
    print("[Node_Head] Looking in the navigation direction")

    print("[Node_TTS] While we walk, tell me something you like: a movie, book, or series?")
    interest1 = "music"
    print(f"[Node_STT] Detected interest: {interest1}")

    print("[Node_TTS] What’s your favorite drink?")
    drink1 = "juice"
    print(f"[Node_STT] Preferred drink: {drink1}")
    print("[Node_object_detection] Checking drink availability...")
    print(f"[Node_TTS] Perfect! You may take the {drink1} from the table")

    print("[Node_TTS] Would you like me to take you to the living room?")
    print("[Node_path_planning] Guiding the guest to the living room")
    print("[Node_Head] Looking in the navigation direction")

    print("[Node_TTS] This is your seat, please sit down")

    guests.append({"name": name1, "drink": drink1, "interest": interest1})
    gathered_interests.append(interest1)

    # --- GUEST 2 ---
    print("[Node_object_detection] Guest detected at the entrance")
    print("[Node_armcontrol] Opening the door for the guest")
    print("[Node_TTS] Welcome, what is your name?")
    name2 = "Guest_2"
    print(f"[Node_STT] Detected name: {name2}")

    print("[Node_TTS] Would you please join me at the drink table?")
    print("[Node_path_planning] Guiding the guest to the drink table")
    print("[Node_Head] Looking in the navigation direction")

    print("[Node_TTS] While we walk, tell me something you like: a movie, book, or series?")
    interest2 = "music"
    print(f"[Node_STT] Detected interest: {interest2}")

    print("[Node_TTS] What’s your favorite drink?")
    drink2 = "juice"
    print(f"[Node_STT] Preferred drink: {drink2}")
    print("[Node_object_detection] Checking drink availability...")
    print(f"[Node_TTS] Perfect! You may take the {drink2} from the table")

    print("[Node_TTS] Would you like me to take you to the living room?")
    print("[Node_path_planning] Guiding the guest to the living room")
    print("[Node_Head] Looking in the navigation direction")

    print("[Node_TTS] This is your seat, please sit down")

    guests.append({"name": name2, "drink": drink2, "interest": interest2})
    gathered_interests.append(interest2)

    print("[Node_TTS] Let me introduce you to each other")
    print(f"[Node_TTS] {guests[0]['name']} meet {guests[1]['name']}, they like {guests[1]['interest']}")
    print(f"[Node_TTS] {guests[1]['name']} meet {guests[0]['name']}, they like {guests[0]['interest']}")

    if guests[0]['interest'] == guests[1]['interest']:
        print(f"[Node_TTS] You both like {guests[0]['interest']}, how interesting!")
    else:
        print("[Node_TTS] You have different tastes, but I’m sure you’ll get along.")

    print("[Node_TTS] The first guest has brown hair and wears glasses")
    print("[Node_Head] Observing the conversation, looking at the speaker")
    print("[Node_Head] Adjusting orientation if a guest moves")

    print("Task completed: Receptionist\n")

def Storing_Groceries():
    detected_objects = ["apple", "orange", "cereal_box", "bottle", "banana"]
    categories = {
        "fruits": ["apple", "orange", "banana"],
        "cereals": ["cereal_box"],
        "liquids": ["bottle"]
    }
    shelf_levels = {
        "fruits": "middle level",
        "cereals": "top level",
        "liquids": "bottom level"
    }

    print("[Node_path_planning] Navigating to the object table...")
    # 15 pts

    print("[Node_object_detection] Detecting and classifying objects on the table...")
    for obj in detected_objects:
        print(f"[Node_Reasoning] Classifying object: {obj}")
    # 5×15 = 75 pts

    print("[Node_armcontrol] Opening first cabinet door...")
    # 200 pts
    print("[Node_armcontrol] Opening second cabinet door...")
    # 100 pts

    for category, objects in categories.items():
        for obj in objects:
            print(f"[Node_armcontrol] Picking up object: {obj} to place in the cabinet")
            # 5×50 = 250 pts
            print(f"[Node_object_detection] Inspecting shelf and deciding level for {obj} ({shelf_levels[category]})")
            # 5×15 = 75 pts
            print(f"[Node_path_planning] Navigating to cabinet to store {obj}")
            print(f"[Node_armcontrol] Placing {obj} on the shelf")
            # 5×15 = 75 pts
            print(f"[Node_Reasoning] Grouping {obj} with others of category {category}")
            # 5×50 = 250 pts

    print("[Node_armcontrol] Detecting cereal to pour into container")
    print("[Node_armcontrol] Pouring cereal into designated container")
    # 300 pts

    # Bonus examples if detected:
    print("[Node_armcontrol] Small object detected: awarding 70 pts bonus")
    print("[Node_armcontrol] Precise placement of small object: 30 pts bonus")
    print("[Node_armcontrol] Heavy object manipulation: 70 + 30 pts bonus")
    print("[Node_armcontrol] Fully autonomous pick and place: 50 + 50 pts bonus")

    print("[Node_path_planning] Returning to starting point to report to the referee")
    print("[Node_TTS] Task successfully completed. All objects have been stored")
    print("✅ [LOG] Task finished: Storing Groceries")


def Clean_the_Table():
    table_objects = ["fork", "knife", "plate", "glass1", "glass2"]
    dishwasher_tab = "tablet"
    cleaning_tool = "sponge"

    print("[Node_path_planning] Navigating to the table to pick up objects...")
    # 15 pts

    print("[Node_object_detection] Detecting objects on the table...")
    print(f"[LOG] Detected objects: {table_objects}")

    print("[Node_armcontrol] Opening dishwasher door...")
    print("[Node_armcontrol] Pulling out dishwasher tray...")
    # 2×200 + 2×100 pts

    for obj in table_objects:
        print(f"[Node_armcontrol] Picking up {obj} to transport it")
        if obj in ["glass1", "glass2"]:
            print(f"[Node_armcontrol] Placing {obj} in the trash bin")
            # 2×50 pts
        else:
            print(f"[Node_TTS] This object is cleanable and should be placed properly")
            print(f"[Node_armcontrol] Inserting {obj} into the dishwasher")
            # 5×50 + 5×75 pts

    print(f"[Node_armcontrol] Picking up dishwasher tab: {dishwasher_tab}")
    print(f"[Node_armcontrol] Placing {dishwasher_tab} in its proper compartment")
    # 100 + 200 pts

    print(f"[Node_armcontrol] Using {cleaning_tool} to clean drink area")
    # 2×50 pts

    # Bonus: Autonomous pick and place
    print("[Node_armcontrol] Object fully handled autonomously (pick + place)")
    # 50 + 50 pts

    print("[Node_path_planning] Returning to starting point")
    print("[Node_TTS] Task finished: all objects handled correctly")
    print("✅ [LOG] Task completed: Clean the Table")


def Enhanced_General_Purpose_Service_Robot():
    # Task: Enhanced General Purpose Service Robot
    # 3 detected problems x 150 pts = 450 pts
    # 3 solutions x 650 pts = 1950 pts

    problems = [
        "The lamp is on with no one in the room",
        "There is trash on the floor",
        "The refrigerator is open"
    ]

    for problem in problems:
        print(f"[Node_LLM] Detecting problem: {problem}")
        print("[Node_Reasoning] Generating corrective action")
        print("[Node_path_planning] Moving toward problem area")
        print("[Node_armcontrol] Executing corrective action (turn off, pick up, close, etc.)")
        print("[Node_TTS] Action completed for the problem")

    print("[LOG] ✅ Task completed: Enhanced General Purpose Service Robot")

def Restaurant():
    client_1 = "table_3"
    client_order = "orange juice"
    available_menu = ["soda", "orange juice", "water"]
    bar_objects = ["orange juice", "apple juice", "soda"]

    # --- CLIENT DETECTION ---
    # Node_object_detection and Node_STT
    print("[Node_pose_estimation] Detecting if a client is calling or greeting the robot")
    print("[Node_TTS] Hello! Would you like to place an order?")
    # → 2×100 pts

    # --- APPROACH THE TABLE ---
    print(f"[Node_path_planning] Navigating to client's location: {client_1}")
    # → 2×100 pts

    # --- TAKE ORDER ---
    print("[Node_TTS] What would you like to order?")
    print(f"[Node_STT] Client: '{client_order}'")
    if client_order not in available_menu:
        print("[Node_TTS] Sorry, that item is not on the menu.")
        return
    print(f"[Node_TTS] Just to confirm, you want '{client_order}'?")
    print("[Node_STT] Client: Yes")
    # → 2×200 pts

    # --- INFORM THE BARTENDER ---
    print("[Node_path_planning] Navigating to the bar")
    print("[Node_TTS] Bartender, please prepare a(n) " + client_order)
    # → 2×100 pts

    # --- PICK UP ORDER ---
    if client_order in bar_objects:
        print(f"[Node_armcontrol] Using tray to pick up: {client_order}")
        # → Bonus 2×200 pts (if non-attached tray is used)
    else:
        print("[Node_TTS] Item not found, canceling delivery")
        return

    # --- RETURN TO TABLE ---
    print(f"[Node_path_planning] Returning to {client_1} with the order...")
    # → 2×100 pts

    # --- SERVE ORDER ---
    print("[Node_armcontrol] Serving the order to the client")
    print("[Node_TTS] Here is your order. Enjoy!")
    # → 2×200 pts

    print("✅ [LOG] Task finished: Restaurant completed")


def Give_Me_a_Hand():
    # Initial navigation to the operator
    print("[Node_path_planning] Entering test area and locating operator...")
    print("[Node_pose_estimation] Operator detected. Approaching to receive instructions.")
    # → 100 pts

    requests = ["remote control", "book", "glass"]
    locations = {
        "remote control": "living room",
        "book": "bedroom",
        "glass": "kitchen"
    }
    available_objects = {
        "living room": ["remote control", "pillow"],
        "bedroom": ["book", "lamp"],
        "kitchen": ["glass", "plate"]
    }

    for item in requests:
        print(f"\n[User] Please take the {item}")

        # Approach the operator’s hand to receive the item
        print(f"[Node_armcontrol] Approaching operator’s hand without contact to receive: {item}")
        # → 50 pts

        print(f"[Node_armcontrol] Receiving '{item}' from operator")
        # → 100 pts

        location = locations.get(item)
        if not location:
            print(f"[Node_TTS] Where should I take the {item}?")
            # → 50 pts (natural interaction to disambiguate)
            print("[Node_STT] User: Take it to the desk")
            continue

        print(f"[Node_path_planning] Navigating to the {location}")
        found = available_objects.get(location, [])
        print(f"[Node_object_detection] Scanning in {location}... detected objects: {found}")

        if item in found:
            print(f"[Node_armcontrol] Placing '{item}' in the {location}")
            # → 100 pts
        else:
            print(f"[Node_TTS] I couldn’t find the {item} in the {location}")
            print("[Node_TTS] Would you like me to try with another object?")

    print("\n[Node_TTS] Do you need anything else?")
    print("[User] No, thank you.")
    print("✅ [LOG] Task finished: Give Me a Hand completed")


def show_menu():
    print("\n=== MAIN MENU ===")
    print("1. Run Help_me_carry")
    print("2. Run General_Purpose_Service_Robot")
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
                General_Purpose_Service_Robot()
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

# ⚠️ General guideline:
# If the robot cannot complete an action:
# 1. It must use natural language to inform the user of the failure
# 2. If possible, it should signal (visually or acoustically) to support communication
