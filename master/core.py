from redis_client import r_client
from mongodb_client import Mdb
import requests
import string
import random
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from queue import Queue
import time
from logger import logger
from login import session


db_id = 36
#r_client.sadd("Got","*")   # requested
#r_client.sadd("Queue","*")  # wait to request
#r_client.sadd("Inserted","*")   # inserted to db to be unique

url = "https://xueqiu.com/friendships/groups/members.json?uid={0}&gid=0&page={1}&_={2}"
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

def getRandom():
    rom = ''
    s = string.digits
    for i in range(13):
        rom+=''.join(random.choice(s))
    return rom

def do_request(id_unique,page,followers):  #process page info   **all network request**
    """
    users
    :return: json
    """
    headers['Referer'] = "https://xueqiu.com/" + str(id_unique)
    try:
        paging = session.get(url.format(id_unique,page,getRandom()),headers=headers)
        followers.extend(paging.json()["users"])
    except:
        logger.warn("{} request failed".format(id_unique))


#return dick of all followers by mutli
def getFollowers(id_unique,maxPage):
    id_followers = []
    threads = []
    for page in range(maxPage):
        t = Thread(target=do_request,args=(id_unique,page+1,id_followers,))
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        if thread.isAlive():
            thread.join()
    return id_followers

def parse(id_unique):   #process id
    global db_id
    headers['Referer'] = "https://xueqiu.com/" + str(id_unique)
    try:
        mainPage = session.get(url.format(id_unique, 1, getRandom()), headers=headers)
    except:
        logger.warn("id {} request failed.".format(id_unique))
    maxPage = mainPage.json()["maxPage"]
    """
    threading pool process the rest of page
    """
    followers = []

    followers = getFollowers(id_unique,maxPage)  # get all followers' list contain dict type
        #logger.warn("threading maybe wrong from {}".format(id_unique))
    for follower in followers:
        #insert id to redis and insert dict to db
        uid = follower['id']
        if r_client.sismember("Inserted",uid):
            followers.remove(follower)
        else:
            r_client.sadd("Inserted",uid)

        if not r_client.sismember("Got",uid):
            r_client.sadd("Queue",uid)
    if Mdb["snowball" + str(db_id)].count() > 10000:
        db_id = db_id + 1
    Mdb["snowball" + str(db_id)].insert_many(followers)
    logger.info("Your insert {} 's {} followers successfully.".format(id_unique,len(followers)))
    r_client.sadd("Got",id_unique)

def main():
    while r_client.scard("Queue")!=0:
        id_wait_req = r_client.spop("Queue").decode('utf-8')
        try:
            parse(id_wait_req)
            #time.sleep(0.1)
        except:
            #r_client.sadd("Error",id_wait_req)
            logger.warn("database operation failed,parse_id {}".format(id_wait_req))
if __name__ == '__main__':
    r_client.sadd("Queue",9507349744)
    main()


"""
多线程处理网络请求
单线程完成循环调用主函数
"""















