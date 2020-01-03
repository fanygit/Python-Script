# 功能 检测是否存在常见高危漏洞  ms07-010 ms08-067
# 命令行调用方式 >>nmap_Arp_scan.py [ip]
import nmap
import sys
import time

# 执行扫描
def scan(hosts, arguments):
    # 实例化
    nm = nmap.PortScanner()
    # scan() 以指定方式扫描主机
    # 扫描计时
    start = time.time()
    print("**漏洞扫描")
    print("**开始扫描...")
    nmScan = nm.scan(hosts=hosts, ports=None, arguments=arguments)
    print("**执行命令：{command}".format(command=nm.command_line()))
    # print(nmScan['scan'][hosts])
    # 根据扫描返回信息特征来进行判断是否存在漏洞
    try:
        print("**扫描结果：")
        if nm.all_hosts() and nmScan['scan'][hosts]['hostscript']:
            # 以下是主要特征 如果存在结果集 就会存在漏洞
            # 条件 nmScan['scan'][hosts]['hostelries'] 表示结果集
            # 用 len(nmScan['scan'][hosts]['hostscript']) 输出查询的结果集

            for i in range(len(nmScan['scan'][hosts]['hostscript'])):
                print(
                    "**主机{hosts}存在{id}漏洞".format(hosts=hosts, id=nmScan['scan'][hosts]['hostscript'][i]['id']))
                print(nmScan['scan'][hosts]['hostscript'][i]['id'])
                print(nmScan['scan'][hosts]['hostscript'][i]['output'])
                print("-" * 16)
        else:
            print("**未找到主机！")
    except:
        if nm.all_hosts():
            print("**主机{hosts}不存在漏洞！".format(hosts=hosts))
        else:
            print("**未找到主机")
    end = time.time()
    print("time:"+ str(end-start)[0:4] + "s")


# 设置参数
def main():
    # 命令行获取IP
    hosts = sys.argv[1]

    # 参数 默认扫描 ms08-067 ms17-010
    arguments = "--script smb-vuln-ms08-067 --script smb-vuln-ms17-010 "

    # 调用扫描
    scan(hosts, arguments)


if __name__ == '__main__':
    main()
