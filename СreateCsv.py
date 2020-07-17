import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

SERCEHRS = {'Google': 'http://google.com', "Yandex": "http://yandex.ru"}

class Search():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.titles = []
        self.descriptions = []
        self.searcher = ""
        self.tonals = []
        self.sample = []
        self.myFile = open('sample.csv', 'w', encoding='utf-8')
        self.wrinte = csv.writer(self.myFile)

    def setSearcher(self, name):
        self.searcher = name

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
            self.titles = driver.find_elements_by_xpath("//div[@class = 'r']/a/h3")
            self.descriptions = driver.find_elements_by_xpath("//div[@class = 's']/div/span[@class = 'st']")
        elif(SERCEHRS[self.searcher] == "http://yandex.ru"):
            self.titles = driver.find_elements_by_class_name('organic__url-text')
            self.descriptions = driver.find_elements_by_class_name('organic__content-wrapper')
        else:
            return

        self.titles = [x.text for x in self.titles]
        self.descriptions = [x.text for x in self.descriptions]
        for i in range(len(self.titles)):
            self.tonals.append(1-i/100)
        self.genSample()

    def genSample(self):
        temp = []
        for i in range(len(self.titles)):
            temp.append(self.titles[i])
            temp.append(self.descriptions[i])
            temp.append(self.tonals[i])
            for i in range(len(temp)):
                if temp[i] == '':
                    temp[i] = '0'
                else:
                    temp[i] = str(temp[i])
            self.wrinte.writerow(temp)
            temp.clear()



    def quit(self):
        self.driver.quit()
        self.myFile.close()

    def genCsv(self):
        myFile = open('sample.csv', 'w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(self.sample)
        print("Writing complete")


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
    for samp in s.sample:
        print(samp)
    s.quit()