import urllib.request
import re
import time
import os
# 流程
# 请求->处理->返回
# 1.获取首页url 2.获取首页url里的图片url 3.获取图片url的值 4.创建文文件夹保存
# 多线程爬取
class Mzimg(object):
    # 获取html源码
    def get_html(self,url):
        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'
            }
        # 添加headers
        request = urllib.request.Request(url=url,headers=headers)
        try:
            # 获取页面源码
            resp = urllib.request.urlopen(request,timeout=10)
            # 用gbk解析页面源码(使用utf-8会出错) 并对内容进行切片(因为正则会匹配到其他不相干内容，所以对内容进行切片,以保证指定区域url被爬取) 并返回
            # 经过不断调试 切片区块为[6800:-4800]
            result = resp.read().decode('gbk',errors='ignore')[6800:-4800]
            result_lenth = len(result)
            return result,result_lenth
        except:
            print("[-] 请求失败 可能网络故障")
            return False

    # 获取首页url
    def get_page_url(self,url):
       
       # 获取源码
       print("[*] 正在请求url：%s" %(url))
       try: 
           res,res_len = self.get_html(url)
           print("[+] 字节：%d"%(res_len))
           ''' 
           f = open('/home/yangfan/Code/Python/_urllib/file_name.txt','w')
           f.write(res)
           f.close()
           '''
           # 正则匹配url
           list1 = re.findall('https://www.meizitu.com/a/\d{1,5}.html',res)
           page_url_list=[]
           # 去掉重复url
           for i in list1:
               if i not in page_url_list:
                   page_url_list.append(i)
           #print(url_list)
           print("[+] url：%s"%(url))
           print("[+] 获取url数量：%d"%(len(page_url_list)))
           # 返回页面所有url
           return page_url_list
       except:
            print("[-] 请求失败")
            return False

    # 获取page页面的所有img_url
    def get_img_url(self,page_url):
        print("[*] 正在请求url：%s"%(page_url))
        try:
            res,res_len = self.get_html(page_url)
            list1 = re.findall("http://pic.topmeizi.com/wp-content/uploads/\d{4}a/\d{2}/\d{2}/\d{2}.jpg",res)
            #print(list1)
            img_url_list = []
            # 去掉重复的url
            for i in list1:
                if i not in img_url_list:
                    img_url_list.append(i)
            print("[+] url：%s"%(page_url))
            print("[+] 获取url数量：%d"%(len(img_url_list)))
            # 返回page_url 下的所有img_url
            return img_url_list
        except:
            print("[-] 请求失败 可能网络故障")
            return False
    # 获取img_value (图片二进制)
    def get_img_value(self,img_url):
        print("[*] 正在请求url：%s"%(img_url))
        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'
            }
        # 添加headers
        request = urllib.request.Request(url=img_url,headers=headers)
        # 获取页面源码
        try:
            resp = urllib.request.urlopen(request,timeout=10)
            print("[+] 请求成功")
            # print("[]")
            # print(resp.read())
            print("[+] url：%s"%(img_url))
            print("[*] 正在保存：%s"%(img_url[-18:]))
            return resp.read()
        except:
            print("[-] 请求失败")
            return False

    # 创建路径
    def crea_folder(self,path):
        # 去除首尾空格
        path = path.strip()
        # 去除尾部\符号
        path = path.rstrip("\\")
        # 判断路径是否存在
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            print("[+] 路径：%s Create Success"%(path))
            # 切换到创建的路径
            # os.chdir(path)
            return True
        else:
            print("[+] 路径：%s 存在"%(path))
            # os.chdir(path)
            return False
    # 保存图片二进制为文件
    def save_img(self,img_name,img_value):
        try:
            with open(img_name,'wb+') as f:
                f.write(img_value)
                print("[+] 保存成功")
                f.close()
        except:
            print("[-] 保存失败")
            return False
        
