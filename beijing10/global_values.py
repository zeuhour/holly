dbunit = ''#'2002,1102,1202,1402,1602,1802,2202,2402,2502,2702,2902,3102,3202'#以逗号，分割
socname = ''#'SOC_AZM90TEST,SOC_BGZ90TEST,SOC_SZJ90TEST,SOC_ZCI90TEST,SOC_XTC90TEST,SOC_JDM90TEST,SOC_SYJ90TEST,SOC_SYQ90TEST,SOC_LMQ90TEST,SOC_TJH90TEST,SOC_JTX90TEST,SOC_SJZ90TEST,SOC_JSZ90TEST' #SOC_ZCI90TEST

keyword_open =  ["OPEN","STOP"] #分闸关键字
keyword_close = ["CLOSE","START"] #合闸关键字
device_open =   ["分位"] #装置分闸状态描述（以顺控卡片中为准）
device_close =  ["合位"] #装置合闸状态描述

attribute = {
    "顺控设备ID" : "cmdPreList.szObject",
    "反校表达式" : "ExprReturnCheck_ExpressionJS",
    "反校关键字" : "ExprReturnCheck_KeyWord",
    "控制表达式" : "ExprOutControl_OutPutJS",
    "控制关键字" : "ExprOutControl_KeyWord",
    "遥控逻辑名" : "AppPubBase_Remote_Ctrl.ControlLogicName",
    "卡片设备数" : "uiCmdSize",
    "预期值描述" : "cmdPreList.szExpectStatus"
}
#使能条件
precondition = {
    'LVP_0014.D2SP':1,
    'LVP_0024.D2SP':1,
    'LVP_0034.D2SP':1,
    'LVP_0044.D2SP':1,
    'FJD_0065.DIRL':1,
    'FJD_0075.DIRL':1,
    'ZZ__0060.D2HP':1,
    'ZZ__0060.D2RL':1,
    'ZZ__0070.D2HP':1,
    'ZZ__0070.D2RL':1,
    'LVD20061.D2RL':1,
    'LVD20071.D2RL':1,
    'NLDG0085.D2RL':2,
    'NKNB0K80.D2RL':2,
    'LV__0010.D2HP':1,
    'LV__0010.D2RL':1,
    'LV__0020.D2HP':1,
    'LV__0020.D2RL':1,
    'LV__0030.D2HP':1,
    'LV__0030.D2RL':1,
    'LV__0040.D2HP':1,
    'LV__0040.D2RL':1,
    'LVB_0090.D2RL':1,
    'LVB_0090.D2HP':1,
    'HVNK0822.D2SP':2,
    'HVNK0821.D2SP':2,
    'XHVN0821.D2SP':2,
    'XHVN0822.D2SP':2
}
# precondition = {}