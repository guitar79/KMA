from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Chrome()
driver.get('https://data.kma.go.kr/data/grnd/selectAsosList.do?pgmNo=34')
#log=driver.find_element_by_id('loginBtn')
log=driver.find_element_by_css_selector('#loginBtn')
sleep(1)

log.click()
logid=driver.find_element_by_name('loginId')
logid.send_keys('dragoninsky@naver.com')
logpw=driver.find_element_by_name('passwordNo')
logpw.send_keys('neverhack72^@^')
logpw.send_keys(Keys.RETURN)

sleep(1)
box=driver.find_element_by_css_selector('#content > div.btn-area > span:nth-child(2)')
box.click()
ActionChains(driver).send_keys(Keys.END).send_keys(Keys.RETURN).perform()
check=driver.find_element_by_id('checkAll')
check.click()
down=driver.find_element_by_css_selector('#schForm > div.btn-area.text-center > a:nth-child(2)')
down.click()
sleep(1)
btn=driver.find_element_by_css_selector('#reqstPurposeCd7')
btn.click()
conf=driver.find_element_by_css_selector('#btnArea > input.btn.btn-primary')
conf.click()
sleep(1)
two=driver.find_element_by_css_selector('#content > div.boardWrap > div > div.pagination.pagination-small > ul > li:nth-child(4) > a')
two.click()

#ActionChains(driver).send_keys(Keys.END)



