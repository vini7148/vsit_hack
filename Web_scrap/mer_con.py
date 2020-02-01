import pandas as pd

df = pd.read_csv(r"C:/Users/Acer/Desktop/Hack_vsit/wthpt/sclist.csv")

sids = df['list']

r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []
r7 = []

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

            '''dfd = pd.DataFrame()
            dfd["1"] = a
            dfd.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/1/school{sid}.json", index = True)'''
            r1.append(a)

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

            '''dfd = pd.DataFrame()
            dfd["1"] = a
            dfd.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/2/school{sid}.json", index = True)'''
            r2.append(a)

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

            '''dfd = pd.DataFrame()
            dfd["1"] = a
            dfd.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/3/school{sid}.json", index = True)'''
            r3.append(a)

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

            '''dfd = pd.DataFrame()
            dfd["1"] = a
            dfd.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/4/school{sid}.json", index = True)'''
            r4.append(a)

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

            '''dfd = pd.DataFrame()
            dfd["1"] = a
            dfd.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/5/school{sid}.json", index = True)'''
            r5.append(a)

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

            '''dfd = pd.DataFrame()
            dfd["1"] = a
            dfd.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/6/school{sid}.json", index = True)'''
            r6.append(a)
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

            '''dfd = pd.DataFrame()
            dfd["1"] = a
            dfd.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/7/school{sid}.json", index = True)'''
            r7.append(a)

    except:
        pass

df1 = pd.DataFrame()
df1['sc'] = r1
df1.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/1/school1.json", index = True)

df2 = pd.DataFrame()
df2['sc'] = r2
df2.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/2/school2.json", index = True)

df3 = pd.DataFrame()
df3['sc'] = r3
df3.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/3/school3.json", index = True)

df4 = pd.DataFrame()
df4['sc'] = r4
df4.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/4/school4.json", index = True)

df5 = pd.DataFrame()
df5['sc'] = r5
df5.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/5/school5.json", index = True)

df6 = pd.DataFrame()
df6['sc'] = r6
df6.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/6/school6.json", index = True)

df7 = pd.DataFrame()
df7['sc'] = r7
df7.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/7/school7.json", index = True)