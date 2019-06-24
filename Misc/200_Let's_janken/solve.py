from selenium import webdriver
import chromedriver_binary
from datetime import datetime
from time import sleep

#driver_path = '/usr/local/lib/python3.6/dist-packages/chromedriver_binary'
driver = webdriver.Firefox()
url = 'http://192.168.36.1/ctf/MaidakeCTF2019/janken/'

driver.get(url)

while True:
	now = int(datetime.now().strftime("%S"))
	if now // 20 == 0:
		driver.find_element_by_id('par').click()
	elif now // 20 == 1:
		driver.find_element_by_id('goo').click()
	elif now // 20 == 2:
		driver.find_element_by_id('choki').click()

	print(driver.find_element_by_id('flag').text)
	if 'MaidakeCTF' in driver.find_element_by_id('flag').text:
		print(driver.find_element_by_id('flag').text)
		break
	
#driver.find_element_by_id('choki').click()
#driver.find_element_by_id('par').click()

driver.close()
driver.quit()