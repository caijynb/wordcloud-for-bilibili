用于爬取B站弹幕并制作词云图

代码以那年那兔的第一集为例

（解决完依赖）可立即使用，适用任何B站视频

代码根据对应的视频需要修改的地方共3处：

1.

```
url='https://comment.bilibili.com/3216790.xml'
```

这里url的3216780改成想要爬取的B站视频cid号



2.

```
#设置一些弹幕高频出现但是非常见的词
jieba.add_word("种花家")
jieba.add_word("小男孩")
jieba.add_word("追梦赤子心")
jieba.add_word("哭了")
jieba.add_word("鸡你太美")
jieba.add_word("此生无悔入华夏")
```

根据弹幕内容自行替换高频出现但是非常见的词



3.

```
stopwords=['不是','我们','前面','这个','应该','不要','其实','那么']
```

stopwords处无意义不想加入词云图的词也根据需要自行替换

