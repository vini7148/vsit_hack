from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(r"C:\Users\Acer\chromedriver.exe")

sids = [1001001, 1001002, 1001004, 1001006, 1001008, 1001009, 1001012, 1001018, 1001022, 1001023, 1001024, 1001026, 1001102, 1001104, 1001105, 100106,1001109, 100110]

for sid in range(1411001, 2128033):
    url = 'http://www.edudel.nic.in/mis/schoolplant/frmSchoolInformation.aspx?Schoolid='
    url = url + str(sid)
    print(url)
    driver.get(url)
    print("get reached")
    page = driver.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(''.join(page), 'html.parser')

    print(type(soup))

    print(soup.prettify())

    names = (soup.find_all('span', class_ = 'mislabel'))
    print(names)

    cust_name = []
    for i in range(0, len(names)):
        # get_text() - Removes all the tags & extracts text
        cust_name.append(names[i].get_text())
    
    print(cust_name)
    if cust_name[8] != "Not Available":
        df = pd.DataFrame()
        df['values'] = cust_name
        df.to_json(f"C:/Users/Acer/Desktop/Hack_vsit/school{sid}.json", index = True)

