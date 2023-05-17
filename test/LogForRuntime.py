import time,logging,os,datetime
from functools import wraps

path = './log'

logs = {} #存放根据文件名生成的日志对象

class Logger:
    def __init__(self):
        self.format = logging.Formatter('%(asctime)s-%(levelname)s: %(message)s')
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(logging.DEBUG)
        self.stream_handler.setFormatter(self.format)
        if not os.path.exists(path):
            os.mkdir(path)

    def getlog(self, filename):
        if filename in logs.keys():
            return logs[filename]
        else:
            self.file_handler = logging.FileHandler(filename="./log/{}-{}.log".format(filename, datetime.date.today()),
                                                    mode='a')
            self.file_handler.setLevel(logging.DEBUG)
            self.file_handler.setFormatter(self.format)
            _log = logging.getLogger(filename)
            _log.setLevel('DEBUG')
            _log.addHandler(self.file_handler)
            _log.addHandler(self.stream_handler)
            logs[filename] = _log
            return _log


def logger(fname):
    _log = Logger().getlog(fname)
    def out_log(func):
        @wraps(func)
        def infunc(*args, **kwargs):
            t_start = time.time()
            res = func(*args, **kwargs)
            t_end = time.time()
            _log.debug('执行函数: {} 调用参数: {} {} 返回值: {} 执行耗时: {} 秒'.format
                       (func.__name__, args if len(args)>0 else 'None', kwargs if len(kwargs)>0 else 'None', res, t_end-t_start))
        return infunc
    return out_log

@logger('Runtime')
def func1(name):
    print('调用func1')
    for i in range(100):
        time.sleep(0.01)
    return name

@logger('Runtime')
def func():
    print('func2 runtime')

@logger('Runtime')
def fff():
    print('fff test')

if __name__ == '__main__':
    '''
        from xxx.py import logger
        @logger(logfilename)
        def func():
            pass
    '''
    func1('527sdss')
    func()
    fff()