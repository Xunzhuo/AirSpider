import grequests
import lxml
from bs4 import BeautifulSoup
import logging
import selenium

class dyttSpider(object):
    start_URL = 'https://www.dy2018.com/'
    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/80.0.3987.149 Safari/537.36'}

    # URL去重和URL判断是否爬取过：采用的方式是比较基础的set，后面要采用BoomFilter代替此方法
    URL_PARSED = set()
    URL_UNPARSED = set()

    # 初始化
    def __init__(self):
        self.URL_UNPARSED.add(self.start_URL)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(filename)s : %(funcName)s  %(message)s')

    # 下载器模块 雏形 采用协程 异步IO
    def downloader(self, request):
        request = [grequests.get(request, headers=self.headers)]
        response = grequests.map(request)
        res = response[0].text
        return res

    # spider模块 雏形
    def spider(self, response):
        soup = BeautifulSoup(response, 'lxml')
        URL_list = soup.find_all('a')
        URLs = []
        Items = {}
        for url in URL_list:
            print("Found " + url.get_text() + ' ' + self.start_URL + url.get('href'))
            res = self.start_URL + url.get('href')
            if 'magnet' in res:
                pass
            else:
                URLs.append(res)
        print(str(len(URL_list)) + ' in total')
        return URLs, Items

    # 调度器模块 雏形
    # Add函数来把新的URL去重加入到Set中
    def scheduler_Add(self, url):
        if url not in self.URL_PARSED:
            self.URL_UNPARSED.add(url)
            logging.info("URL: %s added successfully" % url)
        else:
            logging.info("URL: %s has been parsed" % url)

    # Dispatcher函数 用来分发任务
    def scheduler_Dispatcher(self):
        if len(self.URL_UNPARSED) == 0:
            logging.info("Parsing work is finished ")
            return 'end'
        for i in self.URL_UNPARSED:
            self.URL_PARSED.add(i)
            self.URL_UNPARSED.discard(i)
            logging.info("URL: %s is on parsing" % i)
            return i

    # NLP模块雏形
    def NLP_engine(self, piplines):
        pass

    # 管道雏形
    # 把items加入到Piplines中
    def piplines_add(self, items):
        pass

    # 把piplines持久化处理
    def piplines_persistence(self):
        pass

    # 获取Piplines中的内容
    def piplines_read(self):
        pass

    # 核心模块 雏形
    def core(self):
        logging.info("\n\n"
                     "        /$$$$$$  /$$                  /$$$$$$            /$$       /$$                            /$$$$$$   /$$                           /$$                     /$$\n"
"       /$$__  $$|__/                 /$$__  $$          |__/      | $$                           /$$__  $$ | $$                          | $$                    | $$\n"
"      | $$  \ $$ /$$  /$$$$$$       | $$  \__/  /$$$$$$  /$$  /$$$$$$$  /$$$$$$   /$$$$$$       | $$  \__//$$$$$$    /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$$\n"
"      | $$$$$$$$| $$ /$$__  $$      |  $$$$$$  /$$__  $$| $$ /$$__  $$ /$$__  $$ /$$__  $$      |  $$$$$$|_  $$_/   |____  $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$\n"
"      | $$__  $$| $$| $$  \__/       \____  $$| $$  \ $$| $$| $$  | $$| $$$$$$$$| $$  \__/       \____  $$ | $$      /$$$$$$$| $$  \__/  | $$    | $$$$$$$$| $$  | $$\n"
"      | $$  | $$| $$| $$             /$$  \ $$| $$  | $$| $$| $$  | $$| $$_____/| $$             /$$  \ $$ | $$ /$$ /$$__  $$| $$        | $$ /$$| $$_____/| $$  | $$\n"
"      | $$  | $$| $$| $$            |  $$$$$$/| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$            |  $$$$$$/ |  $$$$/|  $$$$$$$| $$        |  $$$$/|  $$$$$$$|  $$$$$$$\n"
"      |__/  |__/|__/|__/             \______/ | $$____/ |__/ \_______/ \_______/|__/             \______/   \___/   \_______/|__/         \___/   \_______/ \_______/\n"
"                                              | $$                                                                                                                   \n"
"                                              | $$                                                                                                                   \n"
"                                              |__/                                                                                                                   \n")
        logging.info("AirSpider is starting and parsing the website: %s" % self.start_URL)

        while len(self.URL_UNPARSED) != 0:
            URL = self.scheduler_Dispatcher()
            if URL == 'end':
                break
            Response = self.downloader(URL)
            URLs, Items = self.spider(Response)
            if len(URLs) != 0:
                for url in URLs:
                    self.scheduler_Add(url)
            self.piplines_add(Items)
        self.NLP_engine(self.piplines_read())
        self.piplines_persistence()


if __name__ == '__main__':
    spider = dyttSpider()
    spider.core()
