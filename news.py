from selenium import webdriver
from urllib.parse import urlparse
option = webdriver.ChromeOptions()
option.add_argument("--headless")
option.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=option)


driver.get('https://udn.com/news/breaknews/1')
def catch_news_graphic(n):
   result=driver.find_element_by_xpath('//*[@id="breaknews"]/div[1]/div{}/div[1]/a/picture/img'.format([n])).get_attribute("src") #動態xpath
   #get到的網址是縮圖的網址需處理出.jepg的網址
   result=result.replace('https://pgw.udn.com.tw/gw/photo.php?u=','')
   result=result.replace(result[result.find('&'):len(result)],'')
   return(result)
def catch_news_text(n):
    return(driver.find_element_by_xpath('//*[@id="breaknews"]/div[1]/div{}/div[2]/h2/a'.format([n])).text)
def catch_news_time(n):
    return(driver.find_element_by_xpath('//*[@id="breaknews"]/div[1]/div{}/div[2]/div/time'.format([n])).text)
def catch_news_url(n):
    return(driver.find_element_by_xpath('//*[@id="breaknews"]/div[1]/div{}/div[2]/h2/a'.format([n])).get_attribute('href'))
def detail(new_num):
    new_num=new_num.replace('第','')
    new_num=new_num.replace('則新聞','')
    return(driver.find_element_by_xpath('//*[@id="breaknews"]/div[1]/div{}/div[2]/p/a'.format([int(new_num)])).text)
