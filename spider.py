#! python3
import requests
from bs4 import BeautifulSoup
import jieba
from wordcloud import WordCloud

url='https://comment.bilibili.com/3216790.xml'

#设置一些弹幕高频出现但是非常见的词
jieba.add_word("种花家")
jieba.add_word("小男孩")
jieba.add_word("追梦赤子心")
jieba.add_word("哭了")
jieba.add_word("鸡你太美")
jieba.add_word("此生无悔入华夏")

r=requests.get(url)
r.encoding=r.apparent_encoding
data=r.text
soup = BeautifulSoup(data,"html.parser")
f=open("弹幕.txt",'w',encoding='utf-8')
word_split=''
for i in soup.find_all('d'):
    f.write(i.text+'\n')
    word=' '.join(jieba.cut(i.text,cut_all=False))  #分词得到的结果
    word_split = ' '.join([word_split, word])
f.close()

wordcloud = WordCloud(font_path="C:\\Windows\\Fonts\\STXINGKA.TTF",
                      background_color="white",
                      width=1920, height=1080,
                      font_step=5,
                      random_state= 30,
                      min_font_size=15,max_font_size=200,
                      stopwords=['不是','我们','前面','这个','应该','不要','其实','那么']).generate(word_split)
wordcloud.to_file('pic.png')


