## 微信图灵聊天机器人
之前看到过有用几行python代码实现微信聊天机器人的帖子，但是发现过于简陋，并且bug还很多（比如无法区分个人消息和群消息）。于是就自己研究了一下，利用网上开源的wxbot微信聊天机器人再自己加上图灵机器人的api，做成了一个实用的微信图灵聊天机器人。

需要准备的：

* 图灵机器人接口api。这个可以去[www.truing123.com](www.truing123.com)注册，然后可以获得一个api接口地址和key，凭借这两个东西可以访问图灵机器人的服务器并获得返回数据
* wxbot。是一个开源的Python包装Web微信协议实现的微信机器人框架，可以去GitHub：[https://github.com/liuwons/wxBot](https://github.com/liuwons/wxBot)上下载

图灵机器人服务器的操作流程：
通过urllib2库的request命令将自己输入的文本发送至图灵机器人的api接口（需要配合key），然后使用response命令得到返回的json形式的数据，取出其中有用的部分，放入需要回复的字段中。

