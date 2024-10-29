from datetime import datetime
from pathlib import Path

from interfaces.writer import IWriter


class ConsoleLog(IWriter):
    """
    Стратегия логирования, которая выводит сообщения в консоль
    """

    def write(self, message: str) -> None:
        """
        Записывает сообщение в консоль
        :param message: сообщение для вывода
        """
        print(message)


class FileLog(IWriter):
    """
    Стратегия логирования, которая записывает сообщения в файл
    """

    def __init__(self, path_directory: str) -> None:
        """
        Инициализирует стратегию логирования в файл и создает файл для логов
        :param path_directory: путь к директории, где будет создан файл логов
        """
        self._create_path_file(path_directory)
        with open(self.path_file, "w"):
            pass

    def write(self, message: str) -> None:
        """
        Записывает сообщение в файл лога
        :param message: сообщение для записи в файл
        """
        with open(self.path_file, "a") as f:
            f.write(message)

    def _create_path_file(self, path_directory: str) -> None:
        """
        Создает путь до файла для логирования в указанной директории
        :param path_directory: путь к директории для создания файла логов
        """
        time_stamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
        file_name = f"DP.P1.{time_stamp}.log"
        self.path_file = Path(path_directory) / file_name


class UpperCaseFileLog(FileLog):
    """
    Стратегия логирования, которая записывает сообщения в файл в верхнем регистре
    """

    def write(self, message: str) -> None:
        """
        Записывает сообщение в верхнем регистре
        :param message: Сообщение для записи в файл
        """
        super().write(message.upper())
