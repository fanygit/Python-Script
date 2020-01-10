from mzimg import Mzimg
import argparse
# 创建对象
mzimg = Mzimg()
# 保存page_url 到文件
def save_page_url():
    # sava_page_url
    # 构造每页url
    for i in range(1,93):
        url = "https://www.meizitu.com/a/list_1_"+str(i)+".html"
       # print(url)
        list2  = mzimg.get_page_url(url)
        # 判断是否请求失败
        if list2 is not False:
            # 打开文件
            # 注意事项：如果重复执行此方法 会不断在page_url_list.txt 上追加 
            # 避免url重复叠加 应执行为后立即删除page_url_list.txt 文件
            f = open('page_url_list.txt','a')
            # 写入每条page_url
            for url in list2:
                f.write(url+'\r\n')
            # 关闭文件
            f.close()

def save_img_url():
    # 调试get_img_url方法
    # page_url = "https://www.meizitu.com/a/5122.html"
    # 打开 page_url 文件
    with open('page_url_list.txt') as f:
        for page_url in f:
            page_url = page_url.strip('\r').strip('\n')
            # 请求get_img_url 方法 返回Page_url(缩略图) 的img_url(内容)
            img_url_list = mzimg.get_img_url(page_url)
            # 判断是否请求失败
            if img_url_list is not False:
                # 打开文件
                f = open('img_url_list.txt','a')
                # 写入每条img_url
                for url in img_url_list:
                    f.write(url+'\r\n') 
                # 关闭文件
                f.close()

def save_img_jpg(path):
    # 存放目录
    # path = '/home/yangfan/Code/Python/_urllib/demo_mz/MZT/'
    # 调用crea_folder 创建文件夹
    mzimg.crea_folder(path)
    # 调试get_img方法
    with open('img_url_list.txt') as f:
        for img_url in f:
            img_url = img_url.strip('\r').strip('\n')
            img_name = img_url[-18:].replace('/','_')
            # print(img_name)
            img_name = path + img_name
            # 调用get_img 以二进制形式返回 
            img_value = mzimg.get_img_value(img_url)
            # 调用save_img 保存
            if img_value is not False:
                mzimg.save_img(img_name,img_value)

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('name',help="save_page_url：获取页面缩略图所有url.\n save_img_url：获取页面缩略图里的图片所有url. \n save_img_jpg：保存所有图片为文件,需要指定路径.")
    parser.add_argument('-p','--path',dest="path",help="设置图片存放路径")
    
    args = parser.parse_args()
    return args

def main():
    try:
        # 创建解析
        args = parse()
        if args.name == 'save_page_url':
            save_page_url()

        elif args.name == 'save_img_url':
            save_img_url()

        elif args.name == 'save_img_jpg':
            if args.path: 
                save_img_jpg(args.path)
            else:
                print("[-] 未设置路径")
                exit()
    except:
        print("[-] 输入-h 查看详细信息")
        exit()
                     
            
            

if __name__=='__main__':
    main()
