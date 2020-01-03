# 功能：使用syn半开式对端口扫描
# 使用方法：
# ubuntu:   sudo python3 syn_port_scan.py [ip]
from scapy.all import *
import sys

def get_port():
    port = [21,22,23,25,53,69,79,80,110,111,113,119,135,137,139,161,389,443,1080,2601,2604,5900,8080,5554,7626,8011,7306,1024,7001,7002,9080,9090,8080,3306,1433,1434,1521,5432,1158,8080,2100,443,512,513,514,873,2375,5984,6379,7001,7002,9200,9300,11211,27017,27018,28017,50000,50070,50030]
    return port

def scan(host):
    # 构建发送数据包
    for port in get_port():
        syn = IP(dst=host)/TCP(dport=port,flags="R")
        res = sr1(syn,timeout=2,verbose=0)
        # 格式化输出结果
        if res is not None:
            if res['TCP'].flags =="SA":
                res_1 = sr1(IP(dst=host)/TCP(dport=port,flags="AR"),timeout=0,verbose=0)
                print("[+] %d open flags=%s " %(port,res['TCP'].flags))
            elif res['TCP'].flags == "RA":
                print("[+] %d Closed " %(prot))
        else:
            print("[+] %d Closed res:None " %(port))

def main():
    host = sys.argv[1]
    scan(host)


if __name__ == '__main__':
    main()
