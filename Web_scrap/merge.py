from pprint import pprint

from jsonmerge import merge

import json

import pandas as pd

df = pd.read_csv(r"C:/Users/Acer/Desktop/Hack_vsit/wthpt/sclist2.csv")

sids = df['list']

print(sids)

result = []

for sid in sids:
    try:
        fi = pd.read_json(f"C:/Users/Acer/Desktop/Hack_vsit/wthpt/school{sid}.json")
        result.append(fi)
        
    except:
        pass

print(result)

'''with open("school1.json", "w") as write_file:
    json.dump(result, write_file, indent=4)'''

df = pd.DataFrame()
df['sc'] = result
df.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/wthpt/school1.json", index = True)