import threading


class Singleton:
    """
    Класс Singleton.
    Обеспечивает потокобезопасную запись логов в файл.
    """

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args):
        """
        Метод для создания нового экземпляра класса.
        :param args: аргументы, передаваемые при создании экземпляра
        :return: единственный экземпляр класса
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
