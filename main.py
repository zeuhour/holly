import json

json_head = {
    "packageCount": "45",
    "packageHead": {
        "name": "数据包头", "length": "1472", "default": "0xff", "generate": "true", "dataItem": [
            {
                "message": ["包头", "40byte", "0xff", "数据包头", "0xff"],
                "childCount": "0"
            },
            {
                "message": ["序列号", "4byte", "0x00000001", "序列号+1", "0x00000001"],
                "childCount": "0"
            },
            {
                "message": ["识别号", "1byte", "0x0a", "识别号", "0x0a"],
                "childCount": "0"
            },
            {
                "message": ["编组号", "2byte", "0x0001", "编组号", "0x0001"],
                "childCount": "0"
            },
            {
                "message": ["预留", "15byte", "0xff", "编组号", "0xff"],
                "childCount": "0"
            },
            {
                "message": ["数据包", "1408byte", "0xff", "数据包", "0xff"],
                "childCount": "44",
                "childName": ["62", "coms_002", "reserve", "reserve", "reserve", "reserve", "reserve", "reserve",
                              "reserve", "reserve", "reserve", "reserve", "reserve", "EDCU", "reserve", "atc_090",
                              "atc_091", "atc_092", "atc_093", "atc_094", "atc_095", "reserve", "reserve", "reserve",
                              "reserve", "reserve", "reserve", "reserve", "reserve", "reserve", "reserve",
                              "reserve", "reserve", "reserve", "reserve", "reserve", "reserve", "reserve",
                              "reserve", "reserve", "reserve", "reserve", "reserve", "reserve"
                              ],
            },
            {
                "message": ["CRC", "2byte", "0xFF", "CRC", "0xFF"],
                "childCount": "0",
                "begin": 40,
                "end": 1472
            }
        ],
    },

}

json_item = {'''
    "packageItem": {
        "reserve": {
            "name": "reserve",
            "length": "32",
            "default": "0xff",
            "generate": "true",
            "dataItem": [
                {
                    "message": ["序列号", "4byte", "0x00000001", "序列号", "0x00000001"],
                    "childCount": "0"
                },
            ]
        },
    },'''
}


def nameinit():
    json_head["packageHead"]["dataItem"][5]["childName"] = []
    for i in range(int(json_head["packageHead"]["dataItem"][5]["childCount"])):
        json_head["packageHead"]["dataItem"][5]["childName"].append(f"{62 + 32 * i}-{62 + 32 * (i + 1)}")

def iteminit():
    json_head["packageItem"] = {}
    for i in range(len(json_head["packageHead"]["dataItem"][5]["childName"])):
        json_head["packageItem"][json_head["packageHead"]["dataItem"][5]["childName"][i]] = {}
        json_head["packageItem"][json_head["packageHead"]["dataItem"][5]["childName"][i]] = {
            "name": json_head["packageHead"]["dataItem"][5]["childName"][i],
            "length": "32",
            "default": "0xff",
            "generate": "true",
            "dataItem": []
        }


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    nameinit()
    iteminit()
    with open("out.json", 'w', encoding='utf8') as f:
        f.write(str(json_head).replace('\'','"'))
    print(json_head)
