import threading
import time
from threading import Thread

import xlrd
from inspect import getframeinfo, stack

from opcua import Client, ua
# from opcua.ua import VariantType
from UA_Logic import Values, Log

log = Log.logg()

def nprintf(*args,  level = "INFO", end = " "):
    datatime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    caller = getframeinfo(stack()[1][0])
    message = end.join(["{}".format(i) for i in args])
    str = f"{datatime} - {level}:{message}"
    print(str)


def getcolnm(path) -> dict:
    colnm = {}
    '''
    获取点表表头及列码
    '''
    if not path:
        nprintf('空路径')
        raise Exception('空路径')
    try:
        if Values.xl:
            del Values.xl
        Values.xl = xlrd.open_workbook(path, encoding_override=True)
        Values.iolist = Values.xl.sheet_by_name("IO List(点表)")
        iolist = Values.iolist
        for i in range(iolist.ncols):
            for j in range(2):
                if iolist.cell_value(j, i) != '':
                    colnm[iolist.cell_value(j, i)] = i

        nprintf('点表初始化成功！')
        return colnm
    except BaseException as e:
        log.error('点表初始化失败：'+str(e))
        nprintf('点表初始化失败：'+str(e))



def DIauto(uac, cond, value, wtime):
    '''
    :param uac:UAClient实例，Values.cl
    :param cond: 判断条件，最大两个
    :param value: 目标值
    :param wtime: 写点之间的等待时间
    :return:
    '''
    try:
        sheet = Values.iolist
        condi = []

        for k in cond.keys():
            condi.append(k)

        if len(condi) == 1:
            for row in range(2, sheet.nrows):
                if cond[condi[0]] in str(sheet.cell_value(row, Values.colnum[condi[0]])) and 'DI' in sheet.cell_value(row, Values.colnum['I/O类型']):
                    res = uac.set_Value(sheet.cell_value(row, Values.colnum['数据库实例名']) + '.' + sheet.cell_value(row,Values.colnum['属性名']),'PV',int(value))
                    # print(Msg)
                    if res:
                        nprintf(str(sheet.cell_value(row, Values.colnum['设备编号']))+'\t' +sheet.cell_value(row,Values.colnum['属性描述']) +'\t' + sheet.cell_value(row, Values.colnum['比特数值' + str(value) + '描述']))
                    time.sleep(int(wtime))
        elif len(condi) == 2:
            for row in range(2, sheet.nrows):
                if cond[condi[0]] in str(sheet.cell_value(row, Values.colnum[condi[0]])) and cond[condi[1]] in str(sheet.cell_value(row, Values.colnum[condi[1]])) and 'DI' in sheet.cell_value(row, Values.colnum['I/O类型']):
                    res = uac.set_Value(sheet.cell_value(row, Values.colnum['数据库实例名']) + '.' + sheet.cell_value(row,Values.colnum['属性名']),'PV',int(value))
                    # print(Msg)
                    if res:
                        nprintf(str(sheet.cell_value(row, Values.colnum['设备编号']))+'\t' +sheet.cell_value(row,Values.colnum['属性描述']) +'\t' + sheet.cell_value(row, Values.colnum['比特数值' + str(value) + '描述']))
                    time.sleep(int(wtime))
        nprintf('执行完成')
        log.info("完成DI写值")
    except BaseException as e:
        log.error(str(e))
        nprintf(str(e), level='ERROR')


def AIauto(UA, value):
    '''
    根据Values中存放的点表筛选置值
    :param UA: Values.cl
    :param value: 目标值，‘asc’递增，或固定值
    :return:
    '''
    try:
        sheet = Values.iolist
        if value == 'asc':
            sign = 1
            for n in range(2, sheet.nrows):
                if sheet.cell_value(n, Values.colnum['I/O类型']) == 'AI':
                    res = UA.set_Value(sheet.cell_value(n, Values.colnum['数据库实例名'])+'.'+sheet.cell_value(n, Values.colnum['属性名']),
                                        'In_Channel0', float(sign))
                    if res:
                        nprintf(str(sheet.cell_value(n, Values.colnum['设备编号'])), str(sheet.cell_value(n, Values.colnum['设备描述'])),
                          sheet.cell_value(n, Values.colnum['属性描述']))
                    sign += 1
        else:
            for n in range(2, sheet.nrows):
                if sheet.cell_value(n, Values.colnum['I/O类型']) == 'AI':
                    res = UA.set_Value(sheet.cell_value(n, Values.colnum['数据库实例名'])+'.'+sheet.cell_value(n,
                                                                                                            Values.colnum[
                                                                                                                '属性名']),
                                        'In_Channel0', float(value))
                    if res:
                        nprintf(str(sheet.cell_value(n, Values.colnum['设备编号'])), str(sheet.cell_value(n, Values.colnum['设备描述'])),
                          sheet.cell_value(n, Values.colnum['属性描述']))
        nprintf("执行完成")
        log.info('完成AI写入')
    except BaseException as e:
        nprintf('UAClient::AIauto:'+str(e), level='ERROR')
        log.error('UAClient::AIauto:'+str(e))

