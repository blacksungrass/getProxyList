from selenium import webdriver
from time import sleep
class Proxy(object):
	def __init__(self,ip,port):
		self.ip = ip
		self.port = int(port)
def getProxyList(driver,page):
	#driver = webdriver.Firefox()
	driver.get("http://www.kuaidaili.com/free/inha/"+str(page)+'/')
	sleep(2)
	r = driver.find_elements_by_tag_name('tr')
	r.pop(0)
	for i in range(len(r)):
		t = r[i].text.split()
		r[i] = Proxy(t[0],t[1])
	driver.close()
	return r
driver = webdriver.Firefox()
for i in range(1,100):
	getProxyList(driver,i)