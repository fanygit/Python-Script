# 功能：使用tcp全连接方式对常用端口进行扫描 
# 使用方法：sudo python3 syn_port_scan.py [ip]
from scapy.all import *
import time
import sys

def get_port():
    port = [21,22,23,25,53,69,79,80,110,111,113,119,135,137,139,161,389,443,1080,2601,2604,5900,8080,5554,7626,8011,7306,1024,7001,7002,9080,9090,8080,3306,1433,1434,1521,5432,1158,8080,2100,443,512,513,514,873,2375,5984,6379,7001,7002,9200,9300,11211,27017,27018,28017,50000,50070,50030]
    return port

def scan(host):
    start = time.time()
    for port in get_port():
        tcp = IP(dst=host)/TCP(dport=port,flags="S")
        res = sr1(tcp,timeout=2,verbose=0)
        if res is not None:
            if res['TCP'].flags == "SA":
                res_1 = sr1(IP(dst=host)/TCP(dport=port,flags="AR"),timeout=2,verbose=0)
                print("[+] %d open " %(port))
            elif res['TCP'].flags == "RA":
                print("[+] %d Closed  "  %(port))
        else:
            print("[+] %d Closed res:None  "%(port))
    end = time.time()
    print("time: " + str(end-start)[0:4] + "s" )

def main():
    host = sys.argv[1]
    scan(host)


if __name__ =='__main__':
    main()
