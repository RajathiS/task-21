import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_argument("--incognito")


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


url = "https://www.saucedemo.com/"

try:
   
    driver.get(url)

    cookies_before_login = driver.get_cookies()
    print("Cookies before login:")
    for cookie in cookies_before_login:
        print(cookie)

 
    username_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

   
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    
    cookies_after_login = driver.get_cookies()
    print("\nCookies after login:")
    for cookie in cookies_after_login:
        print(cookie)

    
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()

    logout_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_link.click()

  
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )

    cookies_after_logout = driver.get_cookies()
    print("\nCookies after logout:")
    for cookie in cookies_after_logout:
        print(cookie)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:


    driver.quit()
