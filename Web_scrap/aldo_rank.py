# first yes at 17

import pandas as pd
from pandas.io.json import json_normalize
import json
import demjson

co = 0

df = pd.read_csv(r"C:/Users/Acer/Desktop/Hack_vsit/wthpt/sclist.csv")

sids = df['list']

print(sids)

schools = []
pts = []

for sid in sids:
    try:
        df = pd.read_json(f"C:/Users/Acer/Desktop/Hack_vsit/school{sid}.json")
        print(df)
        a = []
        a = df["values"]
        # print(a)
        '''for i in df["values"]:
            print(i)'''
        '''text = demjson.decode(df)
        print(text)'''
        '''dfj = json_normalize(df[0])
        print("json")
        print(dfj)
        print("endjson")'''
        point = 0
        if a[17] == "Yes":
            point =  point + 100

        if a[18] == "Yes":
            point =  point + 100

        if a[19] == "Yes":
            point =  point + 100

        if a[20] == "Yes":
            point =  point + 100

        per = float(a[25]) / float(a[24])
        per = per * 10
        point = point + int(per)
        
        if a[17] == "Yes" and a[45] == "Yes":
            point =  point + 50

        if a[17] == "Yes" and a[45] == "Yes(Fully Equipped)":
            point =  point + 100

        if a[17] == "Yes" and a[46] == "Yes":
            point =  point + 50

        if a[17] == "Yes" and a[46] == "Yes(Fully Equipped)":
            point =  point + 100

        if a[17] == "Yes" and a[47] == "Yes":
            point =  point + 50

        if a[17] == "Yes" and a[47] == "Yes(Fully Equipped)":
            point =  point + 100

        if a[17] == "Yes" and a[48] == "Yes(Fully Equipped)":
            point =  point + 100

        if a[49] == "Yes":
            point =  point + 50

        if a[49] == "Yes(Fully Equipped)":
            point =  point + 100

        if a[50] == "Yes":
            point =  point + 50

        if a[50] == "Yes(Fully Equipped)":
            point =  point + 100

        print(point)

        va = [a, point]

        dfd = pd.DataFrame()
        dfd["1"] = va
        dfd.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/wthpt/school{sid}.json", index = True)

        schools.append(sid)
        pts.append(point)

        co = co + 1


    except:
        pass

    '''if sid > 1003265 and sid < 1104000:
        sid = 1104001
'''

'''for sid in range(1001001, 1003266):
    df = pd.read_json(f"C:/Users/Acer/Desktop/Hack_vsit/school{sid}.json")
    print(df)
    print(json_normalize(df))
    print("json")
    print(df)
    print("endjson")
    co = co + 1'''

print(co)

dfdd = pd.DataFrame()
dfdd['list'] = schools
dfdd['points'] = pts
dfdd.to_csv(f"C:/Users/Acer/Desktop/Hack_vsit/wthpt/sclist2.csv", index = True)