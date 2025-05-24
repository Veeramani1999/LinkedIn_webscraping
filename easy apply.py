import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome('driver/chromedriver.exe')
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

elementID = browser.find_element(By.ID, 'username')
elementID.send_keys('abinaya.abi0895@gmail.com')
elementID = browser.find_element(By.ID, 'password')
elementID.send_keys('scrabby_1990')
elementID.submit()

search_query = 'machine learning'
search_url = f'https://www.linkedin.com/search/results/Jobs/?keywords={search_query}&origin=GLOBAL_SEARCH_HEADER'
#search_url = f'https://www.linkedin.com/jobs/search/?currentJobId=3508048000&keywords={search_query}&refresh=true'

browser.get(search_url)
time.sleep(10)

search_query_1= 'ALL'
#search_url_1= f'https://www.linkedin.com/jobs/search/?currentJobId=3508048000&keywords={search_query}&refresh=true'
search_url_1= f'https://www.linkedin.com/search/results/{search_query_1}/?keywords={search_query}&origin=SWITCH_SEARCH_VERTICAL&sid=_z7'

browser.get(search_url_1)
time.sleep(10)

search_url_2= f'https://www.linkedin.com/jobs/search/?currentJobId=3513712924&keywords={search_query}'
browser.get(search_url_2)
#print(search_url_2)
time.sleep(10)

browser.find_element(By.XPATH,"//div[@class='relative mr2']").click()
time.sleep(10)

browser.find_element(By.XPATH,"//div[@data-control-name='filter_detail_select']").click()
time.sleep(10)

bb=browser.find_element(By.XPATH,"//button[@class='reusable-search-filters-buttons search-reusables__secondary-filters-show-results-button artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")
bb.click()
time.sleep(10)




#print(bb)
#link=f"https://www.linkedin.com/jobs/search/?currentJobId=3490907185&distance=25.0&f_AL=true&geoId=102713980&keywords={search_query }&sortBy=R"
#browser.get(bb)
#time.sleep(5)

open_profile_hrefs = []
soup = BeautifulSoup(browser.page_source, 'html.parser')
#print(soup)
search_results = soup.find_all('div', {'class': 'flex-grow-1 artdeco-entity-lockup__content ember-view'})
con1=[]
for result in search_results:
    if result.find('div', {'class': 'flex-grow-1 artdeco-entity-lockup__content ember-view'}):
        continue
    profile_link = result.find('a', {'class': 'disabled ember-view job-card-container__link job-card-list__title'})['href']
    #print(profile_link)
   # if '/in/' in profile_link and '/pub/' not in profile_link:
    open_profile_hrefs.append(profile_link)

print(open_profile_hrefs)

time.sleep(10)


my_string = "https://www.linkedin.com"
h=[]
for item in open_profile_hrefs:
    final=my_string + str(item)
    h.append(final)
print(h)
for url in h:
    browser.get(url)
    time.sleep(5)

    browser.find_element(By.XPATH, "//button[@class='jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view']").click()

    elementID = browser.find_element(By.CLASS_NAME,'artdeco-text-input--input')
    elementID.send_keys('9655934230')
    time.sleep(5)

    browser.find_element(By.XPATH,"//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']").click()
    time.sleep(5)

"""

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'scaffold-layout__list')))

    # Get the HTML content of the page and create a BeautifulSoup object
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

    # Find all job listings
job_listings = soup.find_all('section', class_='scaffold-layout__list')

    # Filter job listings to only include those with the Easy Apply button
easy_apply_jobs = []
for job in job_listings:
    easy_apply_button = job.find('ul', class_='scaffold-layout__list-container')



    if easy_apply_button:
        easy_apply_jobs.append(job)

    # Extract job title and job ID for each Easy Apply job
job_ids = []
for job in easy_apply_jobs:
    job_id = job.get('data-occludable-job-id')
    job_title = job.find('li', class_='ember-view   jobs-search-results__list-item occludable-update p0 relative scaffold-layout__list-item')
    job_ids.append((job_id, job_title))

print(job_ids)
"""
"""
open_profile_hrefs = []
soup = BeautifulSoup(browser.page_source, 'html.parser')
search_results = soup.find_all('ul', {'class': 'job-card-list__footer-wrapper job-card-container__footer-wrapper flex-shrink-zero display-flex t-sans t-12 t-black--light t-normal t-roman'})

for result in search_results:
    if result.find('li', {'class': 'job-card-container__footer-item inline-flex align-items-center'}):
        continue
    profile_link = result.find('li', {'class': 'job-card-container__apply-method job-card-container__footer-item inline-flex align-items-center'})
    #if '/in/' in profile_link and '/pub/' not in profile_link:
    open_profile_hrefs.append(profile_link)
print(open_profile_hrefs)
"""