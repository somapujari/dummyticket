import inspect
import logging


class LogGen:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        file = logging.FileHandler(r'C:\Users\Dell\PycharmProjects\dummyticket\logs\logsdummy.log')
        formatter = logging.Formatter('%(message)s : %(asctime)s : %(name)s : %(funcName)s : %(lineno)s')
        file.setFormatter(formatter)
        logger.addHandler(file)
        return logger
