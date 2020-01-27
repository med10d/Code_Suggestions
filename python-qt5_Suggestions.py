import bs4 as bs
import sys
import csv
import urllib.request  # import not used.
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from lxml.html import fromstring
# import time    # This import can be used in junction with line 21 below, to show that the page has not completed loading yet.

class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        # time.sleep(2)   # This import can be used in junction with 9 above, to show that the page has not completed loading yet.
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str): # method names should be lowercase, "callable".
        self.html = html_str
        self.app.quit()


class main():
    def __init__(self):
        self.data = []

    def scrape_data(self):
        print('Loading...')
        page = Page('https://www.udemy.com')
        soup = bs.BeautifulSoup(page.html, 'html.parser')
        course = soup.findAll(class_='merchandising-course-card--course-title--2Ob4m')
        author = soup.findAll(class_='merchandising-course-card--instructor-titles--vXVfV')
        crs = []
        auth = []
        for tag in course:
            crs.append(tag.text)
        print(crs)
        for tag in author:
            auth.append(tag.text)
        print(auth)
        self.data = zip(crs, auth)
        start.save_to_file()

    def save_to_file(self):
        with open("Courses.csv", "w") as f:
            w = csv.writer(f, delimiter=",")
            for item in self.data:
                w.writerow(item)
        print('Saved to file: Courses.csv')


start = main()
start.scrape_data()