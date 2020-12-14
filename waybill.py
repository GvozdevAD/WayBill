print("Программа для заполнения ПУТЕВОГО ЛИСТА\n")

while True:
    startSpeed = int(input("Введите пробег на начало смены: "))
    endSpeed = int(input("Введите пробег по оканчанию смены: "))
    if endSpeed < startSpeed:
        print("Неверный пробег!!")
        continue
    
    while True:
        try:
            rateFuel = float(input("Введите норму расхода на 100 км: "))
            startFuel = float(input("Введите количество бензина на начало смены: "))
            break        
        except ValueError:        
            print("Нужно вводить через точку!")
    
    refueling = float(input("Введите количество заправленого топлива: "))

    totalSpeed = endSpeed - startSpeed
    endRateFuel = (totalSpeed/100)*rateFuel
    endFuel = startFuel + refueling - endRateFuel
    print(f"\n\nОбщий пробег ТС за сутки: {totalSpeed}")
    print(f"Фактический расход за сутки: {round(endRateFuel, 2)}")
    print(f"Остаток топлива на конец работы: {round(endFuel, 2)}\n\n")

    exitProgramm = input("Для выхода нажмите \"Y\"\n")
    if exitProgramm.lower() == "y":
        break