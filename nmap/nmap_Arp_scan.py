# 功能 实现对ip段进行主机发现  发现主机后 显示存活主机ip和mac地址
# 调用方式 >>nmap_Arp_scan.py [ip段]

import nmap
import sys
import time

# 执行arp 主机发现
def arp_scan(ip):
    # 创建解析器
    nm = nmap.PortScanner()
    # 开始计时
    start= time.time()
    print("**主机发现")
    print("**开始扫描...")
    # 指定参数 并扫描
    nmScan = nm.scan(hosts=ip, arguments='-PR')
    # nm.all_hosts() 代表存活的主机
    num = nm.all_hosts()
    if len(num) > 1 :
        print("**主机存活状态：")
        print("Host" + '\t\t' + "STATE" )
        for i in num:
            try:
                print(i + '\t' +  nmScan['scan'][i]['status']['state'] )
            except:
                pass
            try:
                print("MAC:" + nmScan['scan'][i]['addresses']['mac'] )
            except:
                print("无MAC")
    else:
        print("**未发现主机")

    # 结束计时
    end = time.time()
    # 输出扫描所用时间
    print("time:"+str(end-start)[0:4] + "s")

# 设置参数
def main():
    # 命令行解析
    ip = sys.argv[1]
    arp_scan(ip)


if __name__ == '__main__':
    main()
