# print("   1  2  3")
# print("1   |  |  ")
# print("  ________")
# print("2   |  |  ")
# print("  ________")
# print("3   |  |  ")






laukums = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

speletaja_simbols = "X"

def izdruka_laukumu():
    j = 1
    print("  1   2   3")
    for rinda in laukums:
        i = 1
        print(j, end = " ")
        for rutina in rinda:
            if i < 3:
                beigas = " | "
            else:
                beigas = ""
            print(rutina, end = beigas)
            i = i + 1
        print()
        if j < 3:
            print("------------")
        j = j + 1

def gajiena_ievads(x_vai_y):
    while True:
        skaitlis = input(x_vai_y + ": ")
        if len(skaitlis) != 1 or skaitlis < "1" or skaitlis > "3":
            print("Nekorekts ", x_vai_y)
        else:
            return int(skaitlis)

def gajiena_ievade():
    print("Ievadi gājienu:")
    while True:
        x = gajiena_ievads("X")
        y = gajiena_ievads("Y")

        rutina = laukums[y - 1][x - 1]
        if rutina != " ":
            print("Rūtiņa jau ir aizņemta! Izvēlies citu!")
        else:
            laukums[y - 1][x - 1] = speletaja_simbols
            break

def ir_speles_beigas():
    for rinda in laukums:
        if rinda[0] != " " and rinda[0] == rinda[1] and rinda[1] == rinda[2]:
            print("Spēle beigusies! Uzvarēja: ", rinda[0], )
            return True

    x = 0
    while x < 3:
        if laukums[0][x] != " " and laukums[0][x] == laukums[1][x] and laukums[1][x] == laukums[2][x]:
            print("Spēle beigusies! Uzvarēja: ", rinda[0], )
            return True
        x += 1

    ir_tuksa_rutina = False
    for rinda in laukums:
        for rutina in rinda:
            if rutina == " ":
                ir_tuksa_rutina = True

    if not ir_tuksa_rutina:
        print("Neizšķirts!")
        return True

while True:
    izdruka_laukumu()
    gajiena_ievade()

    if ir_speles_beigas():
        break

    if speletaja_simbols == "X":
        speletaja_simbols = "0"
    else:
        speletaja_simbols = "X"
