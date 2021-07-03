import json
from selenium import webdriver



def Nearest_restaurant(lat,lng):
    
   option = webdriver.ChromeOptions()
   option.add_argument("--window-size=1920,1080")
   option.add_argument("--allow-insecure-localhost")
   option.add_argument("--no-sandbox")
   option.add_argument("--headless")
   option.add_argument('--incognito')
   option.add_argument("--disable-javascript") 
   option.add_argument('--ignore-certificate-errors')
   option.add_argument('--allow-running-insecure-content')
   option.add_experimental_option('excludeSwitches', ['enable-automation']) 
   user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
   option.add_argument(f'user-agent={user_agent}')
   driver = webdriver.Chrome(chrome_options=option)

   driver.get('https://www.foodpanda.com.tw/restaurants/new?lat={}&lng={}&vertical=restaurants&sort=distance_asc'.format(lat,lng))
   ########json open######
   with open('foodpanda.json', 'r', encoding='utf-8') as f:
    food_data  = json.load(f)
   #######################
    

    for i in range(10):
        urlstr=driver.find_element_by_css_selector('#restaurant-listing-root > div > div.page-wrapper > main > div.organic-list > div > section.vendor-list-section.open-section > ul > li:nth-child({}) > a > figure > div > picture > div'.format(i+1)).get_attribute('style')
        urlstr=urlstr.replace('background-image: url("','')    
        urlstr=urlstr.replace('?width=400&height=292");','')
        #print(urlstr)
        #print(driver.find_element_by_css_selector('#restaurant-listing-root > div > div.page-wrapper > main > div.organic-list > div > section > ul > li:nth-child({}) > a > figure > figcaption > span > span.name.fn'.format(i+1)).text)
        food_data['contents'][i]['hero']['url']=str(urlstr)
        #標題#
        food_data['contents'][i]['body']['contents'][0]['text']=driver.find_element_by_css_selector('#restaurant-listing-root > div > div.page-wrapper > main > div.organic-list > div > section > ul > li:nth-child({}) > a > figure > figcaption > span > span.name.fn'.format(i+1)).text
        #print(driver.find_element_by_css_selector('#restaurant-listing-root > div > div.page-wrapper > main > div.organic-list > div > section > ul > li:nth-child({}) > a > figure > figcaption > span > span.ratings-component > span.rating > b'.format(i+1)).text)
        #print(driver.find_element_by_css_selector('#restaurant-listing-root > div > div.page-wrapper > main > div.organic-list > div > section > ul > li:nth-child({}) > a > figure > figcaption > ul.categories.summary > li.vendor-characteristic'.format(i+1)).text)
        #星星數
        food_data['contents'][i]['body']['contents'][1]['contents'][1]['text']=driver.find_element_by_css_selector('#restaurant-listing-root > div > div.page-wrapper > main > div.organic-list > div > section > ul > li:nth-child({}) > a > figure > figcaption > span > span.ratings-component > span.rating > b'.format(i+1)).text
        #描述
        food_data['contents'][i]['body']['contents'][2]['contents'][0]['contents'][0]['text']=driver.find_element_by_css_selector('#restaurant-listing-root > div > div.page-wrapper > main > div.organic-list > div > section > ul > li:nth-child({}) > a > figure > figcaption > ul.categories.summary > li.vendor-characteristic'.format(i+1)).text
        #print(driver.find_element_by_css_selector('#restaurant-listing-root > div > div.page-wrapper > main > div.organic-list > div > section > ul > li:nth-child({}) > a'.format(i+1)).get_attribute('href'))
        food_data['contents'][i]['action']['uri']=driver.find_element_by_css_selector('#restaurant-listing-root > div > div.page-wrapper > main > div.organic-list > div > section > ul > li:nth-child({}) > a'.format(i+1)).get_attribute('href')
        #最後一個樣板的圖片food_data['contents'][2]['hero']['url']
        #最後一個樣板的連結food_data['contents'][2]['body']['contents'][2]['action']['uri']
        food_data['contents'][10]['action']['uri']='https://www.foodpanda.com.tw/restaurants/new?lat={}&lng={}&vertical=restaurants&sort=distance_asc'.format(lat,lng)
    ###########json close#########
    with open('foodpanda.json', 'w', encoding='utf-8') as f:
     json.dump(food_data, f)
    #driver.close()
    ##############################

if __name__=='__main__':
    Nearest_restaurant(25.033710,121.564718)
