用于爬取B站弹幕并制作词云图

我以那年那兔的第一集为例

```
url='https://comment.bilibili.com/3216790.xml'

#设置一些弹幕高频出现但是非常见的词
jieba.add_word("种花家")
jieba.add_word("小男孩")
jieba.add_word("追梦赤子心")
jieba.add_word("哭了")
jieba.add_word("鸡你太美")
jieba.add_word("此生无悔入华夏")
```

这里url的3216780改成想要爬取的B站视频cid号

然后根据弹幕内容自行替换掉这些高频出现但是非常见的词

