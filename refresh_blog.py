import os,time,requests,re
from selenium import webdriver

def gatherUrls(page):
	url = "http://www.jianshu.com/u/79a88a044955?order_by=shared_at&page=" + str(page)
	response = requests.get(url)
	datas = re.findall(r'<a class="title" target="_blank" href="/p/(.+)">', response.content.decode())

	urls = []
	for data in datas:
		urls.append("http://www.jianshu.com/p/" + data)
	return urls	

def refreshBrowser(url):
	browser.get(url)
	print(browser.session_id)
	# print(browser.page_source)
	# print(browser.get_cookies())

	flag = True
	times = 0
	while flag:
		times+=1
		if times > 6:
			flag = False
		else:
			browser.refresh()
			time.sleep(3)

if __name__ == '__main__':
	print("start")
	os.environ["webdriver.chrome.driver"] = "C:\chromedriver.exe"

	PROXY = "42.51.26.79:3128"
	chromeOptions = webdriver.ChromeOptions()
	chromeOptions.add_argument('--proxy-server={0}'.format(PROXY))

	# browser = webdriver.Chrome("C:\chromedriver.exe")
	browser = webdriver.Chrome(executable_path="C:\chromedriver.exe", chrome_options=chromeOptions)
	# time.sleep(3)
	browser.implicitly_wait(30) # 智能等待30s,每次 会话只需调用一次
	browser.maximize_window() # 浏览器最大化

	try:
		urls = gatherUrls(page=1)
		for url in urls:
			print("current page is " + url)
			refreshBrowser(url)
			time.sleep(8) # 

		browser.quit()
		print("end")

	except Exception as e:
		raise
	finally:
		browser.quit()
		print("webdriver is quit!")


