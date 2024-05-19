# 출처: https://stackoverflow.com/a/43529502
# 출처: https://stackoverflow.com/a/5618893
# 출처: https://stackoverflow.com/a/46057350

import os
import re

def wrap_multi_data_with_mark(line):
    line = line.replace(" ", "")
    target = re.findall(r'[^0-9,][가-힣,(가-힣)\[가-힣\]]{1,}[^0-9,]', line)
    if target:
        dict_target = {}
        
        # 각 데이터를 딕셔너리에 추가하고, 쌍따옴표로 묶음
        for i, element in enumerate(target):
            dict_target[str(i)] = '"' + element + '"'
            line = line.replace(element, "@@@{}".format(str(i)), 1)

        # 딕셔너리 값을 데이터에 대체하여 쌍따옴표로 묶음
        for idx, val in dict_target.items():
            line = line.replace('@@@{}'.format(idx), '{}', 1).format(val)

    # 콤마로 구분된 데이터를 추출하여 결과에 추가
    split_list = line.split(",")
    split_list[-1] = split_list[-1] + "\n"

    new_line = ','.join(split_list)
    return new_line

base_directory = '../source-data/climate/example-data/wind/'
# Change this to your CSV file base directory

for dir_path, dir_name_list, file_name_list in os.walk(base_directory):
    for file_name in sorted(file_name_list):
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
                line = line.replace("\"", "")
                line = line.strip()
                if line:
                    line = wrap_multi_data_with_mark(line)
                    new_line_list.append(line)
            
            new_line_list[-1] = new_line_list[-1].replace("\n","")
            ofile.writelines(new_line_list)
