
from bs4 import BeautifulSoup
import requests

baidu=requests.get('https://www.baidu.com')
print(baidu)
# 向网址请求，反馈值为<Response [200]>就代表已经通过了
baidu=requests.get('https://www.baidu.com').content
print(baidu)
# 这时打印出来的数据很混乱就是网站的原始编码，如果要更清晰就需要透过BeautifulSoup来解析内容

soup=BeautifulSoup(baidu,'html.parser')
# 设置一个变量，并且用BeautifulSoup来解析parser它（badu)html
print(soup.text)
# 打印出变量soup的文字部分

links=soup.findAll('a')
print(links)
for i in links:
    # 设置一个回路，让link逐一列出来
    print(i)
    print(i.string)
    # 打印不带链接的文字