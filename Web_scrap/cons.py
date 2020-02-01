import pandas as pd

df = pd.read_csv(r"C:/Users/Acer/Desktop/Hack_vsit/wthpt/sclist.csv")

sids = df['list']

# print(sids)

for sid in sids:
    try:
        df = pd.read_json(f"C:/Users/Acer/Desktop/Hack_vsit/school{sid}.json")
        a = []
        a = df['values']
        print(int(a[16]))
        '''b = []
        b = a['0']
        print(b)
        c = []
        c = b['16']
        print(c)'''

        if 0 < int(int(a[16])) and int(a[16]) < 11:
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
            dfd["1"] = a
            dfd.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/1/school{sid}.json", index = True)

        if 10 < int(int(a[16])) and int(int(a[16])) < 20:
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
            dfd["1"] = a
            dfd.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/2/school{sid}.json", index = True)

        if 19 < int(int(a[16])) and int(int(a[16])) < 28:
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
            dfd["1"] = a
            dfd.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/3/school{sid}.json", index = True)

        if 26 < int(int(a[16])) and int(int(a[16])) < 37:
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
            dfd["1"] = a
            dfd.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/4/school{sid}.json", index = True)

        if 36 < int(int(a[16])) and int(int(a[16])) < 58:
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
            dfd["1"] = a
            dfd.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/5/school{sid}.json", index = True)

        if 57 < int(int(a[16])) and int(a[16]) < 63:
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
            dfd["1"] = a
            dfd.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/6/school{sid}.json", index = True)

        if 62 < int(a[16]) and int(a[16]) < 71:
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
            dfd["1"] = a
            dfd.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/7/school{sid}.json", index = True)

    except:
        pass