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

def most_common_item_dict(my_list):
  item_counts = {}
  for item in my_list:
      if item in item_counts: #if item is not in dictionary then it is add
          item_counts[item] += 1
      else:
          item_counts[item] = 1
        
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

# Test Cases
my_list = [1, 2, 3, 3, 4, 2, 2, 1, 3, 2]
start_time = time.time()
list_result = most_common_item(my_list)
end_time = time.time()
total_time = end_time - start_time
print("List Implementation")
print("Input:", my_list)
print("Output:", list_result)
print("Time", total_time)


start_time = time.time()
dict_result = most_common_item_dict(my_list)
end_time = time.time()
total_time = end_time - start_time

print("\nDictionary Implementation")
print("Input:", my_list)
print("Output:", dict_result)
print("Time", total_time)#Dictionary method is faster