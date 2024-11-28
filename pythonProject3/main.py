from src.book import Book
from src.library import ListBook
from src.service import choosing_action, new_book, choosing_find, change_status


def main():

    list_book = ListBook()
    list_book.load_json()
    print(list_book)
    while True:
        print(f'В наличии книг: {list_book.count()}.')
        my_choice = choosing_action()
        if my_choice == 0:
            list_book.save_json()
            break
        match my_choice:
            case 1:
                print("\nВыводим список книг.")
                print(list_book)
            case 2:
                print("\nДобавляем книгу.")
                book: Book = new_book()
                list_book.add_book(book=book)
            case 3:
                print("\nНайти книгу.")
                list_book_find = choosing_find(list_book)
                print(list_book_find)
            case 4:
                print("\nУдалить книгу.")
                id_book = input('Введите идентификатор книги (число): ')
                if id_book.isdigit():
                    index = list_book.find_index(int(id_book))
                    if index is None:
                        print(f'Книги с идентификатором {id_book} нет.')
                        continue
                    list_book.remove_book(int(id_book))
            case 5:
                print("\nСменить статус книги.")
                change_status(list_book)
            case _:
                print("\nНеверная команда.")



if __name__ == '__main__':
    main()