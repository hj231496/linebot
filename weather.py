from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument("--headless")
option.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=option)

result=[]
def catch_weather(contury):
    if contury=='北部':
        driver.get('https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=63')
    if contury=='中部':
        driver.get('https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=66')
    if contury=='南部':
        driver.get('https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=67')
    temp=driver.find_element_by_xpath('/html/body/div[2]/main/div/div[1]/div[3]/div[2]/ul/li[1]').text
    result=temp.split('\n')

    return(contury+'的天氣狀況:\n'+result[0]+'\n氣溫:'+result[1]+'\n'+result[2]+':'+result[3]+'\n體感狀況:'+result[4])








