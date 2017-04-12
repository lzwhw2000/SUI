"""
1.mongodb 用户信息数据库 单张数据表大小16M上限，因此每张表10000条数据，这样带来的麻烦就是数据库中的值在多个表中可能重复
2.解决 1. 中的问题，用redis做缓存服务器，使用redis的set类型数据，最大上限是 2**32-1，亿万级单位存储，而且查询速度更快
3.递归 

Fatal Python error: Cannot recover from stack overflow. 
"""


#coding=utf-8
from xueqiu import session
import redis
from snowLog import logger
from pymongo import MongoClient
client = MongoClient()  # 默认连接 localhost:27017
db = client.lab
client = redis.Redis(host="localhost",port=6379,db=0)
if client.ping():
    logger.info("Connect to server successfully!")
else:
    logger.info("Connect to server failed!")
client.sadd("got","*")  #检查是否request过
client.sadd("inserted","*")  #检查是否存在数据库了
import random
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
url = "https://xueqiu.com/friendships/groups/members.json?uid={0}&gid=0&page={1}&_={2}"
import string
from time import sleep
def getRandom():
    x = ''
    s = string.digits
    for i in range(13):
        x+=''.join(random.choice(s))
    return x
urlinfo = (2450427100,4)
x = 1
def getInfo(urlinfo):
    global x
    client.sadd("got",urlinfo[0])  #查询过的就加入got
    looPage = urlinfo[1] + 1
    for i in range(looPage):
        sleep(1)
        headers['Referer'] = "https://xueqiu.com/"+str(urlinfo[0])
        try:
            r = session.get(url.format(urlinfo[0],i+1,getRandom()),headers=headers)
        except:
            continue
        users = r.json()['users']
        for raw in users:
            pages = raw['friends_count'] // 20 + 1
            uid = raw['id']
            if not client.sismember('inserted', uid):
                    if db["snow"+str(x)].count() > 10000:
                        x = x+1
                    try:
                        db["snow"+str(x)].insert_one(raw)
                        client.sadd('inserted', uid)
                        logger.info("Insert Successfully!")
                    except:
                        continue
            if not client.sismember('got',uid):
                try:
                    getInfo((raw['id'],pages))
                    client.sadd('got',uid)
                except:
                    logger.warning("anything wrong!")
if __name__ == '__main__':
    getInfo(urlinfo)