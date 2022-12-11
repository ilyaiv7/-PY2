import doctest


class PenBox:
    def __init__(self, color: str, size: str, capacity: int):
        """
        Создание и подготовка к работе обЪекта "Пинал"

        :param color: Цвет пинала
        :param size: Размер пинала
        :param capacity: Вместимость ручек в пинале

        Примеры:
        >>> penbox = PenBox("black", "L", 10)
        """

        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        self.color = color

        if not isinstance(size, str):
            raise TypeError("Размер должен быть типа str")
        if size not in ("S", "M", "L", "XL"):
            raise ValueError('Размер пинала может принимать только следуюзие значения: "S", "M", "L", "XL"')
        self.size = size

        if not isinstance(capacity, int):
            raise TypeError("Вместимость ручек в пинале должна быть типа int")
        if capacity < 1:
            raise ValueError("Любой пинал может вместить в себя как минимум 1 ручку")
        self.capacity = capacity

    def open(self) -> None:
        """
        Функция, которая открывает пинал

        Примеры:
        >>> penbox = PenBox("black", "L", 10)
        >>> penbox.open()
        """
        ...

    def is_inside_pen(self) -> int:
        """
        Функиця, которая проверяет сколько ручек лежит в пинале

        :return: Возвращает количество ручек в пинале

        Примеры:
        >>> penbox = PenBox("black", "L", 10)
        >>> penbox.is_inside_pen()
        """
        ...

    def put_pens(self, amount: int) -> None:
        """
        Функция, которая добавляет ручки в пинал в количестве amount штук

        :param amount: Сколько ручек положить в пинал

        Примеры:
        >>> penbox = PenBox("black", "L", 10)
        >>> penbox.put_pens(3)
        """
        if not isinstance(amount, int):
            raise TypeError("Количество ручек, которые хотим положить в пинал, должно быть типа int")
        if amount < 1:
            raise ValueError("Количество ручек, которые хотим положить в пинал не может быть меньше 1 шт")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
