import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import sortingUI





def scrapeData(url):
    service = Service(executable_path='D:\Study\Semester03\DSA\Week4\Driver\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    data = sortingUI.ScrapedUrlData()

    try:
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")

        tags_to_scrape = ['div', 'span', 'p', 'li', 'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'img', 'ul', 'ol', 'li',
                          'table', 'tr', 'td', 'th']

        for tag in tags_to_scrape:
            data.html_tags[tag] = [element.text.strip() for element in soup.findAll(tag)]

        max_length = max(len(arr) for arr in data.html_tags.values())

        for tag in tags_to_scrape:
            while len(data.html_tags[tag]) < max_length:
                data.html_tags[tag].append("---")

    finally:
        driver.quit()

    return data

def writeDataToCSV(data, filename):
    df = pd.DataFrame(data.html_tags)
    df.to_csv(filename, index=False)


def loadCSVToData(filename):

    df = pd.read_csv(filename)
    data = Data()
    for column in df.columns:
        data.html_tags[column] = df[column].tolist()
    return data

def displayData(data):
    for tag, content in data.html_tags.items():
        print(f"{tag}: {content}")



if __name__ == "__main__":
    check = True
    url ="https://9animetv.to/home"
    loaded_data = loadCSVToData('urlScraped.csv')
    displayData(loaded_data)


