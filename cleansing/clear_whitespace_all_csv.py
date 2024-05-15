# 출처: https://sidorl.tistory.com/48
# 출처: https://redcarrot.tistory.com/222
# 출처: https://stackoverflow.com/a/57394274
# 출처: https://stackoverflow.com/a/4521533
import glob
import csv

weather_element = ['wind']
#weather_element = ['humidity', 'rainfall', 'temperature']

for element in weather_element:
    path = '/Users/DragonPC/Desktop/project_2nd/climate/' + element + '/'
    merge_path = '/Users/DragonPC/Desktop/project_2nd/climate/' + element + '/merge_total_' + element + '.csv'

    file_list = sorted(glob.glob(path + '*'))
    with open(merge_path, 'w', encoding='cp949') as f1:
        write = csv.writer(f1, delimiter=',')

        for i, file in enumerate(file_list):
            if i == 0:
                with open(file, 'r', encoding='cp949') as f2:
                    reader = csv.reader(f2, delimiter=',', quoting=csv.QUOTE_MINIMAL)

                    for line in reader:
                        trim = (field.strip() for field in line)
                        write.writerow(trim)

                file_name = file.split('\\')[-1]
                # print(file.split('\\')[-1] + ' write complete...')

            else:
                with open(file, 'r', encoding='cp949') as f2:
                    n = 0
                    
                    reader = csv.reader(f2, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                    for line in reader:
                        if n != 0:
                            trim = (field.strip() for field in line)
                            write.writerow(trim)
                        if not line:
                            break
                        n += 1

                file_name = file.split('\\')[-1]
                # print(file.split('\\')[-1] + ' write complete...')
