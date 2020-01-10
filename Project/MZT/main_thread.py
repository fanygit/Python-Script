from mzimg import Mzimg
import argparse
import threading,queue
#-----------------------------------------多线程--------------------------------------#
#-------------------------------------------------------------------------------------#
# sava_page_url 多线程
class save_page_thread(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url
    def run(self):
        while not self.url.empty():
            url = self.url.get()
            save_page_url(url)

# save_img_url 多线程
class save_img_thread(threading.Thread):
    def __init__(self,page_url):
        threading.Thread.__init__(self)
        self.page_url = page_url
    def run(self):
        while not self.page_url.empty():
            url = self.page_url.get()
            save_img_url(url)

# save_img_jpg 多线程
class save_img_jpg_thread(threading.Thread):
    def __init__(self,path,img_url):
        threading.Thread.__init__(self)
        self.path = path
        self.img_url = img_url
    def run(self):
        while not self.img_url.empty():
            img_url = self.img_url.get()
            save_img_jpg(self.path,img_url)

#-----------------------------------功能----------------------------------------------#
#-------------------------------------------------------------------------------------#

# 创建对象
mzimg = Mzimg()
# 保获取到的存page_url 链接 到文件
def save_page_url(url):
    # 请求get_page_url方法 返回每页的url集
    list2  = mzimg.get_page_url(url)
    # 判断是否请求失败
    if list2 is not False:
        # 打开文件
        # 注意事项：如果重复执行此方法 会不断在page_url_list.txt 上追加 
        # 避免url重复叠加 应执行为后立即删除page_url_list.txt 文件
        f = open('page_url_list.txt','a')
        # 写入每条page_url
        for url in list2:
            f.write(url+'\r')
        # 关闭文件
        f.close()
# 保存获取到的img_url链接 到文件 
def save_img_url(page_url):
    # 请求get_img_url 方法 返回Page_url(缩略图) 的img_url(内容)
    img_url_list = mzimg.get_img_url(page_url)
    # 判断是否请求失败
    if img_url_list is not False:
        # 打开文件
        f = open('img_url_list.txt','a')
        # 写入每条img_url
        for url in img_url_list:
            f.write(url+'\r') 
        # 关闭文件
        f.close()
# 通过img_url 保存为图片
def save_img_jpg(path,img_url):
    #print(img_url)
    #img_url = img_url.get()
    img_name = img_url[-18:].replace('/','_')
    # print(img_name)
    img_name = path + img_name
    # 调用get_img 以二进制形式返回 
    img_value = mzimg.get_img_value(img_url)
    # 调用save_img 保存
    if img_value is not False:
        mzimg.save_img(img_name,img_value)
#---------------------------------------队列---------------------------------------------#
#----------------------------------------------------------------------------------------#
# 获取url队列
def get_url():
    q_url = queue.Queue()
    # 构造每页url队列形式返回
    for i in range(1,93):
        url = "https://www.meizitu.com/a/list_1_"+str(i)+".html"
        q_url.put(url)
       # print(url)
    return q_url

# 获取page_url队列
def get_page_url():
    q_page_url = queue.Queue()
    # 打开 page_url 文件
    with open('page_url_list.txt') as f:
        for page_url in f:
            page_url = page_url.strip('\r').strip('\n')
            q_page_url.put(page_url)
    return q_page_url

# 获取img_url队列
def get_img_url():
    q_img_url = queue.Queue()
    with open('img_url_list.txt') as f:
        for img_url in f:
            img_url = img_url.strip('\r').strip('\n')
            q_img_url.put(img_url)
    return q_img_url

#----------------------------------------配置---------------------------------------------#
#-----------------------------------------------------------------------------------------#
# 命令行解析
def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('name',help=" save_page_url：获取页面缩略图所有url.\n     save_img_url：获取页面缩略图里的图片所有url. \n save_img_jpg：保存所有图片为文件,需要指定路径.")
    parser.add_argument('-t','--thread',dest='thread',default=25,type=int,help="设置线程 默认为：25")
    parser.add_argument('-p','--path',dest="path",help="指定图片存放路径")     
    args = parser.parse_args()
    return args
# 个人信息
def info():
    print("-------------------------------------------")
    print("- ******* -------- * ---------- **      * -")
    print("- *        ------ * * --------- * *     * -")
    print("- *       ------ *   * -------- *  *    * -")
    print("- ******* ----- ******* ------- *   *   * -")
    print("- *       ---- *       * ------ *    *  * -")
    print("- *       --- *         * ----- *     * * -")
    print("- *       -- *           * ---- *      ** -")
    print("-------------------------------------------")
    print("-作者：YangFan")
    print("-GitHub：https://github.com/fanygit")
    print("-E-Mail：483813121@qq.com")



def main():
    args = parse()
    name_list = ['save_page_url','save_img_url','save_img_jpg']
    if args.name not in name_list:
        print("[-] 参数有误 检查后输入 -h：更多信息")
        exit()
    try:
        thread_count = args.thread 
        if args.name == 'save_page_url':
            # 获取url队列
            url = get_url()
            # 线程队列
            save_page_threads = []
            # sava_page_url
            # save_page_url(url)
            print("[*] 线程数：%s"%(thread_count))
            for i in range(thread_count):
                thread = save_page_thread(url)
                thread.start()
                save_page_threads.append(thread)

            for t in save_page_threads:
                t.join()
            info()
    except:
        print("[-] 输入-h 查看详细信息")
        exit()

    try:
        if args.name == 'save_img_url':
            # 获取page_url队列
            page_url = get_page_url()
            # 线程队列
            save_img_threads = []
            # 创建线程
            for i in range(thread_count):
                thread = save_img_thread(page_url)
                thread.start()
                save_img_threads.append(thread)

            for t in save_img_threads:
                t.join()
            info()
    except:
        print("[-] 输入-h 查看详细信息")
    
    try:
        if args.name == 'save_img_jpg':
            if args.path:
                # 存放目录
                path = args.path
                # 调用crea_folder 创建文件夹
                mzimg.crea_folder(path)
                # 获取img_url 队列
                q_img_url = get_img_url()
                # 线程列表
                save_img_jpg_threads = []
               # 创建线程
                for i in range(50):
                    thread = save_img_jpg_thread(path,q_img_url)
                    thread.start()
                    save_img_jpg_threads.append(thread) 

                for t in save_img_jpg_threads:
                    t.join()
                info()
            else:
                print("[-] 未设置路径")
                exit()
    except:
        print("[-] 输入-h 查看详细信息")
        exit()
    
         

if __name__=='__main__':
    main()
