# JobSpiderScrapy
该项目基于 Scrapy 框架，爬取了拉钩和智联的职位信息。
其中，拉钩的职位信息是通过 Ajax 动态加载，该项目通过爬取并解析其返回的 json，将数据存储在MySQL；智联的职位信息则是静态网页，爬取到 html 后， 通过 xpath 解析，将数据存储在 MySQL 中。
