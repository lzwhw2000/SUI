# -*- coding: utf-8 -*-
'''
@Referfer xchaoinfo 
'''

import requests
import hashlib
import re


# 构造 Request headers
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
headers = {
    'User-Agent': agent,
    'Host': "xueqiu.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.6",
    "Connection": "keep-alive"
}

session = requests.session()


# 密码的 md5 加密
def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest().upper()


def login(telephone, password):
    url = 'https://xueqiu.com/'
    session.get(url, headers=headers)  # 访问首页产生 cookies
    headers['Referer'] = "https://xueqiu.com/"
    login_url_api = "https://xueqiu.com/service/csrf?api=%2Fuser%2Flogin"  # 模拟更真实的请求
    session.get(login_url_api, headers=headers)
    login_url = "https://xueqiu.com/user/login"
    postdata = {
        "areacode": "86",
        "password": get_md5(password),
        "remember_me": "on",
        "telephone": telephone
    }
    log = session.post(login_url, data=postdata, headers=headers)
    log = session.get("https://xueqiu.com/setting/user", headers=headers)
    pa = r'"profile":"/(.*?)","screen_name":"(.*?)"'
    res = re.findall(pa, log.text)
    if res == []:
        print('try angin\n')
        #print("登录失败，请检查你的手机号和密码输入是否正确")
    else:
        print('\nwelcome {}\n'.format(res[0]))


telephone = ""
password = ""
login(telephone, password)



