# 功能 输入ip实现端口扫描  输出 端口 端口状态  服务名  服务版本
# 命令行操作 >>nmap_Port_scan.py [ip]
import nmap
import sys
import time


# 端口扫描
def Port_Scan(ip):
    # 实例化
    nm = nmap.PortScanner()
    # 开始计时
    start = time.time()
    print("**端口扫描")
    print("**开始扫描...")
    # 设置参数  -sT tcp扫描 -sU upd 扫描 -sS syn扫描 -sV 输出服务版本
    nmScan = nm.scan(hosts=ip, ports='1-65535', arguments='-sS -sV')
    # 判断主机是否存在
    if nm.all_hosts():
        # 分别显示 TCP 和 UPD 端口
        if nm[ip].all_tcp() or nm[ip].all_udp():
            print("**扫描结果：")
            try:
                # 显示TCP 端口信息
                print("-"*16+"TCP"+"-"*16)
                print("PORT" + "\t" + "STATE" + "\t" + "SERVICE" + "\t" + "VERSION")
                for i in nm[ip].all_tcp():
                    print(str(i) + "\t" +
                          nmScan['scan'][ip]['tcp'][i]['state'] + "\t" +
                          nmScan['scan'][ip]['tcp'][i]['name'] + "\t" +
                          nmScan['scan'][ip]['tcp'][i]['version'])
            except:
                pass
            try:
                # 显示UDP 端口信息
                print("-"*16+"UDP"+"-"*16)
                print("PORT" + "\t" + "STATE" + "\t" + "SERVICE" + "\t" + "VERSION")
                for i in nm[ip].all_tcp():
                    print(str(i) + "\t" +
                          nmScan['scan'][ip]['udp'][i]['state'] + "\t" +
                          nmScan['scan'][ip]['udp'][i]['name'] + "\t" +
                          nmScan['scan'][ip]['udp'][i]['version'])
            except:
                pass
        else:
            print("**找到主机，未发现主机端口")
    else:
        print("**未找到主机")
    # 结束计时
    end = time.time()
    # 输出程序执行时长
    print("time" + str(end - start)[0:4] + "s")


def main():
    ip = sys.argv[1]
    Port_Scan(ip)


if __name__ == '__main__':
    main()
