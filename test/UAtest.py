"""
    opc-ua类
    实现工业机器交互
    opc-ua安装使用方式：
        pip3 install PyQt5
        pip3 install PyQt5-tools
        pip install opcua
        pip3 install opcua-client
        pip3 install opcua-modeler
    opc-ua 服务端调试工具：
        python环境下 cmd 运行 opcua-modeler
    opc-ua 客户端调试工具：
        python环境下 cmd 运行 opcua-client
"""
import logging
import threading
import time
from functools import wraps

# from config.config import config
from opcua import Client, ua, Node

logger = logging.getLogger('default')


def read_lock_func(func):
    @wraps(func)
    def run(*args, **kwargs):
        with threading.Lock():
            res = func(*args, **kwargs)
        return res

    return run


def write_lock_func(func):
    @wraps(func)
    def run(*args, **kwargs):
        with threading.Lock():
            res = func(*args, **kwargs)
        return res

    return run


# 自定义回调函数
class SubHandler(object):
    def datachange_notification(self, node, val, attr):
        logger.info(f"data change event: node:{node} value:{val} ")


class EnumType:
    uaBool = ua.VariantType.Boolean
    uaString = ua.VariantType.String
    uaInt16 = ua.VariantType.Int16
    uaInt32 = ua.VariantType.Int32
    uaUInt32 = ua.VariantType.UInt32
    uaFloat = ua.VariantType.Float
    uaByte = ua.VariantType.Byte


class OpcClient:
    """
    OPCUA Client class
    """

    def __init__(self, ip, port, sub_id=None):
        """
        :param ip:  opc server ip
        :param port: opc server port
        :param sub_id: 需要监听的nodeId列表[{node_id:id,handle:handle}]
        """
        self._is_connect = False
        self.ip = ip
        self.port = port
        self.sub_id = sub_id
        self.client = Client("opc.tcp://{}:{}".format(ip, port))
        # self.client.secure_channel_timeout = 10000
        # self.client.session_timeout = 10000
        self.first_connect()
        t = threading.Thread(target=self.check_alive_and_connect_daemon, args=(10,))
        t.setDaemon(True)
        t.start()

    def disconnect(self):
        self.client.disconnect()
        logger.info("client disconnect")

    def first_connect(self):
        tmp = self.__connect__()
        if tmp is False:
            time.sleep(1)
            self.first_connect()
        else:
            self.client.load_type_definitions()
            return True

    def __connect__(self):
        try:
            logger.info("开始创建连接")
            self.client.connect()
        except Exception as e:
            self._is_connect = False
            logger.info("连接失败")
            return False
        self._is_connect = True
        logger.info("连接成功")
        if self.sub_id and len(self.sub_id) > 0:
            for item in self.sub_id:
                logger.info(f"订阅:{item['node_id']}")
                self.create_subscription(item["node_id"], item["handle"])
        return True

    def __check_alive__(self):
        try:
            self.client.send_hello()
        except Exception as e:
            try:
                self.client.disconnect()
            except Exception as c:
                pass
            self._is_connect = False
            return False
        self._is_connect = True
        return True

    def __check_alive_bak__(self):
        res = self.write_by_node_id(config['alive_signal'], 1, EnumType.uaByte)
        if res:
            self._is_connect = True
            # res = self.write_by_node_id(config["make_code_encode"], int(84205), EnumType.uaInt32)
            # print(f"res:{res}")
            return True
        else:
            self._is_connect = False
            return False

    def __check_alive_and_connect__(self):
        with threading.Lock():
            result = self.__check_alive_bak__()
            if result:
                return True
            else:
                logger.info("recv false")
                return self.__connect__()

    def check_alive_and_connect_daemon(self, timedelta):
        """
        保活机制
        :param timedelta: 状态查询时间
        :return:
        """
        while 1:
            self.__check_alive_and_connect__()
            time.sleep(timedelta)

    def create_subscription(self, node_id, node_handler, time_out=300):
        """
        注册监听事件
        :param node_id: node_id,not Node!!!
        :param node_handler:
        :param time_out:
        :return:
        """
        try:
            node = self.get_node(node_id)
        except Exception as e:
            raise Exception("not this node ,please check id!")
        sub = self.client.create_subscription(time_out, node_handler)
        sub.subscribe_data_change(node)

    def get_node(self, node_id):
        """
        获取节点对象
        :param node_id:
        :return:
        """
        try:
            node = self.client.get_node(node_id)
            return node
        except Exception as e:
            raise Exception(f"no this node {node_id}")

    @read_lock_func
    def read_by_node(self, node):
        """
        获取节点对象的值
        """
        if not isinstance(node, Node):
            raise Exception("please pass in the correct parameters")
        return node.get_value()

    @read_lock_func
    def read_by_node_id(self, node_id):
        """
        获取节点对象的值
        """
        node = self.client.get_node(node_id)
        if not isinstance(node, Node):
            raise Exception("please pass in the correct parameters")
        return node.get_value()

    @write_lock_func
    def write_by_node_id(self, node_id, value, ua_type):
        """
        在节点写入值
        :param node_id: 节点对象
        :param value: 写入的值
        :param ua_type: 写入值的ua类型,参照EnumType
        :return:
        """
        try:
            node = self.client.get_node(node_id)
        except Exception as e:
            logger.error(f"写入 获取node:{node_id}失败：{e}")
            return False
        if not isinstance(node, Node):
            raise Exception("please pass in the correct parameters")
        try:
            node.set_attribute(ua.AttributeIds.Value,
                               ua.DataValue(variant=ua.Variant(value=value,
                                                               varianttype=ua_type)))
            return True
        except Exception as e:
            logger.info(f"write error: {e}")
            return False