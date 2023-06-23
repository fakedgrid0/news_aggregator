import json

import Crawler
import GUI
import exceptions


class NewsAggregator():
    
    def __init__(self):
        self.NEWS_SOURCES_PATH = "/home/fakedgrid/GitHub/python-projects/news_aggregator/news_aggregator/NEWS_SOURCES.json"
        self.gui = GUI.GUI()
        self.crawler = Crawler.Crawler()
        self.news_list = []
        self.news_sources_list = self.getNewsSources()
        self.gui.setup()


    def run(self):
        self.gui.root.after(0, self.update)
        self.gui.root.mainloop()
    

    def update(self):

        old_idx = len(self.news_list)

        # for each news source, get its news
        try:
            for i in self.news_sources_list:
                [self.news_list.append(i) for i in self.get_news_list(i["url"], i["div_class"])]
            self.news_list = self.news_list[old_idx:]

        except exceptions.HttpError:
            self.news_list = self.news_list[:old_idx]

        self.gui.updateNewsList(self.news_list)

        self.gui.root.after(60000, self.update)
        

    def get_news_list(self, url, div_class):    
        return self.crawler.crawl(url, div_class)

    
    def getNewsSources(self):
        news_sources_list = []

        news_sources_json = open(self.NEWS_SOURCES_PATH) 
        news_sources_dict = json.load(news_sources_json)
        
        [news_sources_list.append(news_sources_dict[i]) for i in news_sources_dict]

        return news_sources_list