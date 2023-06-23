import requests
from bs4 import BeautifulSoup

import exceptions


class Crawler:
    """Handles tasks that involve web scraping"""

    def __init__(self):
        self.HEADERS = {'accept': '*/*',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
                        'Accept-Language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
                        'referer': 'https://www.google.com/',
                        'cookie': 'DSID=AAO-7r4OSkS76zbHUkiOpnI0kk-X19BLDFF53G8gbnd21VZV2iehu-w_2v14cxvRvrkd_NjIdBWX7wUiQ66f-D8kOkTKD1BhLVlqrFAaqDP3LodRK2I0NfrObmhV9HsedGE7-mQeJpwJifSxdchqf524IMh9piBflGqP0Lg0_xjGmLKEQ0F4Na6THgC06VhtUG5infEdqMQ9otlJENe3PmOQTC_UeTH5DnENYwWC8KXs-M4fWmDADmG414V0_X0TfjrYu01nDH2Dcf3TIOFbRDb993g8nOCswLMi92LwjoqhYnFdf1jzgK0'
                        }

    
    def crawl(self, url, div_class):
        """returns list of dict with title & link, of specific news in specific url"""

        return self.__getNewsInBase(self.__getBase(self.__getRequest(url), div_class), url)


    def __getRequest(self, url):
        """sends a GET request to url"""

        try:
            request = requests.get(url, headers=self.HEADERS)
            request.raise_for_status()
            return request
                
        except Exception as e:
            raise exceptions.HttpError
    

    def __getBase(self, request, div_class):
        """returns list (base) containing relevant data from request.content, using identifier div_class"""

        return BeautifulSoup(request.content, "html.parser").find_all("div", class_= div_class)

    
    def __getNewsInBase(self, base, url):
        """returns list containing dict with title & link for each news article in base"""
            
        return [{"title": n.find("p").text, "link": url +"/"+ n.find("a")["href"]} for n in base]
        