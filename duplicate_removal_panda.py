#!/user/bin/python3
import pandas as pd
import time

source_list = "filtered-list-csv.csv"
filtered_list = "filtered-list-csv-clean.csv"

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
df_source_list = pd.read_csv(source_list, sep=",", engine='python')
step1_time = time.time();
print("Done extracting dataframe from source list in {} seconds".format(step1_time - start_time))

# 2 remove duplicates if any
df_source_list.drop_duplicates(subset=None, inplace=True)
# df_filtered_list.sort('fax')
step2_time = time.time();
print("Done removing duplicates in source list in {} seconds".format(step2_time - step1_time))

# 3 save to csv
df_source_list.to_csv(filtered_list, mode='w', index=False, header=True)
step3_time = time.time();
print("Done writing to csv in {} seconds".format(step3_time - step2_time))

elapsed_time = time.time() - start_time
print("Total execution time: {} seconds".format(elapsed_time))
