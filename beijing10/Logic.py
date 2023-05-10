import re, math
from UA_Logic import Values
from beijing10.global_values import attribute, keyword_close, keyword_open, device_open, device_close, precondition


class seqctrl:
    def __init__(self):
        self.socnode = []  # 顺控设备实例名
        self.node_logic = []  # 顺控设备遥控逻辑名
        # socvalue = []  #
        self.device_status = []  # 顺控设备预期状态描述
        self.client = Values.cl  # 服务端实例
        self.num = 0  # 顺控卡片设备数量
        self.cmdlist = {
            '送电点': [],
            '停电点': [],
            '送电值': [],
            '停电值': [],
            '送电DO': [],
            '送电DO值': [],
            '停电DO': [],
            '停电DO值': []
        }
        self.dbunit = ''

    def unit_init(self, dbunit):
        self.dbunit = dbunit

    def get_socnode(self, socname):
        self.num = int(self.client.get_Value(socname, attribute["卡片设备数"], dbunit=self.dbunit))
        self.socnode = self.client.get_Value(socname, attribute['顺控设备ID'], dbunit=self.dbunit)[:self.num]
        self.device_status = self.client.get_Value(socname, attribute["预期值描述"], dbunit=self.dbunit)[:self.num]

        for i in range(self.num):
            self.node_logic.append(self.client.read(self.socnode[i], attribute["遥控逻辑名"]))

        for i in range(self.num):
            checkjs = self.client.get_Value(self.node_logic[i], attribute["反校表达式"], dbunit=self.dbunit)
            checkkwd = self.client.get_Value(self.node_logic[i], attribute["反校关键字"], dbunit=self.dbunit)
            outjs = self.client.get_Value(self.node_logic[i], attribute["控制表达式"], dbunit=self.dbunit)
            outkwd = self.client.get_Value(self.node_logic[i], attribute["控制关键字"], dbunit=self.dbunit)

            # 反校点解析
            for j in range(len(checkkwd)):
                if checkkwd[j] == None:
                    break
                if checkkwd[j] in keyword_open:
                    if 'Macs_RD' not in checkjs[j]:
                        continue
                    jug: list = re.split('\$\$|\|\|', checkjs[j])
                    for k in range(len(jug)):
                        jug[k] = jug[k].split('.')
                        jug[k][2] = jug[k][2].strip()
                        jug[k][2] = int(jug[k][2][-1:])
                        jug[k].pop(0)

                    n = []
                    v = []
                    for z in range(len(jug)):
                        n.append(jug[z][0])
                        v.append(int(jug[z][1]))
                    self.cmdlist['停电点'].append(n)
                    self.cmdlist['停电值'].append(v)

                elif checkkwd[j] in keyword_close:
                    if 'Macs_RD' not in checkjs[j]:
                        continue
                    jug = re.split('\$\$|\|\|', checkjs[j])
                    for k in range(len(jug)):
                        jug[k] = jug[k].split('.')
                        jug[k][2] = jug[k][2].strip()
                        jug[k][2] = int(jug[k][2][-1:])
                        jug[k].pop(0)

                    n = []
                    v = []
                    for z in range(len(jug)):
                        n.append(jug[z][0])
                        v.append(int(jug[z][1]))
                    self.cmdlist['送电点'].append(n)
                    self.cmdlist['送电值'].append(v)

            # 遥控点解析
            for j in range(len(outkwd)):
                if outkwd[j] == None:
                    break
                if outkwd[j] in keyword_open:
                    nod = outjs[j]
                    nod = nod.split('.')
                    nod[2] = nod[2].strip()
                    nod[2] = int(nod[2][-2:][:1])
                    nod.pop(0)

                    self.cmdlist['停电DO'].append(nod[0])
                    self.cmdlist['停电DO值'].append(int(nod[1]))

                if outkwd[j] in keyword_close:
                    nod = outjs[j]
                    nod = nod.split('.')
                    nod[2] = nod[2].strip()
                    nod[2] = int(nod[2][-2:][:1])
                    nod.pop(0)

                    self.cmdlist['送电DO'].append(nod[0])
                    self.cmdlist['送电DO值'].append(int(nod[1]))

    # 初始化Values.rc_subnode自动返校
    def status_init(self):
        for i in range(len(self.socnode)):
            Values.rc_subnode[f"{self.socnode[i]}.{self.cmdlist['送电DO'][i]}.Out_Channel0"] = {
                int(self.cmdlist['送电DO值'][i]): []}
            Values.rc_DOdesp[f"{self.socnode[i]}.{self.cmdlist['送电DO'][i]}.Out_Channel0"] = {
                int(self.cmdlist['送电DO值'][i]): "合闸"}
            Values.rc_subnode[f"{self.socnode[i]}.{self.cmdlist['停电DO'][i]}.Out_Channel0"] = {
                int(self.cmdlist['停电DO值'][i]): []}
            Values.rc_DOdesp[f"{self.socnode[i]}.{self.cmdlist['停电DO'][i]}.Out_Channel0"] = {
                int(self.cmdlist['停电DO值'][i]): "分闸"}
            for j in range(len(self.cmdlist['送电点'][i])):
                Values.rc_subnode[f"{self.socnode[i]}.{self.cmdlist['送电DO'][i]}.Out_Channel0"][
                    int(self.cmdlist['送电DO值'][i])].append(
                    [f"{self.socnode[i]}.{self.cmdlist['送电点'][i][j]}.PV", int(self.cmdlist['送电值'][i][j])])
                Values.rc_subnode[f"{self.socnode[i]}.{self.cmdlist['停电DO'][i]}.Out_Channel0"][
                    int(self.cmdlist['停电DO值'][i])].append(
                    [f"{self.socnode[i]}.{self.cmdlist['停电点'][i][j]}.PV", int(self.cmdlist['停电值'][i][j])])

        for key in precondition.keys():
            self.client.set_Value(key, 'PV', precondition[key], dbunit=self.dbunit)

    # 执行

    def seq_ctrl(self):
        for i in range(self.num):
            if self.device_status[i] in device_open:
                if self.socnode[i] not in self.socnode[:i]:
                    if len(self.cmdlist['送电点'][i]) > 1:
                        for j in range(len(self.cmdlist['送电点'][i])):
                            self.client.write(self.socnode[i] + '.' + self.cmdlist['送电点'][i][j], 'PV',
                                              self.cmdlist['送电值'][i][j])
                        self.client.write(self.socnode[i] + '.' + self.cmdlist['停电DO'][i], 'Out_Channel0',
                                          int(math.fabs(self.cmdlist['停电DO值'][i] - 1)))
                    else:
                        self.client.write(self.socnode[i] + '.' + self.cmdlist['送电点'][i][0], 'PV',
                                          self.cmdlist['送电值'][i][0])
                        self.client.write(self.socnode[i] + '.' + self.cmdlist['停电DO'][i], 'Out_Channel0',
                                          int(math.fabs(self.cmdlist['停电DO值'][i] - 1)))

            elif self.device_status[i] in device_close:
                if self.socnode[i] not in self.socnode[:i]:
                    if len(self.cmdlist['停电点'][i]) > 1:
                        for j in range(len(self.cmdlist['停电点'][i])):
                            self.client.write(self.socnode[i] + '.' + self.cmdlist['停电点'][i][j], 'PV',
                                              self.cmdlist['停电值'][i][j])
                        self.client.write(self.socnode[i] + '.' + self.cmdlist['送电DO'][i], 'Out_Channel0',
                                          int(math.fabs(self.cmdlist['送电DO值'][i] - 1)))
                    else:
                        self.client.write(self.socnode[i] + '.' + self.cmdlist['停电点'][i][0], 'PV',
                                          self.cmdlist['停电值'][i][0])
                        self.client.write(self.socnode[i] + '.' + self.cmdlist['送电DO'][i], 'Out_Channel0',
                                          int(math.fabs(self.cmdlist['送电DO值'][i] - 1)))

        # self.client.rc_subnode()

    #
    #     for i in range(self.num):
    #
    #         for timer in range(2):
    #
    #             if self.device_status[i] in device_open:
    #                 if self.client.read(self.socnode[i] + '.' + self.cmdlist['停电DO'][i], 'Out_Channel0') == self.cmdlist['停电DO值'][i]:
    #                     print(self.cmdlist['停电DO'][i], "已接收目标值", self.cmdlist['停电DO值'][i], self.device_status[i],'\n',end='')
    #                     if len(self.cmdlist['停电点'][i]) > 1:
    #                         for j in range(len(self.cmdlist['停电点'][i])):
    #                             self.client.write(self.socnode[i] + '.' + self.cmdlist['停电点'][i][j], 'PV', self.cmdlist['停电值'][i][j])
    #
    #                     else:
    #                         self.client.write(self.socnode[i] + '.' + self.cmdlist['停电点'][i][0], 'PV', self.cmdlist['停电值'][i][0])
    #
    #                     break
    #
    #             elif self.device_status[i] in device_close:
    #                 if self.client.read(self.socnode[i] + '.' + self.cmdlist['送电DO'][i], 'Out_Channel0') == self.cmdlist['送电DO值'][i]:
    #                     print(self.cmdlist['送电DO'][i], "已接收目标值", self.cmdlist['送电DO值'][i], self.device_status[i],'\n',end='')
    #                     if len(self.cmdlist['送电点'][i]) > 1:
    #                         for j in range(len(self.cmdlist['送电点'][i])):
    #                             self.client.write(self.socnode[i] + '.' + self.cmdlist['送电点'][i][j], 'PV', self.cmdlist['送电值'][i][j])
    #                     else:
    #                         self.client.write(self.socnode[i] + '.' + self.cmdlist['送电点'][i][0], 'PV', self.cmdlist['送电值'][i][0])
    #                     break
    #
    #             time.sleep(0.3)
