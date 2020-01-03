import sys
import getopt #命令行解析
from optparse import OptionParser
from scapy.all import *

def arp_scan(host):
    arp = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=host)
    res = srp(arp,timeout=2,verbose=0)
    print("[+] Scaned %d host"%(len(res)))
    print("HOST             MAC")
   
   # res 返回两个结果 答复和未答复 [0]为答复 [1]为未答复
   # res[0] 中存在多个返回的数据包,每一个数据包都有Ether、ARP、数据部分
   # h['ARP'] 是选择数据包的ARP部分 
   # .psrc 为目标ip地址 .hwsrc 为目的mac地址

    for s,h in res[0]:
        print("{}    {}".format(h['ARP'].psrc,h['ARP'].hwsrc))
#第一种解析
def args():
    args,opts =  getopt.getopt(sys.argv[1:],'-h:',['--host'])
    for name,value in args:
        if name in ('-h','--host'):
            host = value
        else:
            print("-h --host :-h [host] ")
            exit()
    return host
# 第二种解析
def parse():
    # 创建实例
    parser = OptionParser()
    parser.add_option('-i','--host',dest='host',help="-i [ip] --host [ip] :set host")
    (options,args)  = parser.parse_args()
    return options.host
    
def main():
    # 第一种解析
    #host = args()
    # 第二种解析
    host = parse()
    arp_scan(host)


if __name__ == '__main__':
    main()
