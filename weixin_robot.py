#!/usr/bin/env python
# coding: utf-8
import urllib2
import json
import sys


from wxbot import *


class MyWXBot(WXBot):

    def getHtml(url):
        page = urllib2.urlopen(url)
        html = page.read()
        return html

    def handle_msg_all(self, msg):
        key = '**********************'
        api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            info = msg['content']['data']
            request = api + info
            page = urllib2.urlopen(request)
            response = page.read()
            dic_json = json.loads(response)
            reply_text = dic_json['text']
            self.send_msg_by_uid(reply_text, msg['user']['id'])
            #self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            #self.send_file_msg_by_uid("img/1.png", msg['user']['id'])
'''
    def schedule(self):
        self.send_msg(u'张三', u'测试')
        time.sleep(1)
'''
def main():
    reload(sys)
    sys.setdefaultencoding('utf8')
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.is_big_contact = False
    bot.run()


if __name__ == '__main__':
    main()
