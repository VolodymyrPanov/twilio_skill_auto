from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from twilio_functions import launch_set_up, add_delete
import pandas as pd



df = pd.read_csv('twilio_skill_input.csv')

options = Options()
# options.add_experimental_option("detach", True)
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager(latest_release_url='https://chromedriver.storage.googleapis.com/LATEST_RELEASE_107').install(), options=options)
driver.implicitly_wait(5)

# <editor-fold desc="Description">
username = input('Add your transferwise email address: ')
password = input('Add your okta password: ')
# </editor-fold>
okta = input('Add your okta OTP: ')

existing_skills = launch_set_up(driver=driver, username=username, password=password, okta=okta)

df = add_delete(driver=driver, df=df, existing_skills=existing_skills)

with open('twilio_skill_input.csv', 'w') as file:
    df.to_csv(file, sep=',', index=False, line_terminator='\n')

exit()




