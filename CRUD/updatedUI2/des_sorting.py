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


def dsc_Bubble_Sort(data, col):
    datas = copy.deepcopy(data)
    req = getattr(data, col)
    n = len(req)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if req[j] < req[j + 1]:
                swap(datas, j, j+1)
                swapped = True
        if not swapped:
            break
    return datas


def dsc_selection_sort(datas, col):
    data = copy.copy(datas)
    req = getattr(data, col)
    n = len(req)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if req[j] > req[min_index]:
                min_index = j
        swap(data, i, min_index)
    return data


def dsc_insertion_sort(datas, col):
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
        while j >= 0 and key > req[j]:
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


def dsc_comb_sort(datas, col):
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
            if req[i] < req[i + gap]:
                swap(data, i, i+gap)
                swapped = True
    return data


def heapify(data, n, i, col):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and col[left] < col[largest]:
        largest = left

    if right < n and col[right] < col[largest]:
        largest = right

    if largest != i:
        swap(data, i, largest)
        heapify(data, n, largest, col)


def dsc_heap_sort(datas, col):
    data = copy.copy(datas)
    req = getattr(data, col)
    n = len(req)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, req)

    for i in range(n - 1, 0, -1):
        swap(data, 0, i)
        heapify(data, i, 0, req)
    return data


def dsc_bucket_sort_data(datas, col):
    data = copy.copy(datas)
    req = getattr(data, col)
    min_val = min(req)
    max_val = max(req)
    bucket_range = (max_val - min_val) / (len(req) - 1)

    num_buckets = len(req)
    buckets = [[] for _ in range(num_buckets)]

    for i in range(len(req)):
        index = int((req[i] - min_val) / bucket_range)
        buckets[index].append(i)

    sorted_data = main.data()

    for bucket in reversed(buckets):
        for i in reversed(bucket):
            sorted_data.title.append(data.title[i])
            sorted_data.answers.append(data.answers[i])
            sorted_data.views.append(data.views[i])
            sorted_data.votes.append(data.votes[i])
            sorted_data.reputation.append(data.reputation[i])
            sorted_data.time_stamp.append(data.time_stamp[i])
            sorted_data.summary.append(data.summary[i])
            sorted_data.users.append(data.users[i])

    return sorted_data


def dsc_counting_sort(data, col):
    req = getattr(data, col)
    max_val = max(req)
    count = [0] * (max_val + 1)

    for val in req:
        count[val] += 1
    cumulative_sum = [0] * (max_val + 1)
    cumulative_sum[0] = count[0]
    for i in range(1, max_val + 1):
        cumulative_sum[i] = cumulative_sum[i - 1] + count[i]

    sorted_data = main.data()
    value_lists = {i: [] for i in range(max_val + 1)}

    for i, val in enumerate(req):
        value_lists[val].append(i)

    for i in range(max_val, -1, -1):
        for j in value_lists[i]:
            sorted_data.title.append(data.title[j])
            sorted_data.answers.append(data.answers[j])
            sorted_data.views.append(data.views[j])
            sorted_data.votes.append(data.votes[j])
            sorted_data.reputation.append(data.reputation[j])
            sorted_data.time_stamp.append(data.time_stamp[j])
            sorted_data.summary.append(data.summary[j])
            sorted_data.users.append(data.users[j])
    return sorted_data


