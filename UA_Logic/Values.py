from  UA_Logic.UAClient import UAclient
import xlrd
uaclient = {
    "ip" : "",
    "port" : "",
    "unit" : ""
}
xl = ''
lastpath = './'
#服务UA实例
cl = UAclient()
bcl = UAclient()
#点表路径
filepath = ''
#点表表头及列码
colnum = {}
#服务连接状态（被动）
clstatus = False
#点表xlrd实例
iolist = ''
#已订阅的节点名
sub_node = {} #‘完整点名’：‘设备描述及属性名’
#
'''
    点（xxx.xx.pv)：{
                        值1：[反校点1，反校点2],[目标值1，目标值2],
                        值2：[反校点1，反校点2],[目标值1，目标值2]
                    }
'''
rc_subnode = {}
rc_DOdesp = {}
rc_nodes = {}

winexit = True
