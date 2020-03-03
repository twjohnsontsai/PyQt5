
from bs4 import BeautifulSoup

johnson= ('<!DOCTYPE html>\n'
          '<html lang="en">\n'
          '<head>\n'
          '    <meta charset="UTF-8">\n'
          '    <title>味源生技有限公司</title>\n'
          '</head>\n'
          '<body>\n'
          '<h1>这时候就是输入文本的时候了，注意，要先打上"<"再上">"</h1>\n'
          '<h1>这是另外的一段话，需要注明这不是同一行</h1>\n'
          '<h2>你好，用tag来做网络爬虫</h2>\n'
          '<p>这就是网页的内容了，可以学习的网站网址</p>\n'
          '</body>\n'
          '</html>')

soup=BeautifulSoup(johnson,'html.parser')
# BeautifulSoup解析(.parser)johnson这个网页，并赋予这个为一个变量soup
myh1=soup.find('h1')
# 用.fing只能找一个h1
myh1=soup.findAll('h1')
print(myh1)
for i in myh1:
    # 要逐一打印出来
    print(i)
    # 要逐一打印并去掉<>
    print(i.string)
    if '注意' in i.string:
        # 打印出带'注意'的行
        print(i.string)
myh1=soup.find('h2')
print(myh1)
print(myh1.string)