def counting_sort_desc(data, col, digit, base):
    req = getattr(data, col)
    max_val = max(req)

    count = [0] * base

    # Count the occurrences of each digit
    for val in req:
        digit_value = (val // (base ** digit)) % base
        count[digit_value] += 1

    # Update count to store the last index for each digit in reverse order
    for i in range(base - 2, -1, -1):
        count[i] += count[i + 1]

    # Create an output array
    output = [None] * len(req)

    # Build the output array using count information in reverse order
    for i in range(len(req) - 1, -1, -1):
        digit_value = (req[i] // (base ** digit)) % base
        output[count[digit_value] - 1] = i
        count[digit_value] -= 1

    # Populate the sorted data using the output array in reverse order
    sorted_data = main.data()
    sorted_data.title = [data.title[i] for i in output]
    sorted_data.answers = [data.answers[i] for i in output]
    sorted_data.views = [data.views[i] for i in output]
    sorted_data.votes = [data.votes[i] for i in output]
    sorted_data.reputation = [data.reputation[i] for i in output]
    sorted_data.time_stamp = [data.time_stamp[i] for i in output]
    sorted_data.summary = [data.summary[i] for i in output]
    sorted_data.users = [data.users[i] for i in output]

    return sorted_data

def desc_radix_sort(data, col, base=10):
    max_val = max(getattr(data, col))
    num_digits = (len(str(max_val)) + 1) // 2  # In base 100, two-digit numbers

    sorted_data = main.data()
    sorted_data.title = [None] * len(data.title)
    sorted_data.answers = [None] * len(data.answers)
    sorted_data.views = [None] * len(data.views)
    sorted_data.votes = [None] * len(data.votes)
    sorted_data.reputation = [None] * len(data.reputation)
    sorted_data.time_stamp = [None] * len(data.time_stamp)
    sorted_data.summary = [None] * len(data.summary)
    sorted_data.users = [None] * len(data.users)

    for digit in range(num_digits):
        sorted_data = counting_sort_desc(data, col, digit, base)

    return sorted_data


def partition(data, col, low, high):
    req = getattr(data, col)
    pivot = req[high]
    i = low - 1

    for j in range(low, high):
        if req[j] > pivot:
            i += 1
            swap(data, i, j)

    swap(data, i + 1, high)
    return i + 1


def quick_sort(data, col, low, high):
    if low < high:
        pivot_index = partition(data, col, low, high)
        quick_sort(data, col, low, pivot_index - 1)
        quick_sort(data, col, pivot_index + 1, high)


def dsc_quick_sort(data, col):
    datas = copy.deepcopy(data)
    n = len(getattr(datas, col))
    quick_sort(datas, col, 0, n - 1)
    return datas

def Merge(data, col, p, q, r):
    req = getattr(data, col)
    left_array = req[p:q+1]
    left_array_t = data.title[p:q+1]
    left_array_an = data.answers[p:q+1]
    left_array_vi = data.views[p:q+1]
    left_array_vo = data.votes[p:q+1]
    left_array_re = data.reputation[p:q+1]
    left_array_ts = data.time_stamp[p:q+1]
    left_array_su = data.summary[p:q+1]
    left_array_use = data.users[p:q+1]
    Right_array = req[q+1:r+1]
    Right_array_t = data.title[q+1: r+1]
    Right_array_an = data.answers[q+1: r+1]
    Right_array_vi = data.views[q+1: r+1]
    Right_array_vo = data.votes[q+1: r+1]
    Right_array_re = data.reputation[q+1: r+1]
    Right_array_ts = data.time_stamp[q+1: r+1]
    Right_array_su = data.summary[q+1: r+1]
    Right_array_us = data.users[q+1: r+1]

    i, j = 0, 0
    k = p
    while i < len(left_array) and j < len(Right_array):
        if left_array[i] > Right_array[j]:
            req[k] = left_array[i]
            data.title[k] = left_array_t[i]
            data.answers[k] = left_array_an[i]
            data.views[k] = left_array_vi[i]
            data.votes[k] = left_array_vo[i]
            data.reputation[k] = left_array_re[i]
            data.time_stamp[k] = left_array_ts[i]
            data.summary[k] = left_array_su[i]
            data.users[k] = left_array_use[i]
            i += 1
        else:
            req[k] = Right_array[j]
            data.title[k] = Right_array_t[j]
            data.answers[k] = Right_array_an[j]
            data.views[k] = Right_array_vi[j]
            data.votes[k] = Right_array_vo[j]
            data.reputation[k] = Right_array_re[j]
            data.time_stamp[k] = Right_array_ts[j]
            data.summary[k] = Right_array_su[j]
            data.users[k] = Right_array_us[j]
            j += 1
        k += 1
    while i < len(left_array):
        req[k] = left_array[i]
        data.title[k] = left_array_t[i]
        data.answers[k] = left_array_an[i]
        data.views[k] = left_array_vi[i]
        data.votes[k] = left_array_vo[i]
        data.reputation[k] = left_array_re[i]
        data.time_stamp[k] = left_array_ts[i]
        data.summary[k] = left_array_su[i]
        data.users[k] = left_array_use[i]
        i += 1
        k += 1
    while j < len(Right_array):
        req[k] = Right_array[j]
        data.title[k] = Right_array_t[j]
        data.answers[k] = Right_array_an[j]
        data.views[k] = Right_array_vi[j]
        data.votes[k] = Right_array_vo[j]
        data.reputation[k] = Right_array_re[j]
        data.time_stamp[k] = Right_array_ts[j]
        data.summary[k] = Right_array_su[j]
        data.users[k] = Right_array_us[j]
        j += 1
        k += 1


def Merge_Sort(data, col, p, q):
    if p < q:
        midpoint = (p+q) // 2
        Merge_Sort(data, col, p, midpoint)
        Merge_Sort(data, col, midpoint+1, q)
        Merge(data, col, p, midpoint, q)


def dsc_merge_sort(datas, col):
    data = copy.copy(datas)
    n = len(getattr(data, col))
    Merge_Sort(data, col, 0, n-1)
    return data


def dsc_shell_sort(datas, col):
    data = copy.deepcopy(datas)
    req = getattr(data, col)
    n = len(req)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = req[i]
            temp1 = data.title[i]
            temp2 = data.answers[i]
            temp3 = data.views[i]
            temp4 = data.votes[i]
            temp5 = data.reputation[i]
            temp6 = data.time_stamp[i]
            temp7 = data.summary[i]
            temp8 = data.users[i]
            j = i
            while j >= gap and req[j - gap] < temp:
                req[j] = req[j - gap]
                data.title[j] = data.title[j-gap]
                data.answers[j] = data.answers[j-gap]
                data.views[j] = data.views[j-gap]
                data.votes[j] = data.votes[j-gap]
                data.reputation[j] = data.reputation[j-gap]
                data.time_stamp[j] = data.time_stamp[j-gap]
                data.summary[j] = data.summary[j-gap]
                data.users[j] = data.users[j-gap]
                j -= gap
            req[j] = temp
            data.title[j] = temp1
            data.answers[j] = temp2
            data.views[j] = temp3
            data.votes[j] = temp4
            data.reputation[j] = temp5
            data.time_stamp[j] = temp6
            data.summary[j] = temp7
            data.users[j] = temp8
        gap //= 2

    return data
