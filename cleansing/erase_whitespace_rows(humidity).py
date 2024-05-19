# 출처: https://stackoverflow.com/a/43529502
# 출처: https://stackoverflow.com/a/5618893

import os

def last_comma_attach_quote(line):
    split_list = line.split(",")
    split_list[5] = "\"" + split_list[5]
    split_list[-1] = split_list[-1] + "\"\n"

    new_line = ','.join(split_list)

    return new_line

base_directory = '../source-data/climate/example-data/humidity'
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
            new_line_list = []
            for line in line_list:
                line = line.replace("\"\"", "")
                line = line.strip()
                if line:
                    line = last_comma_attach_quote(line)
                    new_line_list.append(line)
            
            ofile.writelines(new_line_list)
