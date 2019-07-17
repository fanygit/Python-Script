from bs4 import BeautifulSoup
import requests
import re
import os


class doutula():

    def all_url(self,url):
        resp=self.request(url)
        path = "E:\doutula"  # 路径
        self.mkdir(path)
        self.name_and_url(resp)

    def mkdir(self,path):
        # 去除首尾空格
        path = path.strip()
        # 去除尾部\符合
        path = path.rstrip("\\")
        # 判断路径是否存在
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            print(path + "创建成功")
            os.chdir(path)
            return True
        else:
            print(path + "目录已存在")
            os.chdir(path)
            return False
    def request(self,url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36'}
        resp = requests.get(url, headers)
        return resp
    def name_and_url(self,resp):
        soup = BeautifulSoup(resp.text, 'lxml').find('div', class_='page-content text-center').find_all('img')
        i=0 #计数
        for temp in soup:
            temp = str(temp)
            dt_url = re.search('https://[a-z1-9]+.[a-z]+.\w{2,3}/[a-z]+/[a-z0-9A-Z]{30,40}.[a-z]{3}'
                               '|http://[a-z]{3}.[a-z]+.[a-z]{2,3}/[a-z]+/[a-z]+/[a-z]+//([0-9]{4}/[0-9]{2}/[0-9]{2})/[0-9]+_[a-zA-Z0-9]+.[a-z]{3,4}![a-z]{3}',
                               temp)
            dt_name = re.search('[\u4e00-\u9fa5]+', temp)
            if dt_url and dt_name:
                i += 1
                print(i)
                print(dt_name.group(0))
                print(dt_url.group(0))
                name=dt_name.group(0)
                url=dt_url.group(0)
                resp = self.request(url)
                self.sava(resp,name)

    def sava(self,resp,name):
        f = open(name + '.jpg', 'ab')
        f.write(resp.content)
        f.close()



#保存图片

def main():
    doutula1=doutula()


    i=1
    while True:
            url="https://www.doutula.com/photo/list/?page="+ str(i)   #网址
            if i<=2: #爬取页数
                doutula1.all_url(url)
                i+=1
            else:
                break




if __name__ == '__main__':
	main()

