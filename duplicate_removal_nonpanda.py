#!/user/bin/python3
import pandas as pd
import time

source_list = "filtered-list-csv.csv"
filtered_list = "filtered-list-csv-clean-nonpanda.csv"

start_time = time.time()
print("removing duplicates")
print("start time is {}".format(start_time))
# Notes:
# - the `subset=None` means that every column is used 
#    to determine if two rows are different; to change that specify
#    the columns as an array
# - the `inplace=True` means that the data structure is changed and
#   the duplicate rows are gone  

# Write the results to a different file

# 1 get the send_list data into memory
with open(source_list,'r') as in_file, open(filtered_list,'w') as out_file:
    seen = set() # set for fast O(1) amortized lookup
    for line in in_file:
        if line in seen: continue # skip duplicate

        seen.add(line)
        out_file.write(line)

elapsed_time = time.time() - start_time
print("Total execution time: {} seconds".format(elapsed_time))
