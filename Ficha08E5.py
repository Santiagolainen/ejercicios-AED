__author__ = "Santiago"

import random

x = random.randint(0, 10)
y = random.randint(0, 10)

print("Tito el robot")
print("="*80)

print(f"\nLa posición de tito es de ({x},{y})")
print("\nSeleccione hacia a donde quiere mover a tito\n")
print("1 - Girar al norte y avanzar 10 pasos")
print("2 - Girar al sur y avanzar 20 pasos")
print("3 - Girar al este y avanzar 10 pasos")
print("4 - Girar al oeste y avanzar 20 pasos")
print("5 - Finalizar programa")
op = int(input())

while op != 5:
    if op == 1:
        y += 10
    elif op == 2:
        y -= 20
    elif op == 3:
        x += 10
    elif op == 4:
        x -= 20
    else:
        print("Comando no válido")
    print(f"\nLa posición de tito es de ({x}, {y})")
    print("\nSeleccione hacia a donde quiere mover a tito\n")
    print("1 - Girar al norte y avanzar 10 pasos")
    print("2 - Girar al sur y avanzar 20 pasos")
    print("3 - Girar al este y avanzar 10 pasos")
    print("4 - Girar al oeste y avanzar 20 pasos")
    print("5 - Finalizar programa")
    op = int(input())

print(f"La posición final de tito es de ({x}, {y})")

