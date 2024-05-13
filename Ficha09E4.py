__author__ = "Santiago"

print("Validación de datos personales")
print("="*80)

print("Eliga una opción:\n")
print("1 - Validez de CUIT\t\t 2 - Validez del DNI")
print("3 - Salir")
op = int(input())

while op != 3:
    if op == 1:
        CUIT = input("Ingrese el número de CUIT con guiones(-) incluidos: ")
        sec_verificar = "5432765432"
        nums = []
        prod_nums = 0
        num_resto = 0
        dig_verificador = 0
        CUIT_valido = False
        if len(CUIT) == 13 and CUIT[2] == "-" and CUIT[11] == "-" and CUIT[0:1].isnumeric() and CUIT[3:10].isnumeric() and CUIT[12].isnumeric():
            for i in CUIT:
                if i == "-":
                    continue
                else:
                    nums.append(i)

            for i in range(len(nums) - 1):
                prod_nums += int(nums[i]) * int(sec_verificar[i])

            num_resto = prod_nums % 11
            dig_verificador = 11 - num_resto

            if dig_verificador == int(nums[-1]):
                CUIT_valido = True

        if CUIT_valido:
            print("El CUIT es válido")
        else:
            print("CUIT no válido")
    elif op == 2:
        DNI = input("Ingrese el número de DNI a verificar: ")

        if DNI[2] == "." and DNI[6] == "." and DNI[0:1].isnumeric() and DNI[3:5].isnumeric() and DNI[7:9].isnumeric():
            print("DNI válido")
        else:
            print("DNI no válido")
    else:
        print("Opción no válida")
    print("Validación de datos personales")
    print("=" * 80)

    print("Eliga una opción:\n")
    print("1 - Validez de CUIT\t\t 2 - Validez del DNI")
    print("3 - Salir")
    op = int(input())