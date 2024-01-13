from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import re
import os


def get_start_index():
    if os.path.exists('start.txt'):
        f = open('start.txt', mode='r')
        data = f.read()
        return int(data)
    else:
        return 0


def data_extracted(count):
    f = open('collected.txt', mode='a')
    f.writelines(f'Data has been collected on Page number: {count} ' + '\n')


def print_start_index(count):
    f = open('start.txt', mode='w')
    data = str(count+1)
    f.write(data)


def fail_to_write(count):
    f = open('Not_found.txt', mode='a')
    f.writelines(f'The data is not available on page number: {count}' + '\n')
    # Beep sound

def web_scraping(count):
    service = Service(executable_path='C:\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    driver = webdriver.Chrome(service=service, options=options)
    #    lists
    votes = []
    answers = []
    views = []
    titles = []
    summarys = []
    users = []
    reputations = []
    timestamps = []


    try:
        print(f'Current page number is {count}')
        url = f"https://math.stackexchange.com/questions?tab=newest&page={count}&pagesize=50"
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")

        count1 = 0
        for a in soup.findAll('div', attrs={'data-post-type-id': "1"}):
            det = "No detail available"
            count1 += 1
            vote = a.find('div', class_='s-post-summary--stats-item__emphasized')
            answer = a.find_all('div', attrs={"class": 's-post-summary--stats-item'})[1]
            view = a.find_all('div', attrs={'class': 's-post-summary--stats-item'})[2]
            title = a.find('h3', attrs={'class': 's-post-summary--content-title'}).a
            summary = a.find('div', attrs={'class': 's-post-summary--content-excerpt'})
            user = a.find('a', attrs={'class': 'flex--item'})
            reputation = a.find('span', attrs={'title': "reputation score "})
            timestamp = a.find('time', attrs={'class': 's-user-card--time'})
            if reputation:
                reputations.append(reputation.text)
            else:
                reputations.append(det)
            if timestamp:
                match = re.search(r'asked (.+)', timestamp.text.strip())
                data = match.group(1)
                timestamps.append(data)
            else:
                timestamps.append(det)
            if user:
                users.append(user.text)
            else:
                users.append(det)
            if summary:
                s = summary.text.strip()
                summarys.append(s)
            else:
                summarys.append(det)
            if title:
                titles.append(title.text)
            else:
                titles.append(det)
            if vote:
                votes.append(vote.span.text)
            else:
                votes.append(det)
            if answer:
                answers.append(answer.span.text)
            else:
                answers.append(det)
            if view:
                views.append(view.span.text)
            else:
                views.append(det)
        if os.path.exists('test_data.csv'):
            df = pd.DataFrame(
                {'Title': titles, 'No. of answers': answers, 'No. of views': views, 'No. of votes': votes,
                 'Users': users,
                 'Reputation': reputations, 'Time_stamp': timestamps, 'Summary': summarys})
            df.to_csv('test_data.csv', mode='a', header=False, index=False, encoding='utf-8')
        else:
            df = pd.DataFrame(
                {'Title': titles, 'No. of answers': answers, 'No. of views': views, 'No. of votes': votes,
                 'Users': users,
                 'Reputation': reputations, 'Time_stamp': timestamps, 'Summary': summarys})
            df.to_csv('test_data.csv', mode='a', header=True, index=False, encoding='utf-8')
        print(f"Total data extracted: {count1} ")
        data_extracted(count)
        print_start_index(count)
    except:
        fail_to_write(count)
        print(f'May be error occur on Page number; {count}')


if __name__ == '__main__':
    start = get_start_index()
    for x in range(start, 32185):
        web_scraping(x)
