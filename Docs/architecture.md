### Central Architecture🌞：

![](https://picreso.oss-cn-beijing.aliyuncs.com/basis.png)

#### AirSpider has 6 modules and 3 sub-modules：

#### 6 main modules：

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

#### 3 sub-modules：

##### 三个中间件：

+ Spider MiddleWare： 负责对解析模块进行额外处理
+ Downloader MiddleWare： 负责下载模块的反爬虫策略处理
+ NLP MiddleWare：负责NLP模块的策略处理

### Distributed Architecture☁️：

![](https://picreso.oss-cn-beijing.aliyuncs.com/cloud.png)


### Redis acts as a Master, distributes tasks, and deduplicates tasks. Each AirSpider acts as a Slaver, and works as follows



## WorkFlow🌊：

![](https://picreso.oss-cn-beijing.aliyuncs.com/flow.png)

1. **Spiders specify the initial URL and encapsulate it as a Request**

2. **Core receives the Request and forwards it to the Scheduler**

3. **Scheduler receives the Request and sends it to Redis**

4. **Redis receives the Request and forwards it to the Scheduler**

5. **Scheduler receives the Request and forwards it to the Core**

6. **Core receives the Request and forwards it to Downloader**

7. **The Downloader crawls the request to the specified URL, and the returned data is encapsulated into a Response**

8. **Core receives the Response and forwards it to Spiders**

9. **Spiders parses the content in the Response to obtain the specified content, encapsulates it into Items and forwards it to Piplines, and encapsulates the URLs that meet the requirements into Requests and sends it to the Core**

10. **Core receives Requests and forwards them to Scheduler**

11. **Scheduler forwards Requests to Redis**

12. **Redis performs deduplication processing and distributes task request to Core**

13. **Core receives the Request and forwards it to Downloader**

    **Then repeat to step 7**

    **Until all the tasks of Redis are crawled**

14. **Persistent processing of data in Piplines**