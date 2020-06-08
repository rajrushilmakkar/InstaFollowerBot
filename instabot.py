from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#username=input('Enter your phone number,username or email:')
#password=input('Enter your password:')
driver=webdriver.Firefox()
driver.get('https://www.instagram.com/')


time.sleep(5)
def login():
    
    driver.find_element_by_name('username').send_keys('rushilmakkar')
    driver.find_element_by_name('password').send_keys('rAJ@150507'+Keys.RETURN)
    time.sleep(6)
    driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     '][@type='button']").click()
    driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()
def get_pics():
    driver.get('https://www.instagram.com/explore/tags/'+'python'+'/')
    time.sleep(3)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    links=driver.find_elements_by_tag_name('a')
    pics=[link.get_attribute('href') for link in links]
    pics0=[pic for pic in pics if 'explore' not in pic]
    print(pics0)
    for pic in pics0:
        driver.get(pic)
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='wpO6b '][@type='button']").click()
    
def follow_people():
    driver.get('https://www.instagram.com/explore/')
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='HUW1v hUQXy']").click()
    time.sleep(2)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    people=driver.find_elements_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     '][@type='button']")
    for person in people:
        person.click()
       


login()
follow_people()
get_pics()
