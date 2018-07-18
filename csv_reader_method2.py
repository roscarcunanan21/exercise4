#!/user/bin/python3
import time
import csv
import mmap

send_list = "send-list.csv"
block_list = "block-list.csv"
filtered_list = "filtered-list-csv2.csv"

start_time = time.time()
print("double csv filtering using csv method2 method")
print("start time is {}".format(start_time))

# Write the results to a different file

# 1 read each csv file separately to memory
with open(block_list, 'r') as list_b, open(send_list, 'r') as list_s:
    file_block = list_b.readlines()
    file_send = list_s.readlines()

with open(filtered_list, 'w') as outFile:
    for line in file_send:
        if line not in file_block:
            outFile.write(line)
		
outFile.close()  

elapsed_time = time.time() - start_time
print("Total execution time: {} seconds".format(elapsed_time))