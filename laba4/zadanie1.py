from random import randrange as rr

n = rr(4, 31)
while n > 0:
    try:
        print("Камней в кучке ", n)
        print("Выберите кол-во камней от 1 до 3")
        take = 0
        try:
            take = int(input())
        except ValueError:
            print("Вы ввели не целое число")
            exit()
        if take < 0 or take > 3:
            print("Введено неверное кол-во камней")
            exit()
        while n - take < 1:
            print("Кол-во камней в куче не может быть отрицательным")
            take = int(input())
            continue
        n -= take

        if n == 1:
            print("Вы выйграли!")
            break

        compTurn = 0
        compTurn = rr(1, 4)
        while n - compTurn < 1:
            compTurn = rr(1, 4)
        n -= compTurn
        print("Компьютер взял", compTurn, "камней")

        if n == 1:
            print("Вы проиграли")
            break
    except ValueError:
        print("Введите число от 1 до 3")