import time,logging,os,datetime,traceback
from functools import wraps

path = './log'

class Logger:
    def __init__(self):
        self.logs = {}  # 存放根据文件名生成的日志对象
        self.format = logging.Formatter('%(asctime)s-%(levelname)s: %(message)s')
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(logging.DEBUG)
        self.stream_handler.setFormatter(self.format)
        if not os.path.exists(path):
            os.mkdir(path)

    def getlog(self, filename):
        self.file_handler = logging.FileHandler(filename="{}/{}-{}.log".format(path, filename, datetime.date.today()),
                                                mode='a')
        self.file_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(self.format)
        _log = logging.getLogger(filename)
        _log.setLevel('DEBUG')
        _log.addHandler(self.file_handler)
        _log.addHandler(self.stream_handler)

        return _log


def logger(fname):
    _log = Logger().getlog(fname)
    def out_log(func):
        @wraps(func)
        def callfunc(*args, **kwargs):
            t_start = time.time()
            try:
                res = func(*args, **kwargs)
                t_end = time.time()
                _log.debug(f"执行完成: {func.__name__} 调用参数: {args if len(args) > 0 else 'None'} {kwargs if len(kwargs) > 0 else 'None'} 返回值: {res} 执行耗时: {t_end-t_start} 秒")
                return res
            except Exception as e:
                _log.error(f"执行异常: {func.__name__} 调用参数: {args if len(args) > 0 else 'None'} {kwargs if len(kwargs) > 0 else 'None'} 异常信息: {e}"
                           f"\n{traceback.format_exc()}")
        return callfunc
    return out_log


@logger('Runtime')
def func1(name):
    print('调用func1')
    for i in range(100):
        time.sleep(0.01)
    return name
@logger('uuu1')
def func2():
    print(2)

func1()
func2()