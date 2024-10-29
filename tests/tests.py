import unittest
from datetime import datetime
from unittest.mock import patch, mock_open

from const.log_levels import Levels
from components.log_strategy import FileLog, UpperCaseFileLog, ConsoleLog
from components.logger import Logger


class LoggerStrategyTestCase(unittest.TestCase):

    def setUp(self):
        """
        Подготавливает переменные для тестов
        """

        self.message = "Test message"
        self.level = Levels.INFO.value

    @patch("builtins.print")
    def test_write_console_log(self, mock_print):
        """
        Тестирует запись сообщения в консоль.
        """

        logger = ConsoleLog()
        logger.write(self.message)
        mock_print.assert_called_once_with("Test message")

    @patch("builtins.open", new_callable=mock_open)
    def test_write_file_log(self, mock_open):
        """
        Тестирует запись сообщения в файл
        """

        log_directory = "log"
        logger = Logger(FileLog(log_directory))
        logger.log(self.level, self.message)

        handle = mock_open()
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"{time_stamp} [{self.level}] {self.message}"
        handle.write.assert_called_once_with(formatted_message)

    @patch("builtins.open", new_callable=mock_open)
    def test_upper_case_file_log(self, mock_open):
        """
        Тестирует запись сообщения в файл в верхнем регистре
        """

        log_directory = "test"
        logger = Logger(UpperCaseFileLog(log_directory))
        logger.log(self.level, self.message)

        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"{time_stamp} [{self.level}] {self.message.upper()}"
        mock_open().write.assert_called_once_with(formatted_message)


if __name__ == "__main__":
    unittest.main()
