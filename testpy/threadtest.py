from LogForRuntime import logger
import time
@logger
def a():
    for i in range(100):
        print(i, end=' ')
    return True

a()