import os
import unittest
from datetime import datetime
from io import StringIO
import sys
from contextlib import redirect_stdout

from module.log_levels import LEVELS
from main import Logger,FileLogStrategy, UpperCaseFileLogStrategy, ConsoleLogStrategy

class LoggerStrategyTestCase(unittest.TestCase):

    def test_logging_console(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        f = StringIO()
        logger = Logger(ConsoleLogStrategy())
        message = 'Test message'
        with redirect_stdout(f):
            logger.log(LEVELS.INFO, message)

        s = f.getvalue()
        self.assertIn(message, s)

    def test_logging_file(self):
        directory = 'test'
        time_stamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
        file = f"{directory}/DP.P1.{time_stamp}.log"

        logger = Logger(FileLogStrategy(directory))
        message = 'Test message'
        logger.log(LEVELS.INFO, message)

        with open(file, 'r') as f:
            content = f.read().strip()

        self.assertIn(message, content)

    def test_logging_uppercase_file(self):
        directory = 'upper_test'
        time_stamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
        file = f"{directory}/DP.P1.{time_stamp}.log"

        logger = Logger(UpperCaseFileLogStrategy(directory))
        message = 'Test message'
        logger.log(LEVELS.INFO, message)

        with open(file, 'r') as f:
            content = f.read().strip()

        self.assertIn(message.upper(), content)
