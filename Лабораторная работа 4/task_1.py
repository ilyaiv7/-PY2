import doctest


class Headphones:
    """
    Создание и подготовка к работе объекта "Наушники"

    :param brand_name: название бренда
    :param model: название модели
    :param construction: конструкция
    :param microphone: наличие микрофона.
    True - микрофон пристуствует.
    False - микрофон отсутсвует
    :paran noise_reduction: Наличие шумоподавления.
    True - шумоподавление присутсвует,
    False - шумоподавление отсуствует

    Атрибуты brand_name, model, construction, microphone, noise_reduction
    являются неизменными. Открыты только для чтения

    Примеры:
    >>> headphones = Headphones(brand_name='Huawei', model='Freebuds 4i', \
        construction='Внутриканальные', microphone=True, noise_reduction=True)
    """

    def __init__(self, brand_name: str, model: str, construction: str,
                 microphone: bool, noise_reduction: bool):
        if not isinstance(brand_name, str):
            raise TypeError("атрибут brand_name должен быть типа str")
        self._brand_name = brand_name
        if not isinstance(model, str):
            raise TypeError("атрибут model должен быть типа str")
        self._model = model
        if not isinstance(construction, str):
            raise TypeError("атрибут construction должен быть типа str")
        self._construction = construction
        if not isinstance(microphone, bool):
            raise TypeError("атрибут microphone должен быть типа bool")
        self._microphone = microphone
        if not isinstance(noise_reduction, bool):
            raise TypeError("атрибут noise_reduction должен быть типа bool")
        self._noise_reduction = noise_reduction

    @property
    def brand_name(self):
        return self._brand_name

    @property
    def model(self):
        return self._model

    @property
    def construction(self):
        return self._construction

    @property
    def microphone(self):
        return self._microphone

    @property
    def noise_reduction(self):
        return self._noise_reduction

    @property
    def presence_microphone(self) -> bool:
        """
        Свойство, которое проверяет наличие микрофона в наушниках

        :return: True - микрофон присутсвует, False - микрофон отсутсвует
        """
        if self.microphone is True:
            return True
        else:
            return False

    @property
    def presence_noise_reduction(self) -> bool:
        """
        Свойство, которое проверяет наличие шумоподавления в наушниках

        :return: True - шумоподавление присутсвует, False - шумоподавление отсутсвует
        """
        if self.noise_reduction is True:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f'Наушники {self.brand_name} {self.model}'

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}(brand_name={self.brand_name!r}, '
                f'model={self.model!r}, construction={self.construction!r}, '
                f'microphone={self.microphone!r}, '
                f'noise_reduction={self.noise_reduction!r})')

    def connection_gadjet(self) -> None:
        """
        Функция, которая соединяет наушники с другим устройством.
        В классе "Headphones" методу "connection_gadjet" не нужно
        знать каким имено образом происходит соединение.

        Примеры:
        >>> headphones = Headphones(brand_name='Huawei', model='Freebuds 4i', \
        construction='Внутриканальные', microphone=True, noise_reduction=True)
        >>> headphones.connection_gadjet()
        """
        ...

    def switch_noise_reduction(self, mode: int) -> None:
        """
        Функция, которая позволяет переключаться между режимами шумоподавления
        при условии, что наушники поддерживают шумоподавление

        :param mode: 0 - шумоподавление выключено. 1 - минимальное шумоподавление.
        2 - среднее шумоподавление. 3 - максимальное шумоподавление.

        Примеры:
        >>> headphones = Headphones(brand_name='Huawei', model='Freebuds 4i', \
        construction='Внутриканальные', microphone=True, noise_reduction=True)
        >>> headphones.switch_noise_reduction(mode=1)
        """


