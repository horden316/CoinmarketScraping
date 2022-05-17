#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 13:58:43 2022

@author: horden
"""

import requests

for k in range(9):
    
    comment = requests.get('https://api-gravity.coinmarketcap.com/gravity/v3/gravity/search?symbol=BTC&start='+str(k)+'&handleOnly=false&latestSort=true')
    comment_json = comment.json()
    data=comment_json["data"]
    text_con=data[0]
    
    
    
    
    for i in range(len(data)):
        try:
            text_con=data[i]
            if ((text_con["textContent"] != "$BTC") and (text_con["textContent"] != "$BTC ")):#排除留言內容空白的
                final_text = text_con["textContent"].strip("$BTC") #刪除$BTC字樣
                final_text = final_text.strip("\n") #刪除有莫名其妙換行的
                final_text = final_text.lstrip()  #刪除左邊的空格
                if(text_con["bullish"]==True):#bullish標籤的
                    print(text_con["textContent"])
                    
                    path="BTC/pos/pos.txt" #指定檔案位置
                    with open(path,"a") as f: #選擇檔案開啟方式 "a"為append，不刪除原本的文字，另外新增上去
                        f.write(final_text+"\n\n")
                        
                elif(text_con["bullish"]==False):#bearish標籤的
                    print(text_con["textContent"])
                    
                    path="BTC/neg/neg.txt"
                    with open(path,"a") as f:
                        f.write(final_text+"\n\n")
            
            else:
                i+=1
        
        except:
            i+=1

