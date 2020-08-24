#encoding:utf-8
import requests
import re
import time
import sys
import os
from urllib.parse import quote

#url = "http://www.uu898.com/newTrade.aspx?gm=156&area=1447&srv=8274&c=-2"
url = "https://www.uu898.com/newTrade.aspx?gm=156&area=1447&key="
#url = "http://www.uu898.com/newTrade.aspx?gm=156&area=1447&srv=8274&c=-2&sa=0"
urltixing = "http://miaotixing.com/trigger?id=tnjznfL&text="
boturl = "https://api.telegram.org/bot1057088352:AAFJwRdGgD7MqEKu20RBOYfL0aFi68CHNW4/sendMessage?chat_id=-1001116422009&text="

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Connection': 'keep-alive',
    'Referer': 'http://www.baidu.com/'
}


proxy='127.0.0.1:861'
proxies = {
    'http':'socks5://'+proxy,
    'https':'socks5://'+proxy,
}

def get_page(url):
    try:
        #response  = requests.get(url,headers=headers,proxies=proxies,timeout = 5)
        response  = requests.get(url=url,headers=headers,timeout = 5)
        #response  = requests.get(url,timeout = 5)
        #respone_gold = requests.get(urlgold)
        if response.status_code == 200:
            return response.text
        return None
    except:
        return None

def parse_page(url,keyword):
    keyword = quote(keyword)
    url = url+keyword
    #print(url)
    html = get_page(url)
    #print(html)    
    pattern = re.compile('<h2><a href=\"//(.*?)\" target=\"_blank\">.*?class=\"sp-ico ico-tu\"></i>(.*?)</a>.*?18px;\">(.*?)</span>',re.S)   
    items = re.findall(pattern,str(html))    
    for item in items[0:1]:
        #print(item)
        yield{
            'weburl':item[0],
            'name':item[1],
            'price':item[2]
        }
 

def cls():
    os.system('cls')





if __name__ == '__main__':
    
    while True:
        keyurl = 'https://raw.githubusercontent.com/ftmcu/c9spider/master/keyword'
        response  = requests.get(url=keyurl,headers=headers,timeout = 5)
        keywords = response.text.split('\n')
        del keywords[-1]
        js = len(keywords)
        record = []
        print(js)
        #if len(record)!=
        for keyword in keywords:
            keyword = keyword.strip('\n')
            print("当前关键词:{0}".format(keyword))
            #print(keyword)
            if not keyword:
                break
                pass
            
            #print(filename)
            results = parse_page(url,keyword)
            
            
            for result in results:
                title = result['name']
                title = title.replace('<em class=\'keyword-list\'>','')
                title = title.replace('</em>','')
                record.append(title)
        print('第一次记录为：')
        print(record)
        if len(record)==js:
            break
        else:
            pass
        time.sleep(5)

    while True:        
        for i in range(0,js):
            keyword = keywords[i]
            keyword = keyword.strip('\n')
            results = parse_page(url,keyword)
            for result in results:
                title = result['name']
                title = title.replace('<em class=\'keyword-list\'>','')
                title = title.replace('</em>','')
                if title in record:
                    print('当前关键词：{0}，没有更新'.format(keyword))
                else:
                    warning = ("UU有更新\n标题:{0}\n价格:{1}\n地址:{2}".format(title,result['price'],result['weburl']))
                    print(warning)
                    boturl2 = boturl+warning
                    response2  = requests.get(url = boturl2,headers=headers,timeout = 5)
                    record[i]=title
                    print('新的记录为:')
                    print(record)
            time.sleep(5)
                
