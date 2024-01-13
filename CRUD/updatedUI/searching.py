def StartsWith(Arr, string, listt):
    """Arr is 1D array according to which search is to occur, array2D is complete list"""
    length = len(str(string))

    feed_back = [[], [], [], [], [], [], [], []]

    for i in range(0, len(Arr)):
        if Arr[i][0:length] == string:
            ind = i
            feed_back[0].append(listt[0][ind])
            feed_back[1].append(listt[1][ind])
            feed_back[2].append(listt[2][ind])
            feed_back[3].append(listt[3][ind])
            feed_back[4].append(listt[4][ind])
            feed_back[5].append(listt[5][ind])
            feed_back[6].append(listt[6][ind])
            feed_back[7].append(listt[7][ind])
    # print(feedBack)
    # print(feed_back)
    return feed_back


def EndsWith(Arr, string, listt):
    """Arr[index] as input"""
    length = len(str(string))

    # print(Arr)
    feed_back = [[], [], [], [], [], [], [], []]

    for i in range(0, len(Arr)):
        print(Arr[i][len(Arr[i]) - length:] + ' is comparing with ' + string)
        if string in Arr[i][len(Arr[i]) - length:]:
            ind = i
            feed_back[0].append(listt[0][ind])
            feed_back[1].append(listt[1][ind])
            feed_back[2].append(listt[2][ind])
            feed_back[3].append(listt[3][ind])
            feed_back[4].append(listt[4][ind])
            feed_back[5].append(listt[5][ind])
            feed_back[6].append(listt[6][ind])
            feed_back[7].append(listt[7][ind])
    return feed_back


def Contains(Arr, string, listt):
    """Arr[index] as input 1D Array, listt is 2D array"""
    length = len(string)

    feed_back = [[], [], [], [], [], [], [], []]

    for i in range(0, len(Arr)):
        for j in range(0, len(Arr[i])):
            if Arr[j: j + length] == string:
                print(Arr[j: j + length])
                ind = i
                feed_back[0].append(listt[0][ind])
                feed_back[1].append(listt[1][ind])
                feed_back[2].append(listt[2][ind])
                feed_back[3].append(listt[3][ind])
                feed_back[4].append(listt[4][ind])
                feed_back[5].append(listt[5][ind])
                feed_back[6].append(listt[6][ind])
                feed_back[7].append(listt[7][ind])
                break
    return feed_back


def And(Arr, string, Arr2d):
    return Contains(Arr, string, Arr2d)


def Not(Arr, string, listt):
    """Arr[index] as input"""
    length = len(string)

    feed_back = [[], [], [], [], [], [], [], []]

    for i in range(0, len(Arr)):
        check = False
        for j in range(0, len(Arr[i])):
            if Arr[i][j: j + length] == string:
                check = True
                break
        if check == False:
            ind = i
            feed_back[0].append(listt[0][ind])
            feed_back[1].append(listt[1][ind])
            feed_back[2].append(listt[2][ind])
            feed_back[3].append(listt[3][ind])
            feed_back[4].append(listt[4][ind])
            feed_back[5].append(listt[5][ind])
            feed_back[6].append(listt[6][ind])
            feed_back[7].append(listt[7][ind])
    return feed_back


def linearSearchStrings(arr, pattern, idx):
    """Linear Search Algorithm for strings"""
    feedBack = []
    for item in arr:
        if pattern in item[idx]:
            feedBack.append(item)

    return feedBack


def linearSearch(arr, Number, idx):
    """Linear Search Algorithm for Integers"""
    feedBack = []
    for item in arr:
        if item[idx] == Number:
            feedBack.append(item)

    return feedBack
