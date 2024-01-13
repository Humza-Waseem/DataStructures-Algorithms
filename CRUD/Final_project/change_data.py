import pandas as pd
import main
import re

def converted_date(data):
    converted = []
    qer = 2023
    for x in data:
        pattern = r'\d{4}'
        val = re.findall(pattern, x)
        if len(val) != 0:
            val = int(val[0])
        if not val:
            val = qer
        converted.append(val)
    return converted


def converted_rep(data):
    for x in range(len(data)):
        if data[x] == 'No detail available':
            data[x] = 0
    return data


def revert_rep(data):
    for x in range(len(data)):
        if data[x] == 0:
            data[x] = 'No detail available'
    return data


def loaddata():
    df = pd.read_csv("1.csv")
    datas = main.data()
    datas.title = df['Title'].values.tolist()
    datas.answers = df['No. of answers'].values.tolist()
    datas.views = df['No. of views'].values.tolist()
    datas.votes = df['No. of votes'].values.tolist()
    datas.users = df['Users'].values.tolist()
    datas.reputation = df['Reputation'].values.tolist()
    datas.time_stamp = df['Time_stamp'].values.tolist()
    datas.summary = df['Summary'].values.tolist()
    return datas


def converted(data):
    converted1 = []
    for x in data:
        numeric = None
        if 'k' in x:
            numeric = int(x.replace('k', ''))*1000
        else:
            numeric = int(x)
        converted1.append(numeric)
    return converted1


if __name__ == '__main__':
    datas = loaddata()
    # numeric = converted(data.views)
    datas.time_stamp = converted_date(datas.time_stamp)

    df = pd.DataFrame(
        {'Title': datas.title, 'No. of answers': datas.answers, 'No. of views': datas.views,
         'No. of votes': datas.votes,
         'Users': datas.users,
         'Reputation': datas.reputation, 'Time_stamp': datas.time_stamp, 'Summary': datas.summary})
    df.to_csv('1.csv', mode='w', header=True, index=False, encoding='utf-8')