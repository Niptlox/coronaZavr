import requests
import json


def preparation_regions():
    regions_title = []
    with open('static/json/Russian.json', "r", encoding="utf-8") as f:
        d = json.load(f)["russia_stat_struct"]
        dates = d["dates"]
        regions_id = {}
        regions = []
        cases = {}
        for rid, inf in d["data"].items():
            inf = inf["info"]
            name = inf["name"]
            
            regions_id[name] = rid
            regions_title.append(name)
            regions.append([name, inf["cases"], inf["cases_delta"], inf["deaths"], inf["deaths_delta"]])
    regions_title.sort()
    regions.sort(key=lambda x: x[0])
    return regions_id, regions_title, dates, regions


def reload_regions():
    url = "https://milab.s3.yandex.net/2020/covid19-stat/data/v10/default_data.json"
    with requests.get(url) as res_:
        print("reload_regions:", res_)
        res = res_
        if res.status_code == 200:
            data = res.json()
            with open('static/json/Russian.json', 'w') as f:
                json.dump(data, f)
        # print(data)


reload_regions()
regions_id, regions_title, dates, regions = preparation_regions()