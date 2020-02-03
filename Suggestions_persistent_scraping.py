import urllib.request
import sqlite3
from bs4 import BeautifulSoup

# Your code works flawlessly. Great job! I just had to change "Dr Phil" to some other name ("Shakira" on line 53) to
# get the result. It looks like the content on the page got updated recently, so Dr Phil is not listed there anymore.
# The results get returned with the new line in the comment at line 58 below.

class Scraper:
    def __init__(self, site):
        self.site = site
        self.links = set()

    def get_links(self, number_of_pages):
        for i in range(1, number_of_pages):
            r = urllib.request.urlopen(self.site + str(i))
            soup = BeautifulSoup(r.read(), "html.parser")
            for a in soup.find_all('a', href=True):
                link = a['href']
                if '-net-worth/' in link:
                    self.links.add(link)

    def scrape_networth(self, number_of_pages):
        self.get_links(number_of_pages)
        conn = sqlite3.connect("my.db")
        # Consider making all SQL keywords capitalized for consistency. May also want to make this just one line.
        # For example:
        # conn.execute('CREATE TABLE IF NOT EXISTS celebs (name text, networth text)')
        conn.execute('''CREATE TABLE if not exists celebs               
                                     (name text, networth text)''')
        for link in self.links:
            r = urllib.request.urlopen(link)
            soup = BeautifulSoup(r.read(), "html.parser")
            try:
                # Consider removing the parentheses from the beginning and end of the expression below for greater
                # readability.
                data = (soup.findAll("div", {"class": "title"})[0].text, soup.findAll("div", {"class": "value"})[0].text)
                conn.execute("INSERT INTO celebs VALUES (?,?);", data)
                conn.commit()
            except IndexError:
                pass
        conn.close()

    def find_net_worth(self,name):
        conn = sqlite3.connect("my.db")
        cur = conn.cursor()
        who = '%' + name + '%'
        cur.execute("SELECT * FROM celebs WHERE name LIKE :who", {"who": who})
        print(cur.fetchone())
        conn.close()


scrape = Scraper('https://www.celebritynetworth.com/category/richest-celebrities/page/')
scrape.scrape_networth(2)
scrape.find_net_worth('Dr Phil')
# It looks like "Dr Phil" has been removed from this page, as mentioned.  The results are returned though with some
# other celebrity name that is at the page, for example "Shakira" works with the line below.
# scrape.find_net_worth('Shakira')
