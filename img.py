from selenium import webdriver
import random
option = webdriver.ChromeOptions()
option.add_argument("--window-size=1920,1080")
option.add_argument("--allow-insecure-localhost")
option.add_argument("--no-sandbox")
#option.add_argument("--headless")
option.add_argument('--incognito')
option.add_argument("--disable-javascript") 
option.add_argument('--disable-gpu')
option.add_argument('--ignore-certificate-errors')
option.add_argument('--allow-running-insecure-content')
option.add_experimental_option('excludeSwitches', ['enable-automation']) 
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
option.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(chrome_options=option)


driver.get('https://www.facebook.com/timliaofb.beauty/photos')
n1=random.randint(1,10)
n2=random.randint(1,10)

girl=driver.find_element_by_css_selector('#mount_0_0_Kc > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.l9j0dhe7.dp1hu0rb.cbu4d94t.j83agx80 > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div > div > div:nth-child(3) > div > div > div > div.bq4bzpyk.j83agx80.btwxx1t3.lhclo0ds.jifvfom9.muag1w35.dlv3wnog.enqfppq2.rl04r1d5 > div:nth-child(1) > div > a > div > div > img')
girl.click()
print(girl)
driver.close()
