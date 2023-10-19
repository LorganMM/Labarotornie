from random import randrange

n = randrange(4, 31)
while n > 0:
    try:
        print("Камней в кучке ", n)
        print("Выберите кол-во камней от 1 до 3")
        playerTurn = 0
        try:
            playerTurn = int(input())
        except ValueError:
            print("Вы ввели не целое число")
            exit()
        if playerTurn < 0 or playerTurn > 3:
            print("Введено неверное кол-во камней")
            exit()
        while n - playerTurn < 1:
            print("Кол-во камней в куче не может быть отрицательным")
            playerTurn = int(input())
            continue
        n -= playerTurn

        if n == 1:
            print("Вы выйграли!")
            break

        compTurn = randrange(1, 4)
        while n - compTurn < 1:
            compTurn = randrange(1, 4)
        n -= compTurn
        print("Компьютер взял", compTurn, "камней")

        if n == 1:
            print("Вы проиграли")
            break
    except ValueError:
        print("Введите число от 1 до 3")
#afafawfawfaw