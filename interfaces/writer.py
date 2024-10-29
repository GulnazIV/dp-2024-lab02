from abc import ABC, abstractmethod


class IWriter(ABC):
    """
    Интерфейс Writer
    Определяет метод для записи сообщений
    """

    @abstractmethod
    def write(self, message: str) -> None:
        """
        Абстрактный метод записи сообщения
        :param message: cообщение для записи
        """
        raise NotImplemented
