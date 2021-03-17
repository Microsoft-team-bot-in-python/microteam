from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.microsoft.com/en-in/microsoft-365/microsoft-teams/group-chat-software')

time.sleep(7)

print("LOGIN PROCESSING........")

driver.find_element_by_xpath('//a[@class="c-button f-secondary ow-slide-in ow-slide-in-2 xs-ow-mr-0 ow-mt-10 ow-txt-trans-upper ow-bvr-signin"]').click()

driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

print("ENTERING EMAIL ID ...........")

driver.find_element_by_name("loginfmt").send_keys("Your email")
time.sleep(2)

driver.find_element_by_id('idSIButton9').click()
time.sleep(2)

print("ENTERING PASSWORD.........")

driver.find_element_by_name("passwd").send_keys('Your password')
time.sleep(2)

driver.find_element_by_id("idSIButton9").click()
time.sleep(2)

print('LOGIN SUCCESSFULL............')