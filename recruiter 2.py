from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import keyboard as key
import time
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlwt
driver = webdriver.Chrome(executable_path=r"driver/chromedriver.exe")
driver.get("https://www.linkedin.com/login")
driver.maximize_window()
actions = ActionChains(driver)
user=driver.find_element(By.NAME,"session_key")
user.send_keys('mnesapriyan477@gmail.com')
password=driver.find_element(By.NAME,"session_password")
password.send_keys('Nesan@0308')
submit=driver.find_element(By.CLASS_NAME,'login__form_action_container ')
submit.click()
driver.implicitly_wait(5)
search_data=driver.find_element(By.CLASS_NAME,'search-global-typeahead__input')
search_data.send_keys('Jasper')
key.press('enter')
key.release('enter')
time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='People']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='Locations']").click()
find_location=driver.find_element(By.XPATH,"//input[@placeholder='Add a location']")
find_location.send_keys('Chennai')
#find_location.click()
driver.implicitly_wait(5)
actions.send_keys(Keys.ENTER).perform()
#key.press('enter')
#key.release('enter')
for i in range(0,5):
    key.press('tab')
    key.release('tab')
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//span[text()='Chennai']").click()
for i in range(0,2):
    key.press('tab')
    key.release('tab')
actions.send_keys(Keys.ENTER).perform()
time.sleep(5)
result=driver.find_element(By.XPATH,"//h2[@class='pb2 t-black--light t-14']").text
for i in result.split():
	if ',' in i:
		a=int(i.replace(',', ''))
Name=[]
Skills=[]
location=[]
contact_info=[]
try:
    def nextfunction(b):
        for i in range(1,b):
            if i < 11:
                peoples=driver.find_element(By.XPATH,f"(//li[@class='reusable-search__result-container'])[{i}]")
                peoples.click()
                time.sleep(5)
                name = driver.find_element(By.XPATH,
                          "//h1[@class='text-heading-xlarge inline t-24 v-align-middle break-words']").text
                driver.implicitly_wait(5)
                Name.append(name)
                print(name)
                skills = driver.find_element(By.XPATH, "//div[@class='text-body-medium break-words']").text
                driver.implicitly_wait(5)
                print(skills)
                Skills.append(skills)
                loc = driver.find_element(By.XPATH,
                                          "//span[@class='text-body-small inline t-black--light break-words']").text
                driver.implicitly_wait(5)
                print(loc)
                location.append(loc)
                contactinfo = driver.find_element(By.XPATH, "//span[@class='pv-text-details__separator t-black--light']")
                contactinfo.click()
                driver.implicitly_wait(5)
                link = driver.find_element(By.XPATH, "//div[@class='pv-contact-info__ci-container t-14']").text
                print(link)
                contact_info.append(link)
                driver.back()
                driver.back()
                time.sleep(5)
            if i>=11:
                time.sleep(5)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(10)
                next_button=driver.find_element(By.XPATH,"//span[text()='Next']")
                next_button.click()
                time.sleep(10)
                nextfunction(13)
                break
    nextfunction(12)
    #for i in range(0,5):
        #nextfunction(12)
except:
    pass
dict={"Name":Name,"SKILLS":Skills,"Location":location,"Contact_Info":contact_info}
print(dict)
import pandas as pd
df=pd.DataFrame(dict)
df.to_csv(r'C:\Users\SSLTP11373\Desktop\parser\linkedIn55.csv')