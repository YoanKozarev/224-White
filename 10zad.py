# Четем началното количество хапки от потребителя и създаваме празна опашка за хората, които искат хапки.
initial_bites = int(input())
people_queue = []

# Чакаме вход от потребителя, докато не получим командата "Start".
while True:
    command = input()
    if command == "Start":
        break
    # Добавяме имената на хората в опашката.
    people_queue.append(command)

# Чакаме вход от потребителя, докато не получим командата "End".
while True:
    command = input()
    if command == "End":
        break
    if command.startswith("refill"):
        # Ако командата започва с "refill", добавяме хапките в платото.
        _, added_bites = command.split()
        added_bites = int(added_bites)
        initial_bites += added_bites
    else:
        # Ако командата е име на човек и количество хапки, проверяваме дали има достатъчно хапки в платото.
        person_name, requested_bites = command, int(command)
        if initial_bites >= requested_bites:
            # Ако има достатъчно хапки, отпечатваме съобщение и намаляваме хапките в платото.
            print(f"{person_name} take bites")
            initial_bites -= requested_bites
            # Премахваме човека от опашката.
            people_queue.pop(0)
        else:
            # Ако няма достатъчно хапки, отпечатваме съобщение и премахваме човека от опашката, без да намаляваме хапките.
            print(f"{person_name} must wait")
            people_queue.pop(0)

# На последно място отпечатваме колко хапки са останали в платото.
print(f"{initial_bites} bites left")
