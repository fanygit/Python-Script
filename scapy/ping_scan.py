# 功能 用ICMP协议探测主机是否在线
# 用法 python3 ping_scan.py [ip]
from scapy.all import *
import sys
import getopt
from random import randint
def ping_scan(host):
    # 参数准备
    ip_id = randint(0,65535)
    icmp_seq = randint(0,65535)
    icmp_id = randint(0,65535)
    # 构建发送ICMP包
    icmp = IP(dst=host,ttl=64,id=ip_id)/ICMP(seq=icmp_seq,id=icmp_id)/b'welcome'
    res = sr1(icmp,timeout=2,verbose=0)
    # 输出结果
    if res:
        print("[+] 主机存在 ")
        print("[+] 返回ICMP包信息")
        print(res['ICMP'].show())
    else:
        print("[+] 数据包未到达")
# 第一种解析方式
def args():
   getopt.getopt(sys.argv[1:],'-h:',['-host'])

def main():
    host = sys.argv[1]
    ping_scan(host)


if __name__ == '__main__':
    main()
