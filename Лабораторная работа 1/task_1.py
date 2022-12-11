import doctest


class Laptop:
    def __init__(self, name: str, model: str, serial_number: str, color: str, size_screen: float, weight: float):
        """
        Создание и подготовка к работе объекта "Ноутбук"

        :param name: Название ноутбука
        :param model: Модель ноутбука
        :param serial_number: Серийный номер ноутбука (5 цифр типа int)
        :param color: Цвет ноутбука
        :param size_screen: Диагональ экрана ноутбука
        :param weight: Вес ноутбука

        Примеры:
        >>> laptop = Laptop("Lenovo", "Legion 5 pro", "12345", "Черный", 15.6, 2.4)
        """
        if not isinstance(name, str):
            raise TypeError("Название ноутбука должно быть типа str")
        self.name = name

        if not isinstance(model, str):
            raise TypeError("Модель ноутбука должна быть типа str")
        self.model = model

        if not isinstance(serial_number, str):
            raise TypeError("Серийный номер ноутбука должен быть типа str")
        if len(serial_number) != 5:
            raise ValueError("Серийный номер ноутбука должен содержать 5 цифр типа int")
        self.serial_number = serial_number

        if not isinstance(color, str):
            raise TypeError("Цвет ноутбука должен быть типа str")
        self.color = color

        if not isinstance(size_screen, float):
            raise TypeError("Размер экрана ноутбука должен быть типа float")
        if size_screen < 10:
            raise ValueError("Размер экрана не должен быть меньше 10 дюймов")
        self.size_screen = size_screen

        if not isinstance(weight, float):
            raise TypeError("Вес ноутбука должен быть типа float")
        if weight <= 0:
            raise ValueError("Вес ноутубка должен быть больше 0 кг")
        self.weight = weight

        self.status = 0 # изначально ноутбук закрыт

    def status_laptop(self) -> bool:
        """
        Функция, которая проверяет в каком положении находится на данный момент ноутбук

        :return: False - ноутбук закрыт, True - ноутбук октрыт

        Примеры:
        >>> laptop = Laptop("Lenovo", "Legion 5 pro", "12345", "Черный", 15.6, 2.4)
        >>> laptop.status_laptop()
        """
        ...

    def open_or_close_laptop(self, state: int) -> None:
        """
        Функция которая открывает и закрывает ноутбук

        :param state: 1 - открыть ноутбук, 0 - закрыть ноутбук

        Примеры:
        >>> laptop = Laptop("Lenovo", "Legion 5 pro", "12345", "Черный", 15.6, 2.4)
        >>> laptop.open_or_close_laptop(1)
        """
        if not isinstance(state, int):
            raise TypeError("переменная state должная быть типа int")
        if state not in (0, 1):
            raise ValueError("state может принимать только два значения 0 - открыть ноутбук, 1 - закрыть ноутбук")
        ...

    def rename(self, name: str) -> None:
        """
        Функция, которая позволяет изменить название ноутбука

        :param name: Новое название нотубка

        Примеры:
        >>> laptop = Laptop("Lenovo", "Legion 5 pro", "12345", "Черный", 15.6, 2.4)
        >>> laptop.rename("MSI")
        """
        if not isinstance(name, str):
            raise TypeError("Название ноутбука должно быть типа str")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
