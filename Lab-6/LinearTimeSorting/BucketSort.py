import time
def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        value = bucket[i]
        j = i - 1
        while j >= 0 and value < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = value

def bucket_sort(array):
   
    TotalBuckets = len(array)   # totalbuckets equal to len of the input array

    # maKINg the buckets according to the TOtal number of buckets
    buckets = [[] for _ in range(TotalBuckets)]

    
    for num in array:
        index = int(num * TotalBuckets)
        buckets[index].append(num)

    
    for i in range(TotalBuckets):
        insertion_sort(buckets[i])

    
    finalArray = []
    for bucket in buckets:
        finalArray.extend(bucket)

    return finalArray


##################  Taking INput from here

array = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
start = time.time()
finalArray = bucket_sort(array)
end = time.time()
TotalTime = end - start
print(f"Bucket Sort took {TotalTime} seconds")
print("The sorted array by Bucket sort is : ",finalArray)
