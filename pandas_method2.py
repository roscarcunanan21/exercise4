#!/user/bin/python3
import pandas as pd
import time
import csv

send_list = "send-list.csv"
block_list = "block-list.csv"
pre_filtered_list = "pre-filtered-list-panda2.csv"
filtered_list = "filtered-list-panda2.csv"

start_time = time.time()
print("double csv filtering using python pandas method 2")
print("start time is {}".format(start_time))
# Notes:
# - the `subset=None` means that every column is used 
#    to determine if two rows are different; to change that specify
#    the columns as an array
# - the `inplace=True` means that the data structure is changed and
#   the duplicate rows are gone  

# Write the results to a different file

# 1 get the send_list data into memoryimport pandas as pd
send_list_data_set=set(pd.read_csv(send_list, index_col=False, header=None)[0]) #reads the csv, takes only the first column and creates a set out of it.
block_list_data_set=set(pd.read_csv(block_list, index_col=False, header=None)[0]) #same here
step1_time = time.time();
print("Done extracting casting the csv files to sets in {} seconds".format(step1_time - start_time))
unique_set = send_list_data_set-block_list_data_set #set A - set B gives back everything thats only in A.
step2_time = time.time();
print("Done getting the difference between sets in {} seconds".format(step2_time - step1_time))

# 4. write output to new csv
text_file = open(pre_filtered_list, "w")
text_file.write("fax\n")
for item in unique_set:
  text_file.write("%s\n" % item)
text_file.close()
step3_time = time.time();
print("Done writing to csv in {} seconds".format(step3_time - step2_time))

# 1 get the send_list data into memory
df_filtered_list = pd.read_csv(pre_filtered_list, sep=",", engine='python')
df_filtered_list.drop_duplicates(subset=None, inplace=True)
# df_filtered_list.sort('fax')
df_filtered_list.to_csv(filtered_list, mode='w', index=False, header=True)
step4_time = time.time();
print("Done removing duplicates in {} seconds".format(step4_time - step3_time))

elapsed_time = time.time() - start_time
print("Total execution time: {} seconds".format(elapsed_time))
