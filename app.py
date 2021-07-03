# -*- coding: utf-8 -*-

#載入LineBot所需要的套件
from flask import Flask, request, abort
import re
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from weather import catch_weather
from news import news_data
from foodpanda import Nearest_restaurant
import json
from ABgame import getans,gaming
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('1vmKFYz8QQclbvt3pdKXcjU40jdw21gmARxiLP0N6bB0dbM47tbAruTbr/jyg+UEMUrFsbucAREkn0YN3dpH5Rq7ruBTcD/iQ0bWVmV+EiPnNyrZWXcN5AsjIXU9xGd8HnKBkFcKkDnjWSPohZgUagdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('e2c72584113eafe24c4da5eadaa195d6')
line_bot_api.push_message('U2d6e82f55b58b4877296ca5bcdb33856', TextSendMessage(text='請輸入:你會做什麼'))
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    #print(body)
    # handle webhook body
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
     message =event.message.text
     
     if re.match('你會做什麼',message):
         flex_message = TextSendMessage(text='請點選以下指令',
                                quick_reply=QuickReply(items=[
                                    QuickReplyButton(action=MessageAction(label="天氣", text="天氣")),
                                    QuickReplyButton(action=MessageAction(label="新聞", text="新聞")),
                                    QuickReplyButton(action=MessageAction(label="foodpanda", text="foodpanda")),
                                    QuickReplyButton(action=MessageAction(label="1A2B遊戲", text="1A2B遊戲"))
                                ]))
         line_bot_api.reply_message(event.reply_token, flex_message)
     #elif re.match('抽卡',message):
        #image_message = ImageSendMessage(
            #original_content_url='https://instagram.ftpe7-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s640x640/210242438_356745869129134_6500305790043252686_n.jpg?tp=1&_nc_ht=instagram.ftpe7-1.fna.fbcdn.net&_nc_cat=110&_nc_ohc=8RBR_Y6_Wp8AX8Nj5LR&edm=ABfd0MgBAAAA&ccb=7-4&oh=83a2875b28cee889888c318a72d4f60b&oe=60E3E73E&_nc_sid=7bff83',
            #preview_image_url='https://instagram.ftpe7-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s640x640/210242438_356745869129134_6500305790043252686_n.jpg?tp=1&_nc_ht=instagram.ftpe7-1.fna.fbcdn.net&_nc_cat=110&_nc_ohc=8RBR_Y6_Wp8AX8Nj5LR&edm=ABfd0MgBAAAA&ccb=7-4&oh=83a2875b28cee889888c318a72d4f60b&oe=60E3E73E&_nc_sid=7bff83'
        #)
        #line_bot_api.reply_message(event.reply_token, image_message)
     elif re.match('1A2B遊戲',message): 
         getans()
         msgarr=[]
         msgarr.append(TextSendMessage('給我四個不重複的數字\n假設數字對了位置對了，就是A\n假設數字對了位置錯了，就是B'))
         msgarr.append(TextSendMessage('舉例:\n你猜1234，答案是1324，這樣就是2A2B\n猜到4A就獲勝囉！'))
         msgarr.append(TextSendMessage('可以開始囉'))
         msgarr.append(TextSendMessage('請輸入四位不重複數字'))
         line_bot_api.reply_message(event.reply_token,msgarr)    
     elif message.isdigit():
         if len(message)!=4:
             line_bot_api.reply_message(event.reply_token,TextSendMessage('請重新輸入四位不重複數字'))   
         line_bot_api.reply_message(event.reply_token,TextSendMessage(gaming(message)))      
     elif re.match('新聞',message):
        news_data()
        FlexMessage = json.load(open('news.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('news',FlexMessage))
     elif re.match('天氣',message):#天氣模板    
         buttons_template_message = TemplateSendMessage(
         alt_text='天氣選單', #按鈕樣板內部註解
         template=ButtonsTemplate(
             thumbnail_image_url='https://i.ytimg.com/vi/ImsgAQKgl34/hqdefault.jpg',
             title='你住在哪裡',#樣板標題 
             text='全台天氣快報',#樣板介紹
             actions=[MessageAction(label='北部',text='北部'),MessageAction(label='中部',text='中部'),MessageAction(label='南部',text='南部'),URIAction(label='詳細全台天氣',uri='https://www.cwb.gov.tw/V8/C/W/County/index.html')]
         )
     )
         line_bot_api.reply_message(event.reply_token, buttons_template_message)#樣板建置完成後發送
     elif re.match('北部',message) or re.match('中部',message) or re.match('南部',message):
         line_bot_api.reply_message(event.reply_token, TextSendMessage(catch_weather(message)))
     elif re.match('foodpanda',message) or re.match('Foodpanda',message) or re.match('FoodPanda',message):
         msgarr=[]
         msgarr.append(TextSendMessage('我可以幫您找附近有開的foodpanda餐廳'))
         msgarr.append(TextSendMessage('並會依照距離來依序顯示'))
         msgarr.append(TextSendMessage('請回傳位置訊息給我並稍等唷'))
         
         line_bot_api.reply_message(event.reply_token,msgarr)
     else:line_bot_api.reply_message(event.reply_token,TextSendMessage('汪'))
@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    lat = str(event.message.latitude)  #緯度
    lon = str(event.message.longitude) #緯度
    Nearest_restaurant(lat,lon)
    FlexMessage = json.load(open('foodpanda.json','r',encoding='utf-8'))
    line_bot_api.reply_message(event.reply_token, FlexSendMessage('foodpanda',FlexMessage))

         

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8070))
    app.run(host='0.0.0.0', port=port)
