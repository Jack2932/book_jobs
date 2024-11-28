class Book:

    id: int = 1
    status_dict: dict = {True: 'в наличии', False: 'выдана'}
    name_fields: tuple = ('Идентификатор', 'Автор', 'Название',
                          'Год издания', 'Наличие')

    __slots__ = ('__id_book', '__title', '__author', '__year', '__status',)

    def __init__(self, title: str, author: str,
                 year: int, status: bool = True, id_book: int = 0) -> None:

        self.__id_book = id_book if id_book != 0 else Book.id
        self.__title = title
        self.__author = author
        self.__year = year
        self.__status = status
        Book.id = id_book if (id_book != 0 and id_book > Book.id) \
            else Book.id + 1

    def __repr__(self):

        return (f'{self.__id_book}\t{self.__title}\t{self.__author}\t'
                f'{self.__year}\t{self.__status}')

    def __str__(self):

        return (f'Заголовок: {self.__title}\n'
                f'Автор: {self.__author}\n'
                f'Год издания: {self.__year}\n'
                f'Статус книги: {Book.status_dict[self.__status]}')


    # идентификатор
    @property
    def id_book(self) -> int:
        return self.__id_book

    # название
    @property
    def title(self) -> str:
        return self.__title

    # автор
    @property
    def author(self) -> str:
        return self.__author

    # год издания
    @property
    def year(self) -> int:
        return self.__year

    # статус
    @property
    def status(self) -> bool:
        return self.__status

    # status класса
    @property
    def status_str(self) -> str:
        return Book.status_dict[self.__status]


    # идентификатор
    @id_book.setter
    def id_book(self, id_book: int) -> None:
        self.__id_book = id_book

    # название
    @title.setter
    def title(self, title: str) -> None:
        self.__title = title

    # автор
    @author.setter
    def author(self, author: str) -> None:
        self.__author = author

    # год
    @year.setter
    def year(self, year: int) -> None:
        self.__year = year

    # статус
    @status.setter
    def status(self, status: bool) -> None:
        self.__status = status

    # status класса
    @status_str.setter
    def status_str(self, status: str) -> None:
        is_status = True if status == Book.status_dict[True] else False
        self.__status = is_status

    def to_json(self) -> dict:
        json_data = {
            "id": self.__id_book,
            "title": self.__title,
            "author": self.__author,
            "year": self.__year,
            "status": Book.status_dict[self.__status]
        }
        return json_data

    def from_json(self, json_data: dict) -> None:
        self.__id_book = json_data["id"]
        self.__title = json_data["title"]
        self.__author = json_data["autor"]
        self.__year = json_data["year"]
        self.__status = [k for k, v in Book.status_dict.items()
                         if v == json_data['status']]