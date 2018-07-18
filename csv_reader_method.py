#!/user/bin/python3
import time
import csv
import mmap

send_list = "send-list.csv"
block_list = "block-list.csv"
filtered_list = "filtered-list-csv.csv"

start_time = time.time()
print("double csv filtering using csv method1 method")
print("start time is {}".format(start_time))

# 1 read each csv file separately to memory
fs = open(send_list, 'r')
reader_s = csv.reader(fs)
step1_time = time.time();
print("Done getting csv data from send list in {} seconds".format(step1_time - start_time))

ff = open(filtered_list, 'a') # python will convert \n to os.linesep
ff.write("fax\n")

block_list_source = open(block_list).read()
for row_s in reader_s:
	if row_s[0] not in block_list_source:
		ff.write(row_s[0] + "\n") 
		
ff.close()  

elapsed_time = time.time() - start_time
print("Total execution time: {} seconds".format(elapsed_time))