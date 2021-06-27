import json
import time
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("--headless")
option.add_argument('--incognito')

option.add_argument('--disable-gpu')
option.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
driver = webdriver.Chrome(chrome_options=option)


def Nearest_restaurant(lat,lng):
   driver.get('https://www.foodpanda.com.tw/restaurants/new?lat={}&lng={}&vertical=restaurants&sort=distance_asc'.format(lat,lng))
   ########json open######
   with open('foodpanda.json', 'r', encoding='utf-8') as f:
    food_data  = json.load(f)
   #######################
    

    for i in range(2):
        
        urlstr=driver.find_element_by_css_selector('#restaurant-listing-root > div > div.page-wrapper > main > div.organic-list > div > section.vendor-list-section.open-section > ul > li:nth-child({}) > a > figure > div > picture > div'.format(i+1)).get_attribute('style')
        urlstr=urlstr.replace('background-image: url("','')    
        urlstr=urlstr.replace('?width=400&height=292");','')
        food_data['contents'][i]['hero']['url']=str(urlstr)
        #標題food_data['contents'][0]['body']['contents'][0]['text']
        #星星數food_data['contents'][0]['body']['contents'][1]['contents'][1]['text']
        #描述food_data['contents'][0]['body']['contents'][2]['contents'][0]['contents'][0]['text']
        #最後一個樣板的圖片food_data['contents'][2]['hero']['url']
        #最後一個樣板的連結food_data['contents'][2]['body']['contents'][2]['action']['uri']
    ###########json close#########
    with open('foodpanda.json', 'w', encoding='utf-8') as f:
     json.dump(food_data, f)
    ##############################

if __name__=='__main__':
    Nearest_restaurant('23.0124556','120.2324031')