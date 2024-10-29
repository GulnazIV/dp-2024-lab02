import os

from components.logger import Logger
from components.log_strategy import ConsoleLog, FileLog, UpperCaseFileLog

from const.log_levels import Levels

if __name__ == "__main__":
    logger = Logger(ConsoleLog())
    logger.log(Levels.INFO.value, "Application started successfully")

    directory = "log"
    os.makedirs(directory, exist_ok=True)

    logger.set_log_strategy(FileLog(directory))
    logger.log(Levels.INFO.value, "Application started successfully")

    logger.set_log_strategy(UpperCaseFileLog(directory))
    logger.log(Levels.INFO.value, "Application started successfully")
