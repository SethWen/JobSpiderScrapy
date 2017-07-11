# JobSpiderScrapy

该项目包含以下三部分：

* 爬虫: 负责拉钩和智联职位信息的数据抓取，解析，存库
* 服务端：服务端，负责为客户端提供数据接口，详情请参见 JobSpiderDjango 仓库
* 移动端：负责在 Android 端展示爬取到的数据， 详情请参见 JobSpiderAndroid 仓库

该仓库是项目基于 Scrapy 框架的爬虫源码。包括两个爬虫，分别爬取了拉钩和智联的职位信息：

1. 拉钩的职位信息是通过 Ajax 动态加载，该项目通过爬取并解析其返回的 json，将数据存储在MySQL
2. 智联的职位信息则是静态网页，爬取到 html 后， 通过 xpath 解析，将数据存储在 MySQL
