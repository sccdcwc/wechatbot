# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from wxpy import *
from config import *
from requests import get
from requests import post
from platform import system
from os import chdir
from random import choice
from threading import Thread
import configparser
import time
import sys

# 启动微信机器人，自动根据操作系统执行不同的指令
# windows系统或macOS Sierra系统使用bot = Bot()
# linux系统或macOS Terminal系统使用bot = Bot(console_qr=2)
dakalist=[]
if ('Windows' in system()):
    # Windows
    bot = Bot(cache_path=True)
elif ('Darwin' in system()):
    # MacOSX
    bot = Bot(cache_path=True)
elif ('Linux' in system()):
    # Linux
    bot = Bot(console_qr=2, cache_path=True)
else:
    # 自行确定
    print("无法识别你的操作系统类型，请自己设置")

def send_message(your_message):
    try:
        # 对方的微信名称
        my_group= bot.groups().search(group_name)[0]

        # 发送消息给对方
        my_group.send(your_message)
    except:

        # 出问题时，发送信息到文件传输助手
        bot.file_helper.send(u"守护程序出问题了，赶紧去看看咋回事~")

# 获取每日励志精句
def get_message():
    r = get("http://open.iciba.com/dsapi/")
    note = r.json()['note']
    content = r.json()['content']
    return note,content


# 在规定时间内进行关心她操作
def start_care():
    global dakalist
    # 待发送的内容，先置为空
    message = ""

    # 来个死循环，24小时关心她
    while(True):
        # 提示
        print("守护中，时间:%s"% time.ctime())
        # 每天定时问候，早上起床，中午吃饭，晚上吃饭，晚上睡觉
        # 获取时间，只获取时和分，对应的位置为倒数第13位到倒数第8位
        now_time = time.ctime()[-13:-8]
        if (now_time == say_good_morning):
            if (flag_learn_english):
                note, content = get_message()
            # 随机取一句问候语
                message = "早安，一起来学英语哦：\n" + "原文: " + content + "\n\n翻译: " + note+"\n记得打卡哟！"
            else:
                message="早安，记得打卡哟( ∙̆ .̯ ∙̆ )"
            str="已经打卡：\n"
            for item in dakalist:
                str+=item
            message+=str
            # 是否加上随机表情
            send_message(message)
            print("提醒早上打卡:%s" % time.ctime())
            dakalist=[]
        elif (now_time == say_good_dinner):
            message = "everybody,该打卡了！！！！"
            str = "已经打卡：\n"
            for item in dakalist:
                str = str+item+";"
            message += str
            send_message(message)
            dakalist = []
            print("提醒晚上打卡:%s" % time.ctime())

        elif (now_time == say_good_dream):
            # 是否在结尾加上每日学英语
            message = "晚安，早点休息哟(●'◡'●)ﾉ♥"
            send_message(message)
            print("提醒晚上睡觉:%s" % time.ctime())
        ## 节日问候语
        # festival_month = time.strftime('%m', time.localtime())
        # festival_day = time.strftime('%d', time.localtime())

        # if(festival_month == '02' and festival_day == '14' and now_time == "08:00"):
        #     send_message(str_Valentine)
        #     print("发送情人节祝福:%s" % time.ctime())
        #
        # elif(festival_month == '03' and festival_day == '08' and now_time == "08:00"):
        #     send_message(str_Women)
        #     print("发送三八妇女节祝福:%s" % time.ctime())
        #
        # elif(festival_month == '12' and festival_day == '24' and now_time == "00:00"):
        #     send_message(str_Christmas_Eve)
        #     print("发送平安夜祝福:%s" % time.ctime())
        #
        # elif(festival_month == '12' and festival_day == '25' and now_time == "00:00"):
        #     send_message(str_Christmas)
        #     print("发送圣诞节祝福:%s" % time.ctime())



        # # 生日问候语
        # if(festival_month == birthday_month and festival_day == birthday_day and now_time == "00:00"):
        #     send_message(str_birthday)
        #     print("发送生日祝福:%s" % time.ctime())

        # 每60秒检测一次
        time.sleep(60)
my_group = bot.groups().search(group_name)[0]  # 记得把名字改成想用机器人的群
tuling = Tuling(api_key='aa82f087376f44d5941bda3871d46a1d')  # 一定要添加，不然实现不了

t = Thread(target=start_care, name='start_care')
t.start()


@bot.register(my_group, except_self=False)  # 使用图灵机器人自动在指定群聊天
def reply_my_group(msg):
    global dakalist
    if "朱一龙" in msg.text:
        send_message("朱一龙喜欢大零零，不解释！")
    elif "白宇" in msg.text:
        send_message("白宇喜欢小明同学，没理由！")
    if "pika妹" in msg.text.lower():
        print(tuling.do_reply(msg))
    list=["打卡","打","卡","ka","daka","da"]
    for item in list:
        if item in msg.text.lower():
            name=msg.member.name
            print(name)
            if name not in dakalist:
                dakalist.append(name)
                break


# 注册好友请求类消息
@bot.register(msg_types=FRIENDS)
# 自动接受验证信息中包含 'wxpy' 的好友请求
def auto_accept_friends(msg):
    # 判断好友请求中的验证文本
    if '芝麻开门' in msg.text.lower():
        # 接受好友 (msg.card 为该请求的用户对象)
        new_friend = bot.accept_friend(msg.card)
        # 或 new_friend = msg.card.accept()
        # 向新的好友发送消息
        new_friend.send('哈哈，快来和我聊天吧！')

myfrieds=bot.friends()
@bot.register(myfrieds,except_self=True)
def reply_my_friend(msg):
    if msg.sender.name=="王嘉茹":
        result="白宇："
    elif msg.sender=="大零零":
        result="朱一龙："
    else:
        result=""
    txt=tuling.reply_text(msg)
    name=msg.sender.name
    txt="亲爱的%s，%s"%(name,txt)
    result=result+txt
    msg.sender.send(result)

mygroups=bot.groups()
mygroups.remove(my_group)
print(mygroups)
@bot.register(mygroups,except_self=True)
def reply_my_group(msg):
    if "聪聪" in msg.text.lower():
    # print(tuling.do_reply(msg))
        txt = tuling.reply_text(msg)
        msg.sender.send(txt)

embed()