from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://news.naver.com/main/ranking/popularMemo.nhn?rankingType=popular_memo&sectionId=100&date=20200903')
print(driver.title)
driver.close()  # close() - close one tap, quit - close entire browser
