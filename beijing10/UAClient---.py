import logging,datetime,os
from logging import StreamHandler, FileHandler

l1 = ''
l2 = ''

def logg():
    logger = logging.getLogger('log1')
    logger1 = logging.getLogger('log2')

    # 设置为DEBUG级别
    logger.setLevel(logging.DEBUG)
    logger1.setLevel(logging.DEBUG)
    format = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    # 标准流处理器，设置的级别为WARNING
    stream_handler = StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(format)
    logger.addHandler(stream_handler)
    path = './log'
    if not os.path.exists(path):
        os.mkdir(path)
    # 文件处理器，设置的级别为INFO
    file_handler = FileHandler(filename="./log/{}_log1.log".format(datetime.date.today()), mode='a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(format)

    file_handler1 = FileHandler(filename="./log/{}_log2.log".format(datetime.date.today()), mode='a')
    file_handler1.setLevel(logging.DEBUG)
    file_handler1.setFormatter(format)

    logger.addHandler(file_handler)
    logger1.addHandler(file_handler1)
    global l1, l2
    l1 = logger
    l2 = logger1

logg()
l1.info('11111111')
l2.info('2222222222')
