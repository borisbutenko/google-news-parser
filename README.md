# google-news-parser
My first scraper used django.
Scraping only external and not empty ex ```<a href="^http">text</a>``` links.
Python 3 req.

## install and commands

``` bash
# install requirements
./install.sh

# activate venv
./venv.sh

# runserver
./manage.py runserve

# deactivate venv
./venv.sh deactivate
```

### run app
http://127.0.0.1:8000/news/ for scraping <news.google.com> as default
http://127.0.0.1:8000/news/site for scraping <site>

Example:
http://127.0.0.1:8000/news/yandex.ru for scraping <yandex.ru>
