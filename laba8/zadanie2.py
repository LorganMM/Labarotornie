authors = {'Толстой': ['Война и мир', 'Анна Каренина'],
           'Достоевский': ['Преступление и наказание', 'Идиот', 'Братья Карамазовы'],
           'Пушкин': ['Капитанская дочка']}


def selection():
    while True:
        print("Выберите автора ", list(authors.keys()))

        author = input()
        if not authors.get(author):
            print("Такого автора нет в списке, попробуйте снова.")
        if authors.get(author):
            print(authors[author])
            break


def books(bks):
    print("Введтие произведение")
    book = input().split(',')
    authors[bks].extend(map(lambda x: x.strip().capitalize(), book))


def addition():
    print("Выберите имеющегося автора или добавьте своего", list(authors.keys()))
    author = input()
    if not authors.get(author):
        authors[author] = []
    books(author)
    print(authors)


while True:
    print("Вы хотите выбрать автора или дополнить список? Выбор/Дополнение")
    choice = input()
    if choice == "Выбор":
        selection()
        break
    if choice == 'Дополнение':
        addition()
        break
    else:
        print("Вы неверно ввели команду!")
        print("Команды: Выбор/Дополнение")