class SubHandler(object):
    #订阅节点变化响应方法:回调函数
    def datachange_notification(self, node, val, attr):
        try:
            nprintf(f"{Values.sub_node[str(node)][0]} :{node} 值:{val} {Values.iolist.cell_value(Values.sub_node[str(node)][1], Values.colnum[f'比特数值{str(int(val))}描述']) if f'比特数值{str(int(val))}描述' in Values.colnum.keys() else '无对应值描述'}")
        except Exception as e:
            print("回调函数异常", e)

class rcHandler(object):
    def datachange_notification(self, node, val ,attr):
        node = str(node)
        val = int(val)
        nprintf(f'{node} 接收值:{val}')
        try:
            for rc in range(len(Values.rc_subnode[node][val])):
                Values.bcl.write_node(Values.rc_subnode[node][val][rc][0], Values.rc_subnode[node][val][rc][1])
                # v = Values.cl.client.get_node(node)
                # v.set_value(val)
        except BaseException as e:
            nprintf(f"{node} 值 {val} 未配置返校点")


class returncheckHandler(object):
    def datachange_notification(self, node, val, attr):
        node = str(node)
        val = int(val)
        nprintf(f'{node} 接收值:{val} {Values.rc_DOdesp[node][val]}')  # \n执行反校:{Values.rc_subnode[node][val][rc][0]} = {Values.rc_subnode[node][val][rc][1]}
        log.info(f'{node} 接收值：{val} {Values.rc_DOdesp[node][val]}')  # \n执行反校:{Values.rc_subnode[node][val][rc][0]} = {Values.rc_subnode[node][val][rc][1]}
        with threading.Lock():
            try:
                for rc in range(len(Values.rc_subnode[node][val])):
                    Values.bcl.write_node(Values.rc_subnode[node][val][rc][0], Values.rc_subnode[node][val][rc][1])
                    # v = Values.cl.client.get_node(node)
                    # v.set_value(val)
            except BaseException as e:
                nprintf(f"{node} 值 {val} 未配置返校点")
                log.error(f"{node} 值 {val} 未配置返校点 {str(e)}")
            # t = Thread(target=rc_write(node, val))
            # t.start()

# def rc_write(node, val):
#     try:
#         for rc in range(len(Values.rc_subnode[node][val])):
#             Values.cl.write_node(Values.rc_subnode[node][val][rc][0], Values.rc_subnode[node][val][rc][1])
#             # v = Values.cl.client.get_node(node)
#             # v.set_value(val)
#     except BaseException as e:
#         nprintf(f"{node} 值 {val} 未配置返校点")
#         log.error(f"{node} 值 {val} 未配置返校点 {str(e)}")

def createallsub(UA):
    #Values.cl，根据点表O点筛选并保存至Values.sub_node，调用UA的创建订阅
    iolist = Values.iolist
    for i in range(2, iolist.nrows):
        if iolist.cell_value(i, Values.colnum['I/O类型']) in ['DO', 'AO']:
            if not iolist.cell_value(i, Values.colnum['IO合并']):
                node = iolist.cell_value(i, Values.colnum['数据库实例名'])+'.'+iolist.cell_value(i, Values.colnum['属性名'])+'.PV'
                Values.sub_node['ns='+UA.dbunit+';s='+node] = [iolist.cell_value(i,Values.colnum['设备描述'])+'-'+iolist.cell_value(i,Values.colnum['属性描述']), i]
            else:
                channel0 = iolist.cell_value(i, Values.colnum['外部变量名1'])
                channel1 = iolist.cell_value(i, Values.colnum['外部变量名2'])
                if channel0:
                    node = iolist.cell_value(i, Values.colnum['数据库实例名'])+'.'+iolist.cell_value(i, Values.colnum['IO合并'])+'.Out_Channel0'
                    Values.sub_node['ns='+UA.dbunit+';s='+node] = [iolist.cell_value(i,Values.colnum['设备描述'])+'-'+iolist.cell_value(i,Values.colnum['属性描述']),i]
                if channel1:
                    node = iolist.cell_value(i, Values.colnum['数据库实例名'])+'.'+iolist.cell_value(i, Values.colnum['IO合并'])+ '.Out_Channel1'
                    Values.sub_node['ns='+UA.dbunit+';s='+node] = [iolist.cell_value(i, Values.colnum['设备描述']) + '-' + iolist.cell_value(i,
                                                                                                                  Values.colnum['属性描述']),i]

    UA.create_subnode()
    time.sleep(1)
    print('订阅完成')

