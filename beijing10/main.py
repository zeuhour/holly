from Logic import seqctrl
from UA_Logic import Values, UAClient
from global_values import dbunit, socname
cl = []
threads = []

def analy(unitstr):
    return unitstr.replace(' ','').split(',')

Values.uaclient = {
    'unit':'3202',
    'ip':'172.120.122.65',
    'port':'48010'
}
Values.cl.getclient(Values.uaclient)
Values.cl.ClientConnect()

unit = analy(dbunit) #需赋值
socname = analy(socname)
soc = []
for i in range(len(unit)):
    soc.append(seqctrl())
    soc[i].unit_init(unit[i])
    soc[i].get_socnode(socname[i])
    soc[i].status_init()
    soc[i].seq_ctrl()

