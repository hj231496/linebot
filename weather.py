from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument("headless")
driver = webdriver.Chrome(chrome_options=option)


def weather(contury):
    if contury=='北部':
        driver.get('https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=63')
    if contury=='中部':
        driver.get('https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=66')
    if contury=='南部':
        driver.get('https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=67')
    temp=driver.find_element_by_xpath('/html/body/div[2]/main/div/div[1]/div[3]/div[2]/ul').text
    return(temp)






