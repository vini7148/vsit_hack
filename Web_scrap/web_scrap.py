from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

url = 'http://www.edudel.nic.in/mis/schoolplant/frmSchoolInformation.aspx?Schoolid='
sid = 1001001
url = url + str(sid)

# url = "http://www.edudel.nic.in/mis/schoolplant/frmDistrictAndSchoolInformation.aspx"

print(url)

driver = webdriver.Chrome(r"C:\Users\Acer\chromedriver.exe")
# print("using firefox")
# driver = webdriver.Chrome(r"C:\Program Files\Mozilla Firefox\firefox.exe")

print("kjfjdhgf")
driver.get(url)

'''select = Select(driver.find_element_by_class('MISFieldCaptionTD'))

select.select_by_value('School')

driver.find_element_by_id('btnGo').click()

print("get reached")'''

page = driver.execute_script('return document.body.innerHTML')
soup = BeautifulSoup(''.join(page), 'html.parser')

print(type(soup))

print(soup.prettify())

names = (soup.find_all('span', class_ = 'MISFieldCaptionTD'))
print(names)

cust_name = []
for i in range(0, len(names)):
    # get_text() - Removes all the tags & extracts text
    cust_name.append(names[i].get_text())
    
print(cust_name)

import pandas as pd
df = pd.DataFrame()
df['values'] = cust_name

df.to_json(r'C:/Users/Acer/Desktop/Hack_vsit/aa.json', index = True)