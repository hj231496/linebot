# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第一章 Line Bot申請與串接
Line Bot機器人串接與測試
"""
#載入LineBot所需要的套件
from flask import Flask, request, abort
import re
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import time
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('1vmKFYz8QQclbvt3pdKXcjU40jdw21gmARxiLP0N6bB0dbM47tbAruTbr/jyg+UEMUrFsbucAREkn0YN3dpH5Rq7ruBTcD/iQ0bWVmV+EiPnNyrZWXcN5AsjIXU9xGd8HnKBkFcKkDnjWSPohZgUagdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('e2c72584113eafe24c4da5eadaa195d6')

line_bot_api.push_message('U2d6e82f55b58b4877296ca5bcdb33856', TextSendMessage(text='你可以開始了'))
for i in [1,2,3,4,5]:
    line_bot_api.push_message('U2d6e82f55b58b4877296ca5bcdb33856', 
                              TextSendMessage(text='我們來倒數：'+str(i)))
    time.sleep(1)
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

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
    message = text=event.message.text
    if re.match('你會做什麼',message):
        line_bot_api.reply_message(event.reply,TextSendMessage('關你屁事'))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(message))

    if re.match('告訴我秘密',message):
        # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )
        line_bot_api.reply_message(event.reply_token, sticker_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
