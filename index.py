import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self,
                 site: str):
        self.site = site

    def scrape(self):
        """Get the html content and scrape it"""
        r = urllib.request.urlopen(self.site)
        html = r.read()
        sp = BeautifulSoup(html,
                           "html.parser")

        for tag in sp.find_all("a"):
            url = tag.get('href')
            if url is None:
                continue
            # look for external links
            if "articles" in url:
                pass
                # print({'name': tag.getText()})
                # print("\n" + url)


news = "https://news.google.com"
Scraper(news).scrape()
