import random

num = random.randint(1, 100)

print("Willkommen bei dem Ratespiel!")
print("Das Spiel hat eine zufällige Zahl zwischen 1 und 100")
print("Gib eine Zahl ein und dir wird gesagt, ob du warm oder kalt bist")
print("Je näher du kommst, desto wärmer wird es, je mehr du dich entfernst, wird es kälter")
print("Wenn du die Zahl gefunden hast, wird dir gratuliert!")
print("And now: Have Fun!")

num_input = [0]

while True:

    inputs = int(input("Wähle eine Zahl zwischen 1 und 100: "))

    if inputs < 1 or inputs > 100:
        print("Ausserhalb des Zahlenbereiches! Wähle eine neue Zahl:")
        continue

    if inputs == num:
        print(f"Herzlichen Glückwunsch! Sie haben die Zahl nach {len(num_input)} Versuchen erraten!")
        break

    num_input.append(inputs)

    if num_input[-2]:
        if abs(inputs - num) < abs(num_input[-2] - num):
            print('WÄRMER!')
        else:
            print('KÄLTER!')
    else:
        if abs(inputs - num) <= 10:
            print('WARM!')
        else:
            print('KALT!')