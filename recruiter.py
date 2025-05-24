import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('driver/chromedriver.exe')
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

elementID = browser.find_element(By.ID, 'username')
elementID.send_keys('abinaya.abi0895@gmail.com')
elementID = browser.find_element(By.ID, 'password')
elementID.send_keys('scrabby_1990')
elementID.submit()

search_query = 'jasper'
search_url = f'https://www.linkedin.com/search/results/people/?keywords={search_query}&origin=GLOBAL_SEARCH_HEADER'

browser.get(search_url)
time.sleep(5)

open_profile_hrefs = []
soup = BeautifulSoup(browser.page_source, 'html.parser')
search_results = soup.find_all('li', {'class': 'reusable-search__result-container'})

for result in search_results:
    if result.find('span', {'class': 'entity-result__title-textt-16'}):
        continue
    profile_link = result.find('a', {'class': 'app-aware-link'})['href']
    if '/in/' in profile_link and '/pub/' not in profile_link:
        open_profile_hrefs.append(profile_link)
print(open_profile_hrefs)
name1 = []
loc1 = []
des1 = []
con1 = []

for url in open_profile_hrefs:
    browser.get(url)
    time.sleep(5)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    name = soup.find('h1', {'class': 'text-heading-xlarge inline t-24 v-align-middle break-words'})
    name1.append(name.text.strip())
    location = soup.find('span', {'class': 'text-body-small inline t-black--light break-words'})
    loc1.append(location.text.strip())
    try:
        designation = soup.find('div', {'class': 'text-body-medium break-words'})
        des1.append(designation.text.strip())
    except AttributeError:
        designation = ''

    contact_info_href = []
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    search_resultt = soup.find_all('span', {'class': 'pv-text-details__separator t-black--light'})

    for resultt in search_resultt:
        if resultt.find('span', {'class': 'pv-text-details__separator t-black--light'}):
            continue
        profile_linkk = resultt.find('a', {
            'class': 'ember-view link-without-visited-state cursor-pointer text-heading-small inline-block break-words'})[
            'href']
        if '/in/' in profile_linkk and '/pub/' not in profile_linkk:
            contact_info_href.append(profile_linkk)
    j = " ".join(contact_info_href)

    a = "https://www.linkedin.com"
    finalurl = a + j
    con1.append(finalurl)


dict1 = {"Name": name1, "Location": loc1, "Designation": des1, "Contact_info": con1}
print(dict1)

import pandas as pd

df1 = pd.DataFrame(dict1)
print(df1)


df1.to_csv(r'C:\Users\SSLTP11373\Desktop\parser\linkedInrecruiter11.csv')
