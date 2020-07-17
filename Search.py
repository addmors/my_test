from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from WorkExcel import Work
from time import sleep
from datetime import datetime

SERCEHRS = {'Google': 'http://google.com', "Yandex": "http://yandex.ru"}

class Search():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.links = []
        self.titles = []
        self.descriptions = []
        self.w = Work()
        self.searcher = ""

    def setSearcher(self, name):
        self.searcher = name
        self.w.__init__()

    def CreateData(self, search_name):
        try:
            self.driver.get(SERCEHRS[self.searcher])
        except:
            return

        driver = self.driver
        if (SERCEHRS[self.searcher] == "http://google.com"):
            input = driver.find_element_by_xpath("//input[@type='text']")
        elif (SERCEHRS[self.searcher] == "http://yandex.ru"):
            input = driver.find_element_by_xpath("//input[@id='text'][@name='text']")
        input.send_keys(search_name)
        input.send_keys(Keys.ENTER)

        sleep(1)
        if(SERCEHRS[self.searcher] == "http://google.com"):
            self.links = driver.find_elements_by_xpath("//div[@class = 'r']/a")
            self.titles = driver.find_elements_by_xpath("//div[@class = 'r']/a/h3")
            self.descriptions = driver.find_elements_by_xpath("//div[@class = 's']/div/span[@class = 'st']")
        elif(SERCEHRS[self.searcher] == "http://yandex.ru"):
            self.links = driver.find_elements_by_xpath(
                "//a[@class='link link_theme_outer path__item i-bem']")
            self.titles = driver.find_elements_by_class_name('organic__url-text')
            self.descriptions = driver.find_elements_by_class_name('organic__content-wrapper')
        else:
            return

        self.links = [x.get_attribute('href') for x in self.links]
        self.titles = [x.text for x in self.titles]
        self.descriptions = [x.text for x in self.descriptions]

        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
        driver.find_element_by_tag_name('body').\
            screenshot('screen/%s %s-%s.png'
                       % (self.searcher, search_name, datetime.today().strftime('%Y-%m-%d')))
        self.w.next_list(search_name)
        self.w.append([self.links, self.titles, self.descriptions])
        self.w.saving(self.searcher)

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    s = Search()
    s.setSearcher('Yandex')
    s.CreateData('яблоко')
    s.CreateData('абрикос')
    s.CreateData('киви')
    s.setSearcher('Google')
    s.CreateData('яблоко')
    s.CreateData('абрикос')
    s.CreateData('киви')
    s.quit()