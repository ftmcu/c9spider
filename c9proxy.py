#encoding:utf-8
import requests
import re
import time
import os
import minimu
import zmail

'''
host_server = 'smtp.163.com'
sender_qq = 'legend0002@163.com'
pwd = ''
sender_qq_mail = 'legend0002@163.com'
receiver = 'legend0002@qq.com'
'''


mail_title = '喜游戏官网更新啦'

proxy='5.196.132.122:3128'
proxies = {
    'http':'http://'+proxy,
    'https':'https://'+proxy,
}
url = "http://c9.xiyouxi.com/article/index.html"
'''
<li>.*?<a href="http://c9.xiyouxi.com/article/.*?" target="_blank">(.*?)</a><span>2019.*?</span></li>
'''
def get_page(url):
    try:
        response  = requests.get(url,proxies=proxies,timeout = 5)
        if response.status_code == 200:
            return response.text
        return None
    except:
        return None


def parse_page(html):
    pattern = re.compile('<li>.*?<a href="http://c9.xiyouxi.com.*?" target="_blank">(.*?)</a><span>2019.*?</span></li>',re.S)
    global items
    items = re.findall(pattern,str(html))
    return items



def sendEmail():
    mail = {
    'subject': '喜游戏官网更新啦!!',  # Anything you want.
    'content_text': 'This message from zmail!喜游戏官网更新啦!{0}'.format(items),  # Anything you want.
    #'attachments': ['/Users/zyh/Documents/example.zip','/root/1.jpg'],  # Absolute path will be better.
}

    server = zmail.server('legend0002@outlook.com', 'wsfttc1990')

    server.send_mail('ftmcuc@gmail.com', mail)

def playmusic(path):
    try:
        song = minimu.load(path)
        song.play()
        time.sleep(60)
        song.stop()
    except ValueError:
        return  None

def main():

    html = get_page(url)
    if html == None:
        print("暂时连不上网")
    else:
        global old_list
        newlist = parse_page(html)
    # print(newlist)
        if old_list != newlist:
            for i in newlist:
                print(i)
            print("updated")
            sendEmail()
            playmusic('mainmenu.mp3')
            old_list = newlist
        else:
            #print(old_list)
            for i in newlist:
                print(i)
            print("没有更新")


if __name__ == '__main__':
    #receiver = input("请输入收件邮箱：")
    print('')
    i=0
    html = get_page(url)
    old_list = parse_page(html)
    #old_list = [1,2]
    #print(old_list)
    time.sleep(3)
    print('')
    while True:
        print("当前时间：{0}".format(time.asctime(time.localtime(time.time()))))
        print('')
        main()
        time.sleep(30)
        print('')
        os.system("cls")
