<p align="center">
    <img src="https://picreso.oss-cn-beijing.aliyuncs.com/air.png" width="150px">
    <h1 align="center">AirSpider</h1>
    <p align="center">
        AirSpider, a distributed async web crawler framework based on redis🕷️
      <br>
     		Distributed👪 - Asynchronou🚶 - Light☁️ - Fast⚡️
      <br>
  <br>
</p>    



# Introduction

> + AirSpider是一款面向开发者的一个高性能异步爬虫框架
> + AirSpider模块之间耦合性低，内聚性高，方便扩展，并且工作流有条不紊
> + 基于Redis进行任务分发，任务去重，并且实现分布式。
> + 作为一个定制化爬虫框架，用户只需要编写指定模块，便可以开始高性能的爬虫任务
>



# Document



## Basic Architecture：

![基础架构](Docs/basis.png)

### AirSpider共有6大模块，三小模块：

### 6大模块：

1. 核心模块：Core：
   + 作为核心引擎，连接了其他几大模块，进行工作，工作流以它为中枢进行
2. 解析模块：Spider：
   + 作为解析模块，负责对Response进行解析，即对爬取回来的页面，进行指定数据的解析
3. 下载模块：Downloader
   + 作为下载模块，负责将Request，进行网络请求，返回指定URL的HTML内容
4. 管道模块：Piplines
   + 作为管道模块，负责将解析模块返回的指定数据进行封装，保存，连接数据库
5. 调度模块：Scheduler
   + 作为调度模块，负责与Redis交互，发送给Redis带下载的Request，Redis将调度好的Request返回给调度模块
6. NLP模块：NLP processor
   + 作为附加的模块，主要是对下游数据进行分析，挖掘

### 3小模块：

#### 三个中间件：

+ Spider MiddleWare： 负责对解析模块进行额外处理
+ Downloader MiddleWare： 负责下载模块的反爬虫策略处理
+ NLP MiddleWare：负责NLP模块的策略处理

## Distributed Architecture：
![分布式架构](Docs/cloud.png)


### Redis作为Master，进行任务的分发，任务去重，各个AirSpider作为Slaver，分别工作如下



## WorkFlow：
![基础架构](Docs/flow.png)

1. Spiders将初始URL指定，封装成Request

2. Core接受到Request，转发给Scheduler

3. Scheduler接收到Request，发给Redis

4. Redis收到Request，转发给Scheduler

5. Scheduler收到Request转发给Core

6. Core接收到Request，转发给Downloader

7. Downloader将Request进行网络爬取指定URL，返回数据封装成Response

8. Core接受到Response，转发给Spiders

9. Spiders将Response里的内容进行解析获取指定内容，封装成Items转发给Piplines 并且将里面符合规定的URLs，封装成Requests，发给Core

10. Core接受到Requests转发给Scheduler

11. Scheduler将Requests转发给Redis

12. Redis进行去重处理，分发任务Request 发给Core

13. Core接收到Request转发给Downloader

    然后重复到第7步

    一直到Redis所有任务都爬取完

14. 对Piplines里面的数据进行持久化处理

# Announcement

开发预期在三个月内完成大体 功能