class WiredHeadphones(Headphones):
    """
    Создание и подготовка к работе объекта "Проводные наушники"

    :param brand_name: название бренда
    :param model: название модели
    :param construction: конструкция
    :param microphone: наличие микрофона.
    True - микрофон пристуствует.
    False - микрофон отсутсвует
    :paran noise_reduction: Наличие шумоподавления.
    True - шумоподавление присутсвует,
    False - шумоподавление отсуствует
    :param wire_material: материал провода
    :param wire_length: длина провода в миллиметрах
    :param connection_type: тип соединения

    Атрибуты brand_name, model, construction, microphone, noise_reduction,
    wire_material, wire_length, connection_type являются неизменными.
    Открыты только для чтения

    Примеры:
    >>> wiredheadphones = WiredHeadphones(brand_name='JBL', model='T205', \
        construction='Вкладыши', microphone=True, noise_reduction=False, \
        wire_material='Силикон', wire_length=750, connection_type='3.5mm jack')
    """

    def __init__(self, brand_name: str, model: str, construction: str,
                 microphone: bool, noise_reduction: bool,
                 wire_material: str, wire_length: int,
                 connection_type: str):
        super().__init__(brand_name, model, construction, microphone,
                         noise_reduction)
        if not isinstance(wire_material, str):
            raise TypeError("Атрибут wire_material должен быть типа str")
        self._wire_material = wire_material
        if not isinstance(wire_length, int):
            raise TypeError("Атрибут wire_length должен быть типа int")
        if wire_length <= 0:
            raise ValueError("Атрибут wire_length должен быть больше нуля")
        self._wire_length = wire_length
        if not isinstance(connection_type, str):
            raise TypeError("Атрибут connection_type должен быть типа str")
        self._connection_type = connection_type

    @property
    def wire_material(self):
        return self._wire_material

    @property
    def wire_length(self):
        return self._wire_length

    @property
    def connection_type(self):
        return self._connection_type

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}(brand_name={self.brand_name!r}, '
                f'model={self.model!r}, construction={self.construction!r}, '
                f'microphone={self.microphone!r}, '
                f'noise_reduction={self.noise_reduction!r}, '
                f'wire_material={self.wire_material!r}, '
                f'wire_length={self.wire_length!r}, '
                f'connection_type={self.connection_type!r})')

    def connection_gadjet(self) -> None:
        """
        Функция, которая соединяет наушники с другим устройством.
        Данный метод перегружается в дочернем классе "WiredHeadphones",
        так как необходимо учесть атрибут экземпляра класса "connection_type"

        Примеры:
        >>> wiredheadphones = WiredHeadphones(brand_name='JBL', model='T205', \
        construction='Вкладыши', microphone=True, noise_reduction=False, \
        wire_material='Силикон', wire_length=750, connection_type='3.5mm jack')
        >>> wiredheadphones.connection_gadjet()
        """
        ...


class WirelessHeadphones(Headphones):
    """
    Создание и подготовка к работе объекта "Беспроводные наушники"

    :param brand_name: название бренда
    :param model: название модели
    :param construction: конструкция
    :param microphone: наличие микрофона.
    True - микрофон пристуствует.
    False - микрофон отсутсвует
    :param noise_reduction: Наличие шумоподавления.
    True - шумоподавление присутсвует,
    False - шумоподавление отсуствует
    :param bluetooth: версия bluetooth
    :param battery_life: время автономной работы.
    Измеряется в часах
    :param connection_range: радиус действия bluetooth

    Атрибуты brand_name, model, construction, microphone, noise_reduction,
    bluetooth, battery_life, connection_range являются неизменными.
    Открыты только для чтения

    Примеры:
    >>> wirelessheadphones = WirelessHeadphones(brand_name='Huawei', model='Freebuds 4i', \
        construction='Внутриканальные', microphone=True, noise_reduction=True, \
        bluetooth=5.0, battery_life=5, connection_range=10.0)
    """

    def __init__(self, brand_name: str, model: str, construction: str,
                 microphone: bool, noise_reduction: bool,
                 bluetooth: float, battery_life: int,
                 connection_range: float):
        super().__init__(brand_name, model, construction, microphone,
                         noise_reduction)
        if not isinstance(bluetooth, float):
            raise TypeError("Атрибут bluetooth должен быть типа float")
        self._bluetooth = bluetooth
        if not isinstance(battery_life, int):
            raise TypeError("Атрибут battery_life должен быть типа int")
        if battery_life <= 0:
            raise ValueError("Атрибут battery_life должен быть больше нуля")
        self._battery_life = battery_life
        if not isinstance(connection_range, float):
            raise TypeError("Атрибут connection_range должен быть типа float")
        if connection_range <= 0:
            raise ValueError("Атрибут connection_range должен быть больше нуля")
        self._connection_range = connection_range

    @property
    def bluetooth(self):
        return self._bluetooth

    @property
    def battery_life(self):
        return self._battery_life

    @property
    def connection_range(self):
        return self._connection_range

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}(brand_name={self.brand_name!r}, '
                f'model={self.model!r}, construction={self.construction!r}, '
                f'microphone={self.microphone!r}, '
                f'noise_reduction={self.noise_reduction!r}, '
                f'bluetooth={self.bluetooth!r}, '
                f'battery_life={self.battery_life!r}, '
                f'connection_range={self.connection_range!r})')

    def connection_gadjet(self) -> None:
        """
        Функция, которая соединяет наушники с другим устройством.
        Данный метод перегружается в дочернем классе "WirelessHeadphones",
        так как необходимо учесть атрибут экземпляра класса "bluetooth"

        Примеры:
        >>> wirelessheadphones = WirelessHeadphones(brand_name='Huawei', model='Freebuds 4i', \
        construction='Внутриканальные', microphone=True, noise_reduction=True, \
        bluetooth=5.0, battery_life=5, connection_range=10.0)
        >>> wirelessheadphones.connection_gadjet()
        """
        ...

    def battery_charge(self) -> str:
        """
        Функция, которая позволяет узнать заряд батареи

        return: возвращает заряд батареи в процентах

        Примеры:
        >>> wirelessheadphones = WirelessHeadphones(brand_name='Huawei', model='Freebuds 4i', \
        construction='Внутриканальные', microphone=True, noise_reduction=True, \
        bluetooth=5.0, battery_life=5, connection_range=10.0)
        >>> wirelessheadphones.battery_charge()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
