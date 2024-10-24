import os
from abc import ABC, abstractmethod
from datetime import datetime
from module.log_levels import LEVELS

class IStrategyLogger(ABC):
    """
    Интерфейс паттерна Стратегия
    Определяет метод для записи сообщений
    """
    @abstractmethod
    def log(self, message: str) -> None:
        """
        Записывает сообщение.
        :param message: cообщение для записи
        """
        raise NotImplemented


class ConsoleLogStrategy(IStrategyLogger):
    """
    Стратегия логирования, которая выводит сообщения в консоль
    """
    def log(self, message: str) -> None:
        """
        Записывает сообщение в консоль
        :param message: сообщение для вывода
        """
        print(message)


class FileLogStrategy(IStrategyLogger):
    """
    Стратегия логирования, которая записывает сообщения в файл
    """
    def __init__(self, path_directory: str) -> None:
        """
        Инициализирует стратегию логирования в файл и создает файл для логов
        :param path_directory: путь к директории, где будет создан файл логов
        """
        self._create_file(path_directory)
        with open(self.path_file, 'w'):
            pass

    def log(self, message: str) -> None:
        """
        Записывает сообщение в файл лога
        :param message: сообщение для записи в файл
        """
        with open(self.path_file, 'a') as f:
            f.write(message + '\n')

    def _create_file(self, path_directory: str) -> None:
        """
        Создает файл для логирования в указанной директории
        :param path_directory: путь к директории для создания файла логов
        """
        os.makedirs(path_directory, exist_ok=True)
        time_stamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
        self.path_file = f"{path_directory}/DP.P1.{time_stamp}.log"

class UpperCaseFileLogStrategy(FileLogStrategy):
    """
    Стратегия логирования, которая записывает сообщения в файл в верхнем регистре
    """
    def log(self, message: str) -> None:
        """
        Записывает сообщение в верхнем регистре
        (ссылается в родительский класс FileLogStrategy с измененным сообщением)
        :param message: Сообщение для записи в файл
        """
        super().log(message.upper())


class Logger:
    """
    Класс логера, использующий выбранную стратегию логирования.
    """
    _strategy: IStrategyLogger

    def __init__(self, strategy: IStrategyLogger) -> None:
        """
        Инициализирует логер с заданной стратегией логирования
        :param strategy: объект стратегии логирования
        """
        self._strategy = strategy

    def log(self, level: LEVELS, message: str) -> None:
        """
        Записывает сообщение
        :param level: уровень важности сообщения
        :param message: текст сообщения для записи в лог
        """
        time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._strategy.log(f'{time_stamp} [{level.value}] {message}')

