from selenium import webdriver
import time
try:
    driver = webdriver.Chrome()
    driver.get("https://shimo.im/login?from=home")
    username_loc = driver.find_element_by_xpath('//input[@name="mobileOrEmail"]')
    username_loc.send_keys("****")
    password_loc = driver.find_element_by_name("password")
    password_loc.send_keys("****")
    login_btn_loc = driver.find_element_by_xpath("//button[@class='sm-button submit sc-1n784rm-0 bcuuIb']")
    login_btn_loc.click()
    time.sleep(3)
    work_plat_loc = driver.find_element_by_xpath('//*[@id="desktop-list"]/a[1]')
    work_plat = work_plat_loc.text

    assert work_plat, "工作台"
    time.sleep(4)

except Exception as e:
    print(e)
finally:
    driver.quit()
