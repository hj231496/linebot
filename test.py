import requests
def foodpanda( city_name):
    #建立縣市相對應網址字典
    city = {"台北市":"taipei-city", "新北市":"new-taipei-city", "台中市":"taichung-city","高雄市":"kaohsiung-city",
            "新竹市":"hsinchu-city", "桃園市":"taoyuan-city", "基隆市":"keelung","台南市":"tainan-city",
            "苗栗市":"miaoli-county", "嘉義市":"chiayi-city", "彰化市":"changhua", "宜蘭縣":"yilan-city",
            "屏東縣":"pingtung-city", "雲林縣":"yunlin-county", "花蓮市":"hualien", "南投市":"nantou-county",
            "台東市":"taitung-county","澎湖縣":"penghu-city", "金門縣":"kinmen-city"}
    
    if city_name in city:
        city_url = city[city_name]
        url = "https://www.foodpanda.com.tw/city/"+city_url
        #如果輸入名稱在字典內,取得相對應網址
        
        header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            }
        
        
        session = requests.Session()
        url = session.get(url, headers = header)
        print(url.text)

foodpanda("台北市")