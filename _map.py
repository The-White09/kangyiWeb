from pyecharts import options as opts
from pyecharts.charts import Geo, Map
import csv

if __name__ == "__main__":
    quezhen = []
    provinces = []
    death = []
    new = []
    cure = []
    local = []
    no = []
    with open("static/csv/yiqingInformation.csv", encoding="utf-8-sig", mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            quezhen.append(int(row["累计确诊"]))
            provinces.append((row["地区名称"]))
            local.append(int(row["本土确诊"]))
            new.append(row["新增确诊"])
            death.append(row["死亡人数"])
            cure.append(row["治愈人数"])
            no.append(row["无症状"])
    print(no)
    c = (
            Map()
            .add("累计确诊", [list(z) for z in zip(provinces, quezhen)], "china")
            .render("quezhen.html")
        )
    c = (
            Map()
            .add("本土确诊", [list(z) for z in zip(provinces, local)], "china")
            .render("local.html")
        )
    c = (
            Map()
            .add("新增确诊", [list(z) for z in zip(provinces, new)], "china")
            .render("new.html")
        )
    c = (
            Map()
            .add("死亡人数", [list(z) for z in zip(provinces, death)], "china")
            .render("death.html")
        )
    c = (
            Map()
            .add("治愈人数", [list(z) for z in zip(provinces, cure)], "china")
            .render("cure.html")
        )
    c = (
            Map()
            .add("无症状", [list(z) for z in zip(provinces, no)], "china")
            .render("no.html")
        )
