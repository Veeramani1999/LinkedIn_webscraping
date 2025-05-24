import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
import keyboard as key

#actions = ActionChains(driver)

list_new = []
list_new_1 = []
list_new_2 = []

browser = webdriver.Chrome('driver/chromedriver.exe')
actions = ActionChains(browser)
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

elementID = browser.find_element(By.ID, 'username')
# elementID.send_keys('veeraragava593@gmail.com')
# elementID.send_keys('rajakumarib.tech1990@gmail.com')
elementID.send_keys('abinaya.abi0895@gmail.com')
# elementID.send_keys('veeraragava593@gmail.com')
# elementID.send_keys('rajakumarihc@gmail.com')
elementID = browser.find_element(By.ID, 'password')
elementID.send_keys('scrabby_1990')
elementID.submit()

search_query = 'hospitals'
search_query_1 = "Companies"
search_url = f'https://www.linkedin.com/search/results/{search_query_1}/?keywords={search_query}&origin=GLOBAL_SEARCH_HEADER'

#search_url = f'https://www.linkedin.com/search/results/{search_query_1}/?companyHqGeo=%5B%22115702354%22%5D&keywords={search_query_1}&origin=FACETED_SEARCH&sid=oy0'
#search_url = f'https://www.linkedin.com/search/results/{search_query_1}/?companyHqGeo=%5B%22103644278%22%5D&companySize=%5B%22E%22%5D&heroEntityKey=urn%3Ali%3Aautocomplete%3A20549930&industryCompanyVertical=%5B%2214%22%5D&keywords={search_query}&origin=FACETED_SEARCH&position=1&searchId=6b9c2352-9dd0-4a14-8c90-90225de2a5d8&sid=V(.'

browser.get(search_url)
time.sleep(10)

browser.find_element(By.XPATH,"//button[text()='Locations']").click()
find_location=browser.find_element(By.XPATH,"//input[@placeholder='Add a location']")
find_location.send_keys('Chennai')
#find_location.click()
browser.implicitly_wait(5)
actions.send_keys(Keys.ENTER).perform()

for i in range(0,5):
    key.press('tab')
    key.release('tab')
browser.implicitly_wait(5)
browser.find_element(By.XPATH,"//span[text()='Chennai']").click()
for i in range(0,2):
    key.press('tab')
    key.release('tab')
actions.send_keys(Keys.ENTER).perform()
time.sleep(5)



soup = BeautifulSoup(browser.page_source, 'html.parser')
search_results = soup.findAll('li', {'class': 'reusable-search__result-container'})

company_urls = []

for result in search_results:
    company_element = result.find('a', {'class': 'app-aware-link'})
    if company_element is not None:
        company_url = company_element['href']
        company_urls.append(company_url)

# print("Profile Link : ",company_urls)
# new_list = [s.replace("'", "quotes") for s in company_urls]
list_new_1.append(company_urls)
print(list_new_1)

name1 = []
loc1 = []

for url in company_urls:
    browser.get(url)

    time.sleep(5)

    soup = BeautifulSoup(browser.page_source, 'html.parser')

    try:
        name = soup.find('h1', {'class': 'ember-view t-24 t-black t-bold full-width'})
        name1.append(name.text.strip())
    except:
        name = soup.find('h2', {'class': 't-16'})
        name1.append(name.text.strip())
list_new_2.append(name1)
print(list_new_2)


"""

a = [2]

for i in a:
    # next_search_url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22103644278%22%5D&industryCompanyVertical=%5B%2214%22%5D&keywords=Health%20care&origin=FACETED_SEARCH&page={i}&sid=VWE'
    next_search_url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22103644278%22%5D&companySize=%5B%22E%22%5D&heroEntityKey=urn%3Ali%3Aautocomplete%3A20549930&industryCompanyVertical=%5B%2214%22%5D&keywords=hospitals&origin=FACETED_SEARCH&page={i}&position=1&searchId=6b9c2352-9dd0-4a14-8c90-90225de2a5d8&sid=_z~'

    browser.get(next_search_url)
    time.sleep(10)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    next_search_results = soup.findAll('li', {'class': 'reusable-search__result-container'})

    next_company_urls = []

    for next_result in next_search_results:
        next_company_element = next_result.find('a', {'class': 'app-aware-link'})
        if next_company_element is not None:
            next_company_url = next_company_element['href']
            next_company_urls.append(next_company_url)

    print("Profile Link : ", next_company_urls)
    list_new_1.append(next_company_urls)
    # print(list_new_1)

    next_name1 = []
    next_loc1 = []

    for next_url in next_company_urls:
        browser.get(next_url)

        time.sleep(5)

        soup = BeautifulSoup(browser.page_source, 'html.parser')

        try:
            next_name = soup.find('h1', {'class': 'ember-view t-24 t-black t-bold full-width'})
            next_name1.append(next_name.text.strip())
        except:
            next_name = soup.find('h2', {'class': 't-16'})
            next_name1.append(next_name.text.strip())
    list_new_2.append(next_name1)
    print(list_new_2)

"""
resultList_1 = [element_1 for nestedlist_1 in list_new_1 for element_1 in nestedlist_1]
resultList_2 = [element_2 for nestedlist_2 in list_new_2 for element_2 in nestedlist_2]

print(resultList_1)
print(resultList_2)

dict1 = {"Name": resultList_2, "Profile Link": resultList_1}
print(dict1)

import pandas as pd

df1 = pd.DataFrame(dict1)

print(df1.shape)

df1.to_csv(r'C:\Users\SSLTP11373\Desktop\parser\linkedInhealthcare85.csv')

