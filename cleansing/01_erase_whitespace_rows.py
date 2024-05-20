# 출처: https://stackoverflow.com/a/43529502

import os

relative_directory = '../source-data/climate/example-data/temperature' # rainfall도 line_list[7:] 로 동일
# relative_directory = '../source-data/climate/example-data/wind' # line_list[14:]
# relative_directory = '../source-data/climate/example-data/humidity' # line_list[15:]
# Change this to your CSV file base directory

current_directory = os.path.dirname(__file__)
base_directory = os.path.join(current_directory, relative_directory)

for dir_path, _, file_name_list in os.walk(base_directory):
    for file_name in file_name_list:
        # If this is not a CSV file
        if not file_name.endswith('.csv'):
            # Skip it
            continue
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'r', encoding='cp949') as ifile:
            line_list = ifile.readlines()
        with open(file_path, 'w', encoding='cp949') as ofile:
            ofile.writelines(line_list[14:])
