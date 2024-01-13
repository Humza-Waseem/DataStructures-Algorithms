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


def asc_insertion_sort(datas, col):
    data = copy.copy(datas)
    req = getattr(data, col)

    for i in range(1, len(req)):
        key = req[i]
        j = i - 1
        key1 = data.title[i]
        key2 = data.users[i]
        key3 = data.answers[i]
        key4 = data.votes[i]
        key5 = data.time_stamp[i]
        key6 = data.views[i]
        key7 = data.reputation[i]
        key8 = data.summary[i]
        while j >= 0 and key < req[j]:
            req[j + 1] = req[j]
            data.title[j + 1] = data.title[j]
            data.users[j + 1] = data.users[j]
            data.answers[j + 1] = data.answers[j]
            data.votes[j + 1] = data.votes[j]
            data.time_stamp[j + 1] = data.time_stamp[j]
            data.views[j + 1] = data.views[j]
            data.reputation[j + 1] = data.reputation[j]
            data.summary[j + 1] = data.summary[j]
            j -= 1
        req[j + 1] = key
        data.title[j + 1] = key1
        data.users[j + 1] = key2
        data.answers[j + 1] = key3
        data.votes[j + 1] = key4
        data.time_stamp[j + 1] = key5
        data.views[j + 1] = key6
        data.reputation[j + 1] = key7
        data.summary[j + 1] = key8
    return data


#

def asc_quick_sort(data, col, p, r):
    if p < r:
        q = Partition(data, col, p, r)
        asc_quick_sort(data, col, p, q-1)
        asc_quick_sort(data, col, q+1, r)


def Partition(data, col, p, r):
    x = col[r]
    i = p - 1
    for j in range(p, r):
        if col[j] <= x:
            i = i + 1
            swap(data, i, j)
    swap(data, i + 1, r)
    return i + 1


def asc_comb_sort(datas, col):
    data = copy.copy(datas)
    req = getattr(data, col)
    gap = len(req)
    shrink = 1.3  # Typical shrink factor
    swapped = True
    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1
        swapped = False
        for i in range(len(req) - gap):
            if req[i] > req[i + gap]:
                swap(data, i, i+gap)
                swapped = True
    return data
