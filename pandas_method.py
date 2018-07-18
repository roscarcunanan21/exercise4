#!/user/bin/python3
import pandas as pd
import time

send_list = "send-list.csv"
block_list = "block-list.csv"
filtered_list = "filtered-list-panda.csv"

start_time = time.time()
print("double csv filtering using python pandas method")
print("start time is {}".format(start_time))
# Notes:
# - the `subset=None` means that every column is used 
#    to determine if two rows are different; to change that specify
#    the columns as an array
# - the `inplace=True` means that the data structure is changed and
#   the duplicate rows are gone  

# Write the results to a different file

# 1 get the send_list data into memory
df_send_list = pd.read_csv(send_list, sep=",", engine='python')
step1_time = time.time();
print("Done extracting dataframe from send list in {} seconds".format(step1_time - start_time))

# 2 get the block_list data into memory
df_block_list = pd.read_csv(block_list, sep=",", engine='python')
step2_time = time.time();
print("Done extracting dataframe from block list in {} seconds".format(step2_time - step1_time))

# 3 merge and remove same values on the 2 dataframes
df_filtered_list = pd.merge(df_send_list, df_block_list[['fax']], on='fax', how='left', indicator=True).query("_merge == 'left_only'").drop('_merge',1)
step3_time = time.time();
print("Done removing block list entries from send list in {} seconds".format(step3_time - step2_time))

# 4 remove duplicates if any
df_filtered_list.drop_duplicates(subset=None, inplace=True)
# df_filtered_list.sort('fax')
step4_time = time.time();
print("Done removing duplicates in combine list in {} seconds".format(step4_time - step3_time))

# 5 save to csv
df_filtered_list.to_csv(filtered_list, mode='w', index=False, header=True)
step5_time = time.time();
print("Done writing to csv in {} seconds".format(step5_time - step4_time))

elapsed_time = time.time() - start_time
print("Total execution time: {} seconds".format(elapsed_time))
