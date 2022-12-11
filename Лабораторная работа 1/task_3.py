import doctest


class Matryoshka:
    def __init__(self, number: int, color: str, production: str, x: float, y: float):
        """
        Создание и подготовка к работе объекта "Матрешка"

        :param number: Количество матрешек в одной игрушке
        :param color: Основной цвет матрешки
        :param production: Город где произвели матрешку
        :param x: декартова координата на оси абсцисс, которая определяет положение матрешки в пространстве
        :param y: декартова координата на оси ординат, которая определяет положение матрешки в пространстве

        Пример:
        >>> matryoska = Matryoshka(5, "красный", "Тверь", 0.0, 0.0)
        """

        if not isinstance(number, int):
            raise TypeError("Количество матрешок должно быть типаы int")
        if number < 2:
            raise ValueError("Матрешка как миниму должна содержать в себе еще одну матрешку")
        self.number = number

        if not isinstance(color, str):
            raise TypeError("Основной цвет матрешки должен быть типа str")
        self.color = color

        if not isinstance(production, str):
            raise TypeError("Город, где производят матрешки, должен быть типа str")
        self.production = production

        if not isinstance(x, float):
            raise TypeError("Координата x должна быть типа float")
        self.x = x

        if not isinstance(y, float):
            raise TypeError("Координата y должна быть типа float")
        self.y = y

    def disassemble(self, num: int) -> None:
        """
        Функция, которая позволяет разобрать матрешку до определенной матрешки внутри одной матрешки

        :param num: Номер матрешки до которой необходимо разобрать матрешку

        Пример:
        >>> matryoska = Matryoshka(5, "красный", "Тверь", 0.0, 0.0)
        >>> matryoska.disassemble(3)
        """
        if not isinstance(num, int):
            raise TypeError("Номер матрешки, до которой необходимо разобрать матрешку должен быть типа int")
        if num > self.number:
            raise ValueError("Номер матрешки, до которой необходимо разобрать матрешку должен быть меньше, чем количество матрешек")
        ...

    def moving(self, delta_x: float, delta_y: float) -> dict:
        """
        Функция, которая позволяет переместить матрешку в пространстве

        :param delta_x: Расстояние, на которое надо переместить матрешку относительно старого положения на оси абсцисс
        :param delta_y: Расстояние, на которое надо переместить матрешку относительно старого положения на оси ординат

        :return: {x: новая координата на оси абсцисс, y: новая координата на оси ординат}

        Пример:
        >>> matryoska = Matryoshka(5, "красный", "Тверь", 0.0, 0.0)
        >>> matryoska.moving(3.0, 7.0)
        """
        if not isinstance(delta_x, float):
            raise TypeError("Координата delta_x должна быть типа float")
        if not isinstance(delta_y, float):
            raise TypeError("Координата delta_y должна быть типа float")
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
