from src.book import Book
from src.library import ListBook


def choosing_action() -> int:


    print("\nВыберите операцию работы с библиотекой.")
    print("1. Вывести список книг.")
    print("2. Добавить книгу.")
    print("3. Найти книгу.")
    print("4. Удалить книгу.")
    print("5. Изменить статус книги.")
    print("0. Выход из работы с библиотекой.")
    my_choice = input('Введите нужную цифру и нажмите Enter: ')
    if my_choice.isdigit():
        my_choice = int(my_choice)
    return my_choice


def new_book() -> Book:

    title = input('Название книги: ')
    author = input('Автор книги: ')
    year = int(input('Год издания книги: '))
    book = Book(title, author, year)
    return book


def choosing_find(list_book: ListBook) -> ListBook:

    list_book_find: ListBook = ListBook()
    while True:
        print("\nВыберите по какому параметру ищем.")
        print("1. Название.")
        print("2. Автор.")
        print("3. Год издания.")
        print("0. Выход из поиска. Вернуть результат.")
        my_choice = input('Введите нужную цифру и нажмите Enter: ')
        if my_choice.isdigit() and 0 <= int(my_choice) <= 3:
            list_book_find.clear()
            match int(my_choice):
                case 1:
                    title = input("Введите название: ")
                    list_book_find.add_list_book(
                        books=list_book.find_book_title(title))
                case 2:
                    author = input("Введите автора: ")
                    list_book_find.add_list_book(
                        books=list_book.find_book_author(author))
                case 3:
                    while True:
                        year = input("Введите год: ")
                        if year.isdigit():
                            list_book_find.add_list_book(
                                list_book.find_book_year(int(year)))
                            break
                        print("Неверный формат года.")
                case 0:
                    return list_book_find
            print(f"Найдено книг: {list_book_find.count()}")
            if list_book_find.count() > 0:
                print(list_book_find)
        else:
            print("\nНеверная команда.")


def change_status(list_book: ListBook):

    while True:
        id_book = input('Введите идентификатор книги (число): ')
        if id_book.isdigit():
            id_book = int(id_book)
            index = list_book.find_index(id_book)
            if index is None:
                print(f'Книги с таким {id_book} нет.')
                continue
            print(f'Для книги с идентификатором={id_book} '
                  f'статус={list_book.list_book()[index].status_str}')
            is_change = input('Меняем статус? 1 - Да, 2 - Нет ')
            if is_change.lower() == 'да' or is_change == '1':
                is_status: bool = not list_book.list_book()[index].status
                list_book.list_book()[index].status = bool(is_status)
            break

