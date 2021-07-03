from selenium import webdriver
import json
option = webdriver.ChromeOptions()
option.add_argument("--headless")
option.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=option)


driver.get('https://udn.com/news/breaknews/1')



def news_data():
    with open('news.json', 'r', encoding='utf-8') as f:
      news  = json.load(f)
    for i in range(4):
        str=driver.find_element_by_xpath('//*[@id="breaknews"]/div[1]/div[{}]/div[1]/a/picture/img'.format(i+1)).get_attribute("src")
        str=str.replace('https://pgw.udn.com.tw/gw/photo.php?u=','')
        str=str.replace(str[str.find('&'):len(str)],'')
        news['contents'][i]['hero']['url']=str
        news['contents'][i]['body']['contents'][0]['text']=driver.find_element_by_xpath('//*[@id="breaknews"]/div[1]/div[{}]/div[2]/h2/a'.format(i+1)).text
        news['contents'][i]['body']['contents'][1]['text']=driver.find_element_by_xpath('//*[@id="breaknews"]/div[1]/div[{}]/div[2]/div/time'.format(i+1)).text
        news['contents'][i]['footer']['contents'][0]['action']['displayText']=driver.find_element_by_xpath('//*[@id="breaknews"]/div[1]/div[{}]/div[2]/p/a'.format(i+1)).text
        news['contents'][i]['footer']['contents'][1]['action']['uri']=driver.find_element_by_xpath('//*[@id="breaknews"]/div[1]/div[{}]/div[2]/h2/a'.format(i+1)).get_attribute('href')
    with open('news.json', 'w', encoding='utf-8') as f:
     json.dump(news, f)

if __name__=='__main__':
    news_data()