#-*-coding:utf8-*-
from urllib import parse
from urllib import request
import re
import sys
from imp import reload 
def downLoadPage(fileName, url):
    print("正在下载%s" % fileName)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    request1 = request.Request(url, headers=headers)
    html_content = request.urlopen(request1).read()
    t = re.compile('class="j_th_tit ">(.*?)</a>|class="pull-right is_show_create_time.*?>(.*?)</span>')
    picture_url_list1 = t.findall(html_content.decode('utf-8',"ignore"))
    a = '\n\n'.join(map(str,picture_url_list1))
    #r = re.compile('class="j_th_tit ">(.*?)</a>')
    #picture_url_list2 = r.findall(html_content.decode('utf-8'))
    #b = '\n\n'.join(picture_url_list2)
    f_write = open(fileName, "w",encoding = 'utf-8')
    try:
        f_write.write(a)
        #f_write.write('\n')
        #f_write.write(b)
    except Exception as ex:
        print("%s" % ex)
    finally:
        f_write.close()

if __name__ == "__main__":
    kw = input("贴吧名字:")
    beginPage = int(input("起始页:"))
    endPage = int(input("结束页:"))
    url = "http://tieba.baidu.com/f?"
    url = url + parse.urlencode({"kw": kw})
    for page in range(beginPage, endPage +1):
        fileName = kw + "吧---第" + str(page) + "页.txt"
        pn = (page - 1) * 50
        t_url = url + "&pn=" + str(pn)
        print(t_url)
        downLoadPage(fileName, t_url)