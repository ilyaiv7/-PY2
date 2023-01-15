BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """
    Создание и подготовка к работе объекта "Книга"

    :param id_: идентификатор книги
    :param name: название книги
    :param pages: количество страниц в книге

    Примеры:
    >>> book = Book(1, "test_name_1", 200)
    """
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть типа int")
        if id_ < 0:
            raise ValueError("Идентификатор книги должен быть больше нуля")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if pages < 1:
            raise ValueError("Количество страниц в книге должно быть больше одной")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


class Library:
    """
    Создание и подготовка к работе объекта "Библиотека"

    :param books: Список книг в библиотеке, каждая книга характеризуется
    параметрами: "id", "name", "pages"
    books = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
    ]
    """
    def __init__(self, books: list = None):
        self.books = [] if books is None else books

    def get_next_book_id(self) -> int:
        if self.books:
            return self.books.index(self.books[-1]) + 2
        else:
            return 1

    def get_index_by_book_id(self, id_: int) -> int:
        dict_index_id = {}
        for index_book, book in enumerate(self.books):
            dict_index_id[book.__dict__["id_"]] = index_book

        if id_ in dict_index_id:
            return dict_index_id[id_]
        else:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
    print(library_with_books.get_index_by_book_id(2))  # проверяем индекс книги с id = 2
    print(library_with_books.get_index_by_book_id(3))  # проверяем индекс книги с id = 3