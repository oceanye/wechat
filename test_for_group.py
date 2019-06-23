#coding=utf-8
import itchat
from itchat.content import TEXT
from itchat.content import *

@itchat.msg_register(TEXT, isGroupChat=True)
def group_text(msg):
    group  = itchat.get_chatrooms(update=True)
    from_user = ''
    from_group = ''
    to_group   = ''
    key_word = 'jd.'
    for g in group:
    #    print(g['NickName'])
        if g['NickName'] =='剪羊毛科技有限公司⚽️ ⚽️ ⚽️':#从群中找到指定的群聊
            from_group = g['UserName']
            print('find_from_group')
            #for menb in g['MemberList']:
            #   #print(menb['NickName'])
            #    if menb['NickName'] == "寿寿":#从群成员列表找到用户,只转发他的消息
            #       from_user = menb['UserName']
            #       break
        if g['NickName'] == '测试群2':#把消息发到这个群
            to_group = g['UserName']
            print('find_to_group')
    T1=msg.text
    if msg['FromUserName'] == from_group:
        ##if msg['ActualUserName'] == from_user:
        if T1.find('key_word')!=-1:
            print ('okay',T1)
            itchat.send(T1,to_group)

itchat.auto_login(hotReload=True)
itchat.run()
