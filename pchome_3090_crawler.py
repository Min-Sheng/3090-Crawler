import sys
sys.path.append('/usr/local/lib/python3.9/site-packages')
import os
import argparse
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import common
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pickle
import json

def auto_purchase(driver, data, url):
    loginAcc = data["loginAcc"]
    loginPwd = data["loginPwd"]
    BuyerName = data["BuyerName"]
    BuyerMobile = data["BuyerMobile"]
    CardNum_single = data["CardNum_single"]
    multi_ThruMonth = data["multi_ThruMonth"]
    multi_ThruYear = data["multi_ThruYear"]
    multi_CVV2Num = data["multi_CVV2Num"]
    BuyerAddrCity = data["BuyerAddrCity"]
    BuyerAddrRegion = data["BuyerAddrRegion"]
    BuyerAddr = data["BuyerAddr"]

    #try:
    driver.get(url)

    # login
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "loginAcc"))
    )
    email_element = driver.find_element_by_id("loginAcc")
    email_element.clear()
    email_element.send_keys(loginAcc)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "loginPwd"))
    )
    password_element = driver.find_element_by_id("loginPwd")
    password_element.clear()
    password_element.send_keys(loginPwd)
    time.sleep(5)
    button = driver.find_element_by_id("btnLogin")
    driver.execute_script("arguments[0].click();", button)

    # put into cart
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@id='ButtonContainer']/button"))
    )
    driver.find_element_by_xpath("//li[@id='ButtonContainer']/button").click()

    # go to cart
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "ico_cart"))
    )
    driver.find_element_by_id('ico_cart').click()

    # go to payment
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@class='CC']/a[@class='ui-btn']"))
    )
    button = driver.find_element_by_xpath("//li[@class='CC']/a[@class='ui-btn']")
    driver.execute_script("arguments[0].click();", button)

    # fill the form
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='BuyerName']"))
    )
    elem = driver.find_element_by_xpath("//input[@id='BuyerName']")
    elem.clear()
    elem.send_keys(BuyerName)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='BuyerMobile']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='BuyerMobile']")
    elem.clear()
    elem.send_keys(BuyerMobile)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='CardNum_single']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='CardNum_single']")
    elem.clear()
    elem.send_keys(CardNum_single)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "multi_ThruMonth"))
    )
    select = Select(driver.find_element_by_id("multi_ThruMonth"))
    select.select_by_value(multi_ThruMonth)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "multi_ThruYear"))
    )
    select = Select(driver.find_element_by_id("multi_ThruYear"))
    select.select_by_value(multi_ThruYear)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='multi_CVV2Num']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='multi_CVV2Num']")
    elem.clear()
    elem.send_keys(multi_CVV2Num)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "BuyerAddrCity"))
    )
    select = Select(driver.find_element_by_id("BuyerAddrCity"))
    select.select_by_visible_text(BuyerAddrCity)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "BuyerAddrRegion"))
    )
    select = Select(driver.find_element_by_id("BuyerAddrRegion"))
    select.select_by_visible_text(BuyerAddrRegion)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='BuyerAddr']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='BuyerAddr']")
    elem.clear()
    elem.send_keys(BuyerAddr)

    ReceiverName = BuyerName
    ReceiverMobile = BuyerMobile 
    ReceiverAddrCity = BuyerAddrCity
    ReceiverAddrRegion = BuyerAddrRegion
    ReceiverAddr = BuyerAddr 

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='ReceiverName']"))
    )
    elem = driver.find_element_by_xpath("//input[@id='ReceiverName']")
    elem.clear()
    elem.send_keys(ReceiverName)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='ReceiverMobile']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='ReceiverMobile']")
    elem.clear()
    elem.send_keys(ReceiverMobile)  

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "ReceiverAddrCity"))
    )
    select = Select(driver.find_element_by_id("ReceiverAddrCity"))
    select.select_by_visible_text(ReceiverAddrCity)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "ReceiverAddrRegion"))
    )
    select = Select(driver.find_element_by_id("ReceiverAddrRegion"))
    select.select_by_visible_text(ReceiverAddrRegion)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='ReceiverAddr']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='ReceiverAddr']")
    elem.clear()
    elem.send_keys(ReceiverAddr)

    # click to agree
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='chk_agree']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='chk_agree']")
    if elem.is_selected() == False:
        elem.click()

    # send the payment
    # WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, "//a[@id='btnSubmit']"))
    # )    
    # button = driver.find_element_by_xpath("//a[@id='btnSubmit']")
    # driver.execute_script("arguments[0].click();", button)

    # except Exception as e:
    #     print(e.__class__.__name__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # basic setting
    parser.add_argument('--chromedriver', type=str, default="/usr/local/bin/chromedriver", help='path of chromedriver')
    parser.add_argument('--buyer_info', type=str, default='pchome_buyer_info.json', help='path of buyer info')
    parser.add_argument('--cookie_path', type=str, default='./cookies.pkl', help='path of cookie')
    args = parser.parse_args()

    with open(args.buyer_info) as jsonfile:
        data = json.load(jsonfile)
    
    driver = webdriver.Chrome(args.chromedriver)
    PRODUT_WEBSITE = 'https://24h.pchome.com.tw/prod/DBAC23-A9006PZEB'
    LOGIN_WITH_PAGE= 'https://ecvip.pchome.com.tw/login/v3/login.htm?rurl=' + PRODUT_WEBSITE

    auto_purchase(driver, data, LOGIN_WITH_PAGE)

