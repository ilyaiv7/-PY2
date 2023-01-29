class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Название книги должно быть типа str")
        if len(new_name) == 0:
            raise ValueError("Название книги должно иметь хотя бы один символ")
        self._name = new_name

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, str):
            raise TypeError("ФИО автора должны быть типа str ")
        if len(new_author) == 0:
            raise ValueError("ФИО автора должны иметь хотя бы один символ")
        self._author = new_author

    def __str__(self):
        return f'Книга "{self.name}". Автор {self.author}'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Бумажная книга. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом больше нуля")
        self._pages = new_pages

    def __str__(self):
        return f'Бумажная книга "{self.name}". Автор {self.author}. Количество страниц {self._pages}'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):
    """ Аудиокнига. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть больше нуля положительным числом")
        self._duration = new_duration

    def __str__(self):
        return f'Аудиокнига "{self.name}". Автор {self.author}. Продолжительность аудокниги {self.duration}'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

print(Book('Евгений Онегин', 'Пушкин'))
print(PaperBook('Евгений Онегин', 'Пушкин', 300))
print(AudioBook('Евгений Онегин', 'Пушкин', 100.5))

print(repr(Book('Евгений Онегин', 'Пушкин')))
print(repr(PaperBook('Евгений Онегин', 'Пушкин', 300)))
print(repr(AudioBook('Евгений Онегин', 'Пушкин', 100.5)))
