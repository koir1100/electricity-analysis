# 출처: https://sidorl.tistory.com/48
# 출처: https://redcarrot.tistory.com/222
import glob

climate_elements = ['humidity', 'rainfall', 'temperature']

for element in climate_elements:
    path = '../source-data/climate/2002-2011/' + element + '/'
    merge_path = path + 'merge_' + element + '.csv'

    file_list = sorted(glob.glob(path + '*'))
    with open(merge_path, 'w', encoding='cp949') as f:
        for i, file in enumerate(file_list):
            if i == 0:
                with open(file, 'r', encoding='cp949') as f2:
                    line = f2.readline()
                    if not line:
                        break

                    f.write(line)

                file_name = file.split('\\')[-1]
                # print(file.split('\\')[-1] + ' write complete...')

            else:
                with open(file, 'r', encoding='cp949') as f2:
                    n = 0
                    while True:
                        line = f2.readline()
                        if n != 0:
                            f.write(line)

                        if not line:
                            break
                        n += 1

                file_name = file.split('\\')[-1]
                # print(file.split('\\')[-1] + ' write complete...')
