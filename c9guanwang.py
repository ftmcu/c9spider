
import requests
import re
import time
import minimu
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header

#qq邮箱smtp服务器
host_server = 'smtp.163.com'
#sender_qq为发件人的qq号码
sender_qq = 'legend0002@163.com'
#pwd为qq邮箱的授权码
pwd = 'wsfttc1990' ## xh**********bdc
#发件人的邮箱
sender_qq_mail = 'legend0002@163.com'
#收件人邮箱
receiver = 'ftmcu.c@gmail.com'

#邮件的正文内容
mail_content = '喜游戏更新活动了，打开看看吧'
#邮件标题
mail_title = '喜游戏官网更新啦'


url = "http://c9.xiyouxi.com/article/lists/4.html"
'''

'''
def get_page(url):
    try:
        response  = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_page(html):
    pattern = re.compile('<li>【活动新闻】<a href=.*?blank">(.*?)</a><span>.*?</span></li>',re.S)
    items = re.findall(pattern,html)
    #print(items)
    return items



def playmusic(path):
    song = minimu.load(path)
    song.play()
    time.sleep(194)
    song.stop()


def sendEmail():
    smtp = SMTP_SSL(host_server)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    #smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()



def main():
    html = get_page(url)
    #print(html)
    global old_list
    newlist = parse_page(html)
    #print(newlist)
    for item in newlist:
        #print('\033[1;33m{0}\033[0m'.format(item['name']),end = '  ')
        #print('\033[3;31m{0}\033[0m' .format(item['price']))
        print('{0}'.format(item))
    if old_list != newlist:
        print("updated")
        sendEmail()
        playmusic('mainmenu.mp3')
        old_list = newlist


if __name__ == '__main__':
    print('')
    html = get_page(url)
    old_list = parse_page(html)
    #old_list = [1,2]
    main()
    time.sleep(60)
    print('')
    while True:
        print("当前时间：{0}".format(time.asctime(time.localtime(time.time()))))
        print('')
        main()
        time.sleep(60)
        print('')