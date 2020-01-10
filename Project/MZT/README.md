#### 关于
功能：爬取www.meizitu.com 整站图片
有多线程版本

#### 使用环境

python3.6+


windows10 下正常运行
![第一步]("http://qiniu.tencentwl.cn/[windows]第一步.png")
ubuntu18.04 下正常运行


#### 注意事项
>1 . 保持网络畅通 会影响爬取速度
>2 . 路径格式  如：/home/yangfan/图片/MZT/
>3 . 注意从第一步依次执行
>4 . 可同时执行三操作（必须依次执行）

#### 操作说明
main.py（无多线程）(供研究用)
第一步：
python3 main.py save_page_url
> 获取页面缩略图url

第二步：
python3 main.py save_img_url
> 获取页面缩略图里的图片rul

第三步：
python3 main.py save_img_jpg -p [路径]
> 获取图片内容并且保存到文件夹 需要指定路径


main_thread.py (多线程)
> 注意：不指定线程数 默认为25  
第一步：
python3 main.py save_page_url -t [线程数]
> 获取页面缩略图url

第二步：
python3 main.py save_img_url -t [线程数]
> 获取页面缩略图里的图片rul

第三步：
python3 main.py save_img_jpg -p [路径] -t [线程数]
> 获取图片内容并且保存到文件夹 需要指定路径
