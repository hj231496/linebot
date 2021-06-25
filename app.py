# -*- coding: utf-8 -*-

#載入LineBot所需要的套件
from flask import Flask, request, abort
import re
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import time
from weather import catch_weather
from news import catch_news_graphic, catch_news_text,catch_news_time, catch_news_url,detail

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('1vmKFYz8QQclbvt3pdKXcjU40jdw21gmARxiLP0N6bB0dbM47tbAruTbr/jyg+UEMUrFsbucAREkn0YN3dpH5Rq7ruBTcD/iQ0bWVmV+EiPnNyrZWXcN5AsjIXU9xGd8HnKBkFcKkDnjWSPohZgUagdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('e2c72584113eafe24c4da5eadaa195d6')

line_bot_api.push_message('U2d6e82f55b58b4877296ca5bcdb33856', TextSendMessage(text='你可以開始了'))
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(body)
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
         line_bot_api.reply_message(event.reply_token, TextSendMessage('我現在只會找天氣，請輸入天氣'))
     if re.match('新聞',message):
        carousel_template_message = TemplateSendMessage(
             alt_text='新聞樣板',
             template=CarouselTemplate(
                 columns=[
                     CarouselColumn(
                         thumbnail_image_url=catch_news_graphic(1),
                         title=catch_news_text(1),
                         text=catch_news_time(1),
                         actions=[MessageAction(label='詳細內容',text= '第1則新聞'),URIAction(label='馬上查看',uri=catch_news_url(1))]
                     ),
                     CarouselColumn(
                         thumbnail_image_url=catch_news_graphic(2),
                         title=catch_news_text(2),
                         text=catch_news_time(2),
                         actions=[MessageAction(label='詳細內容',text= '第2則新聞'),URIAction(label='馬上查看',uri=catch_news_url(2))]
                     ),
                      CarouselColumn(
                         thumbnail_image_url=catch_news_graphic(3),
                         title=catch_news_text(3),
                         text=catch_news_time(3),
                         actions=[MessageAction(label='詳細內容',text= '第3則新聞'),URIAction(label='馬上查看',uri=catch_news_url(3))]
                     )
                 ]
             )
         )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
     elif re.match('第1則新聞',message) or re.match('第2則新聞',message) or re.match('第3則新聞',message):
         line_bot_api.reply_message(event.reply_token, TextSendMessage(detail(message)))
    

     if re.match('天氣',message):#天氣模板
         buttons_template_message = TemplateSendMessage(
         alt_text='天氣選單', #按鈕樣板內部註解
         template=ButtonsTemplate(
             thumbnail_image_url='https://i.imgur.com/GGV9AQv.jpeg',
             title='你住在哪裡',#樣板標題 
             text='你他媽說喔',#樣板介紹
             actions=[MessageAction(label='北部',text='北部'),MessageAction(label='中部',text='中部'),MessageAction(label='南部',text='南部')]
         )
     )
         line_bot_api.reply_message(event.reply_token, buttons_template_message)#樣板建置完成後發送
     elif re.match('北部',message) or re.match('中部',message) or re.match('南部',message):
         line_bot_api.reply_message(event.reply_token, TextSendMessage(catch_weather(message)))
    


         
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
