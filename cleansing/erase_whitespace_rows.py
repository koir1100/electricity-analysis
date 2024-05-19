# 출처: https://stackoverflow.com/a/43529502

import os

base_directory = '/Users/DragonPC/Desktop/project_2nd/climate/temperature'
# base_directory = '/Users/DragonPC/Desktop/project_2nd/climate/rainfall'
# Change this to your CSV file base directory

for dir_path, dir_name_list, file_name_list in os.walk(base_directory):
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
