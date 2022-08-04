import time

def most_common_item(my_list):
    '''
    Return the item that occurs the most frequently in my_list.
    '''
    mci = None #most common item
    mcc = None #most common count
    for item in my_list:
        count = 0
        for item2 in my_list:
            if item2 == item:
                count += 1
        if mcc is None or count > mcc:
            mci = item
            mcc = count
    return mci

# Test Cases list
my_list = [1, 2, 3, 3, 4, 2, 2, 1, 3, 2]
start_time = time.time()
result = most_common_item(my_list)
end_time = time.time()
total_time = end_time - start_time
print("Input:", my_list)
print("Output:", most_common_item(my_list))
print("Time", total_time)

# Test Cases dictonary
my_list = {1, 2, 3, 3, 4, 2, 2, 1, 3, 2}
start_time = time.time()
result = most_common_item(my_list)
end_time = time.time()
total_time = end_time - start_time
print("\nInput:", my_list)
print("Output:", most_common_item(my_list))
print("Time", total_time)