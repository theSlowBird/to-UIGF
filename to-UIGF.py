import json
import time

import xlrd

from hparam import *

typeMap = {
    '角色活动祈愿': '301',
    '武器活动祈愿': '302',
    '常驻祈愿': '200',
    '新手祈愿': '100'
}


def read_xls(filename):
    # 打开Excel文件
    data = xlrd.open_workbook(filename)
    data1 = []
    for i, table in enumerate(data.sheets()):
        print(f"工作表{i + 1}：{table.name}")
        # 统计行数
        rows = table.nrows
        # 时间, 名称, 类别, 星级, 总次数, 保底内, 祈愿Id
        for v in range(1, rows):
            values = table.row_values(v)
            if int(values[6]) == 0:
                continue
            data1.append({
                "time": str(values[0]),
                "name": str(values[1]),  # 这里我只需要字符型数据，加了str(),根据实际自己取舍
                "item_type": str(values[2]),
                "rank_type": str(int(values[3])),
                "id": str(int(values[6])),
                "uigf_gacha_type": typeMap[table.name],
                "gacha_type": typeMap[table.name]
            })

    return data1


def main():
    data = read_xls(xls)
    with open(js_file, 'r', encoding='utf-8') as f:
        gacha_list = json.load(f)
    for k in gacha_list['result']:
        for w in k:
            if not isinstance(w, list):
                continue
            for v in w:
                # ["2021-07-31 23:32:54","行秋","角色",4,"301","1627743960000605115"],
                data.append({
                    "time": v[0],
                    "name": v[1],
                    "item_type": v[2],
                    "rank_type": str(v[3]),
                    "id": v[5],
                    "uigf_gacha_type": v[4],
                    "gacha_type": v[4]
                })
    # exit()
    info = {
        "uid": "189492972",
        "lang": "zh-cn",
        "export_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "export_app": "Excel2JSON",
        "export_app_version": "0.1.1",
        "uigf_version": "v2.1"
    }
    data = {"info": info, "list": data}  # 前面的数据只是数组，加上外面的json格式大括号
    # print(data)
    # 可读可写，如果不存在则创建，如果有内容则覆盖
    with open(f"UIGF_{uid}.json", "w", encoding='utf-8') as jsFile:
        json.dump(data, jsFile, ensure_ascii=False, indent=2)
    print(f"输出成功: UIGF_{uid}.json")


if __name__ == '__main__':
    main()
