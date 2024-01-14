import main
import copy


def swap(datas, i, j):
    datas.title[i], datas.title[j] = datas.title[j], datas.title[i]
    datas.answers[i], datas.answers[j] = datas.answers[j], datas.answers[i]
    datas.views[i], datas.views[j] = datas.views[j], datas.views[i]
    datas.votes[i], datas.votes[j] = datas.votes[j], datas.votes[i]
    datas.reputation[i], datas.reputation[j] = datas.reputation[j], datas.reputation[i]
    datas.time_stamp[i], datas.time_stamp[j] = datas.time_stamp[j], datas.time_stamp[i]
    datas.summary[i], datas.summary[j] = datas.summary[j], datas.summary[i]
    datas.users[i], datas.users[j] = datas.users[j], datas.users[i]


def asc_Bubble_Sort(data, col):
    datas = copy.deepcopy(data)
    req = getattr(data, col)
    n = len(req)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if req[j] > req[j + 1]:
                swap(datas, j, j+1)
                swapped = True
        if not swapped:
            break
    return datas


def asc_selection_sort(datas, col):
    data = copy.copy(datas)
    req = getattr(data, col)
    n = len(req)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if req[j] < req[min_index]:
                min_index = j
        swap(data, i, min_index)
    return data



