import requests
import time
import pandas as pd


if __name__ == "__main_":
    # 获取疫情数据
    url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
    # agent 换成自己的
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"
    }
    data = requests.get(url, headers=headers)

    # print(data.json())

    # 寻找累计数据
    china_data = data.json()['data']['diseaseh5Shelf']['areaTree'][0]['children']

    # 存放数据
    data_li = []

    # 从url 中提取数据
    for child in china_data:
        data_dict = {'地区名称': child['name'], '统计时间': child['date'], '新增确诊': child['total']['nowConfirm'],
                 '死亡人数': child['total']['dead'], '治愈人数': child['total']['heal'], '累计确诊': child['total']['confirm'],
                 '本土确诊': child['total']['provinceLocalConfirm'], '无症状': child['total']['wzz']}
    # print(data_dict)
    data_li.append(data_dict)

    # 保存文件
    df = pd.DataFrame(data_li)
    df.to_csv('全国疫情实时数据.csv', mode="w", encoding="utf-8")
