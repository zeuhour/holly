import logging,datetime,os
from logging import StreamHandler, FileHandler
from logging.handlers import TimedRotatingFileHandler

def logg():
    logger = logging.getLogger(__name__)

    # 设置为DEBUG级别
    logger.setLevel(logging.DEBUG)
    format = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    # 标准流处理器，设置的级别为WARNING
    # stream_handler = StreamHandler()
    # stream_handler.setLevel(logging.DEBUG)
    # stream_handler.setFormatter(format)
    # logger.addHandler(stream_handler)
    path = './log'
    if not os.path.exists(path):
        os.mkdir(path)
    # 文件处理器，设置的级别为INFO
    file_handler = TimedRotatingFileHandler(filename="./log/debuglog.log", when='midnight', interval=1, backupCount=7)
    file_handler.suffix = "%Y-%m-%d"
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(format)
    logger.addHandler(file_handler)

    return logger
