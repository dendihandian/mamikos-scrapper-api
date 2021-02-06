from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get('https://www.mamikos.com/area')

f = open('result.html', 'w')
f.write(driver.page_source)
f.close()

driver.close()
# print(driver.page_source)