import urllib.request

from bs4 import BeautifulSoup
from django.shortcuts import render


# Create your views here.
class Scraper:
    def __init__(self,
                 site: str):
        self.site = site

    def scrape(self) -> list:
        """Get the html content and scrape it"""
        urls = []
        r = urllib.request.urlopen(self.site)
        html = r.read()
        sp = BeautifulSoup(html,
                           "html.parser")

        for tag in sp.find_all("a"):
            name = tag.getText()
            url = tag.get('href')

            if not url or not name:
                continue

            # look for external links
            if "articles" in url:
                urls.append({'href': self.site + url,
                             'name': name})

        return urls


def index(req,
          site: str = 'news.google.com'):
    site = "https://" + site
    context = {'urls': Scraper(site).scrape(),
               'site': site}
    return render(req,
                  'news/index.html',
                  context)