def checkip(ip:str) ->bool:
    if len(ip) < 7 or len(ip) > 15:
        return False
    ipaddr = ip.split('.')
    if len(ipaddr) != 4:
        return False
    try:
        for i in range(4):
            if int(ipaddr[i]) < 0 or int(ipaddr[i]) > 255:
                return False
    except:
        return False
    return True

class UAclient:
    def __init__(self):
        self.dbunit = ''
        self.client = ''
        self.Hander = SubHandler()
        self.rcHander = returncheckHandler()
        self.returncheckhandler = rcHandler()
        self.rcnodes = []
        self.sub = []
        self.rsub = []
        self.goodcl = False
        self.constatus = False
    

    def getclient(self, uaclient):
        try:
            if not checkip(uaclient['ip']):
                nprintf('ip地址格式错误，请重新输入！', level='ERROR')
                return False
            else:
                self.client = Client("opc.tcp://" + uaclient['ip'] + ":" + uaclient['port'] + "/")
                self.dbunit = uaclient['unit']
                log.info('服务器初始化成功:'+ uaclient['ip']+':'+uaclient['port'])
                nprintf('服务器初始化成功:'+ uaclient['ip']+':'+uaclient['port'])
                return True
        except BaseException as e:
            log.error(str(e))

    def ClientConnect(self):
        try:
            self.client.connect()
            nprintf('服务连接成功！')
            log.info(r'服务连接成功')
            self.constatus = True
            self.goodcl = True
        except BaseException as e:
            nprintf("服务器连接错误:"+str(e), level="ERROR")
            log.error('服务器连接错误:'+ str(e))
            self.constatus = False

    def keepalive(self):
        while Values.winexit:
            if self.goodcl == True:
                try:
                    self.client.get_endpoints()
                except:
                    self.constatus = False
                    log.error('服务断开重连')
                    nprintf('服务断开重连中')
                    if self.sub:
                        nprintf("订阅失效，请重新订阅")
                        self.sub=[]
                        self.su.delete()
                        self.unsub()
                        self.unrcsub()
                    self.ClientConnect()

            time.sleep(5)

    def ClientDisconnect(self):
        try:
            if self.constatus == True:
                self.client.disconnect()
                log.info("断开连接成功！")
                nprintf("断开连接成功！")
                self.constatus = False
                self.goodcl = False
        except BaseException as e:
            nprintf("断开连接失败!"+str(e))
            log.error("断开错误："+str(e))
            self.constatus = False
            self.goodcl = False
    #添加订阅
    # def create_sub(self, timeout=0):
    #     self.su = self.client.create_subscription(timeout, self.Hander)
    #     self.rc = self.client.create_subscription(timeout, self.rcHander)
    #tianjiadingyuedian
    def create_subnode(self, timeout=0):
        self.su = self.client.create_subscription(timeout, self.Hander)
        for node in Values.sub_node.keys():#在公共参数文件获取点并订阅
            try:
                va = self.su.subscribe_data_change(self.client.get_node(node))
                self.sub.append(va)
            except:
                log.error(f'订阅失败： {Values.sub_node[node]}：{node}')

    def rc_subnode(self, timeout=0):
        '''
        根据Values.rc_subnode 使用自动返校回调函数订阅，当接收变位自动调用回调函数返校
        :return:
        '''
        self.rc = self.client.create_subscription(timeout, self.rcHander)
        for node in Values.rc_subnode.keys():
            try:
                var = self.rc.subscribe_data_change(self.client.get_node(node))
                self.rsub.append(var)
            except Exception as e:
                log.error('订阅失败 {} {}'.format(node, str(e)))

    def auto_returncheck(self, timeout = 0):
        self.rc = self.client.create_subscription(timeout, self.rcHander)
        for node in Values.rc_subnode.keys():
            try:
                var = self.rc.subscribe_data_change(self.client.get_node(node))
                self.rsub.append(var)
            except Exception as e:
                log.error('订阅失败 {} {}'.format(node, str(e)))

    #取消全部订阅
    def unsub(self):
        try:
            self.su.delete()
            # for j in range(len(self.rsub)):
            #     self.rc.unsubscribe(self.rsub[j])
            # Values.rc_subnode = {}
            Values.sub_node = {}
            self.sub = []
            nprintf('订阅取消！', level='INFO')
        except BaseException as e:
            log.error(str(e))
    def unrcsub(self):
        try:
            self.rc.delete()
            Values.rc_subnode = {}
            nprintf('订阅取消！', level='INFO')
        except BaseException as e:
            log.error(str(e))

    # 取值，点、属性
    def get_Value(self, node, attr, dbunit = None):
        try:
            if dbunit is None:
                dbunit = self.dbunit
            var = self.client.get_node("ns=" + dbunit + ";s=" + node + "." + attr)
            v = var.get_value()
            nprintf('UAClient::get_Value:'+str(var) + ' = ' + str(v))
            #log.info('UAClient::get_Value:'+str(var) + ' = ' + str(v))
            return v
        except BaseException as e:
            nprintf('UAClient::get_Value:'+str(e), level='ERROR')
            log.error('UAClient::get_Value:'+ str(var) + str(e))  #
            return False
        
    def read_Value(self, node, dbunit = None):
        try:
            if dbunit is None:
                dbunit = self.dbunit
            var = self.client.get_node("ns=" + dbunit + ";s=" + node)
            v = var.get_value()
            nprintf('UAClient::read_Value:'+str(var) + ' = ' + str(v))
            #log.info('UAClient::get_Value:'+str(var) + ' = ' + str(v))
            return v
        except BaseException as e:
            nprintf('UAClient::read_Value:'+str(e), level='ERROR')
            log.error('UAClient::get_Value:'+ str(var) + str(e))  #
            return False

    # 写值，点、属性、值
    def set_Value(self, node, attr, value, dbunit = None) -> bool:
        try:
            if dbunit is None:
                dbunit = self.dbunit
            var = self.client.get_node("ns=" + dbunit + ";s=" + node + "." + attr)
            var.set_attribute(ua.AttributeIds.Value,
                               ua.DataValue(variant=ua.Variant(value=value,
                                                               varianttype=var.get_data_type_as_variant_type())))
            #var.set_value(value)
            nprintf(str(var) + ' = ' + str(value))
            #log.info(str(var) + ' = ' + str(value))
            return True
        except BaseException as e:
            nprintf('UAClient::set_Value:' + str(e), level='ERROR')
            log.error('UAClient::set_Value:' + str(var) + str(e))
            return False

    def write_Value(self, node, value, dbunit = None) -> bool:
        try:
            if dbunit is None:
                dbunit = self.dbunit
            var = self.client.get_node("ns=" + dbunit + ";s=" + node)
            var.set_attribute(ua.AttributeIds.Value,
                               ua.DataValue(variant=ua.Variant(value=value,
                                                               varianttype=var.get_data_type_as_variant_type())))
            #var.set_value(value)
            nprintf(str(var) + ' = ' + str(value))
            #log.info(str(var) + ' = ' + str(value))
            return True
        except BaseException as e:
            nprintf('UAClient::write_Value:' + str(e), level='ERROR')
            log.error('UAClient::write_Value:' + str(var) + str(e))
            return False

    def read(self, node, attr):
        try:
            var = self.client.get_node(node + "." + attr)
            return var.get_value()
        except BaseException as e:
            print("UAClient-read ERROR!", e)

    def write(self, node, attr, value):
        try:
            var = self.client.get_node(node + "." + attr)
            var.set_value(value)
            nprintf(str(var) + ' = ' + str(value))
        except BaseException as e:
            nprintf("UAClient-write ERROR!", e)

    def write_node(self, node, value):
        try:
            var = self.client.get_node(node)
            var.set_attribute(ua.AttributeIds.Value, ua.DataValue(variant=ua.Variant(value=value, varianttype=var.get_data_type_as_variant_type())))
            #log.info(f'写点：{node} = {value}')
            nprintf(f'写点：{node} = {value}')
        except BaseException as e:
            nprintf(f'写点错误:{str(e)}{str(node)} = {value}', level='ERROR')
            log.error(f'写点错误:{str(e)}{str(node)} = {value}')

    def Oreset(self):
        ...

    def get_description(self, node, dbunit = None):
        if dbunit is None:
            dbunit = self.dbunit
        try:
            var = self.client.get_node(node)
            return var.get_description()
        except:
            nprintf("获取描述失败", level="ERROR")
