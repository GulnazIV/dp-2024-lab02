import threading
from datetime import datetime

from components.singleton import Singleton
from const.log_levels import Levels
from interfaces.writer import IWriter


class Logger(Singleton):
    """
    Класс Логер
    """

    _lock = threading.Lock()

    def __init__(self, log_strategy: IWriter) -> None:
        """
        Инициализирует логер с заданной стратегией логирования
        :param log_strategy: выбранная стратегия логирования
        """
        self._log_strategy = log_strategy

    def set_writer(self, log_strategy: IWriter):
        """
        Изменяет вариант записи сообщения
        :param log_strategy: выбранная стратегия логирования
        """
        self._log_strategy = log_strategy

    def log(self, level: Levels, message: str) -> None:
        """
        Вызывает метод записи выбранной стратегии
        :param level: уровень важности сообщения
        :param message: текст сообщения для записи в лог
        """
        formatted_message = self._format_message(level, message)
        with self._lock:
            self._log_strategy.write(formatted_message)

    def _format_message(self, level: Levels, message: str) -> str:
        """
        Форматирует сообщение
        :param level: уровень важности сообщения
        :param message: текст сообщения для записи в лог
        """
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{time_stamp} [{level}] {message}"
