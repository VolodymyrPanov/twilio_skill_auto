
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def launch_set_up(driver, username, password, okta):

    driver.get("https://transferwise.okta-emea.com/")
    driver.find_element(By.ID, 'okta-signin-username').send_keys(username)
    driver.find_element(By.ID, 'okta-signin-password').send_keys(password)
    driver.find_element(By.ID, 'okta-signin-password').send_keys(Keys.ENTER)
    time.sleep(1)
    
    try:
        driver.find_element(By.ID, 'input67').send_keys(okta)
        driver.find_element(By.ID, 'input67').send_keys(Keys.ENTER)
    except:
        while True:
            try:
                button = wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="button button-primary"]')))
                break
            except TimeoutException:
                time.sleep(0.2)
        button.click()

    while True:
        try:
            wait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='dashboard--my-apps-title']")))
            break
        except TimeoutException:
            time.sleep(0.2)
            
    driver.execute_script("window.open('');")
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    driver.get("https://flex.twilio.com/teams/")
    while True:
        try:
            button = wait(driver, 1).until(EC.element_to_be_clickable((By.NAME, "runtimeDomain")))
            break
        except TimeoutException:
            time.sleep(0.2)
    button.click()
    driver.find_element(By.NAME, "runtimeDomain").click()
    driver.find_element(By.NAME, "runtimeDomain").clear()
    driver.find_element(By.NAME, "runtimeDomain").send_keys("raspberry-grouse-1842")
    driver.find_element(By.CSS_SELECTOR, "button.Twilio-Button.Twilio-LoginFormView-LoginButton.css-f5lad7").click()
    # driver.minimize_window()

    while True:
        try:
            button = wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="ant-btn"]')))
            break
        except TimeoutException:
            print('skip button not found')
            time.sleep(0.2)
    button.click()

    driver.find_element(By.XPATH, '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained Twilio-Button css-1rjnz87 MuiButton-containedSecondary"]').click()
    driver.find_element(By.XPATH, '//button[@class="MuiButtonBase-root MuiIconButton-root Twilio-IconButton css-169h1y7 css-1jbz6hu MuiIconButton-sizeSmall"]').click()
    driver.find_element(By.XPATH, '//input[@id="Available___custom_activity_name"]').click()
    driver.find_element(By.XPATH, '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained Twilio-Button css-1rjnz87 Twilio-FilterListButtons-ApplyButton css-f5w1de MuiButton-containedPrimary"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@class="MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedStart"]').click()
    driver.find_element(By.XPATH, '//input[@class="MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedStart"]').send_keys('Felipe Saito')
    driver.find_element(By.XPATH, '//input[@class="MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedStart"]').send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='Felipe Saito']/ancestor::div[@role='button']").click()

    try:
        button = wait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//button[@class="ant-btn"]')))
        button.click()
    except Exception:
        pass

    driver.find_element(By.XPATH, "//span[@class='Twilio' and text() = 'Add skill']/parent::div").click()

    existing_skills = []
    for elem in driver.find_elements(By.XPATH, '//li[@class="MuiButtonBase-root MuiListItem-root MuiMenuItem-root MuiMenuItem-gutters MuiListItem-gutters MuiListItem-button"]/following::span[@class="Twilio"]'):
        existing_skills.append(elem.text)
    driver.find_element(By.XPATH, '//div[@style="z-index: -1; position: fixed; inset: 0px; background-color: transparent; -webkit-tap-highlight-color: transparent;"]').click()
    return existing_skills

def add_skill(driver, skill, name, existing_skills):
    skill = skill.strip()
    if skill in existing_skills:
        try:
            driver.find_element(By.XPATH, "//span[text()='{}']".format(skill.strip()))
            print(f'{name} has {skill} skill already')
            outcome = 'success'
        except:
            driver.find_element(By.XPATH, "//span[@class='Twilio' and text() = 'Add skill']/parent::div").click()
            time.sleep(1)
            driver.find_element(By.XPATH,'//li[@class="MuiButtonBase-root MuiListItem-root MuiMenuItem-root MuiMenuItem-gutters MuiListItem-gutters MuiListItem-button"]/following::span[@class="Twilio" and text()="{}"]'.format(skill)).click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiIconButton-root Twilio-IconButton css-169h1y7 MuiIconButton-colorPrimary']").click()
            driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained Twilio-Button css-1rjnz87 Twilio-WorkerSkills-SkillsSaveButton MuiButton-containedPrimary']").click()
            print(f'{name} added {skill} skill')
            outcome = 'success'
    else:
        outcome = 'fail'
        pass
    return outcome

def delete_skill(driver, skill, name, existing_skills):
    skill = skill.strip()
    if skill in existing_skills:
        result = 0
        try:
            driver.find_element(By.XPATH, "//span[text()='{}']".format(skill))
            result = 1
        except:
            print(f'{name} has no {skill} skill to delete')
            pass
            outcome = 'success'
        if result == 1:
            driver.find_element(By.XPATH, '//span[@class="Twilio" and text()="{}"]/following::button[@type="button"]'.format(skill)).click()
            driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained Twilio-Button css-1rjnz87 Twilio-WorkerSkills-SkillsSaveButton MuiButton-containedPrimary']").click()
            print(f'{name} deleted {skill} skill')
            outcome = 'success'
        else:
            pass
    else:
        outcome = 'fail'
    return outcome

def add_delete(driver, df, existing_skills):
    for i, row in df.iterrows():
        name = row['name'].strip()
        driver.find_element(By.XPATH,'//input[@class="MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedStart"]').click()
        for x in range(20):
            driver.find_element(By.XPATH,'//input[@class="MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedStart"]').send_keys(Keys.BACKSPACE)
        try:
            driver.find_element(By.XPATH,'//input[@class="MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedStart"]').send_keys(name)
            driver.find_element(By.XPATH,'//input[@class="MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedStart"]').send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//span[text()='{}']/ancestor::div[@role='button']".format(name)).click()
        except Exception:
            print(f"{name} was not found or something else went wrong")
            df.loc[i, 'outcome'] = 'not found'
            continue
        try:
            driver.find_element(By.XPATH, '//button[@class="ant-btn"]').click()
        except:
            pass
        action = row['action'].strip()
        if action == 'add':
            try:
                add_skill(driver, row['skill'], name, existing_skills)
                df.loc[i, 'outcome'] = 'success'
            except Exception:
                df.loc[i, 'outcome'] = 'fail'
                pass
        elif action == 'delete':
            try:
                outcome = delete_skill(driver, row['skill'], name, existing_skills)
                df.loc[i, 'outcome'] = outcome
            except Exception:
                df.loc[i, 'outcome'] = 'fail'
                pass
    return df



