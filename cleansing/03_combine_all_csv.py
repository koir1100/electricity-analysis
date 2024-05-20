# 출처: https://sidorl.tistory.com/48
# 출처: https://redcarrot.tistory.com/222
# 출처: https://stackoverflow.com/a/40416154
# 출처: https://stackoverflow.com/a/64033961
from pathlib import Path
import glob

climate_elements = ['wind']

for element in climate_elements:
    relative_path = Path(__file__).parent
    
    target_path = '../source-data/climate/' + element
    path = (relative_path / target_path).resolve()
    merge_file = 'merge_' + element + '.csv'
    merge_path = (path / merge_file).resolve()

    file_list = sorted(glob.glob(str(path) + '/*'))
    with open(merge_path, 'w', encoding='cp949') as f:
        for i, file in enumerate(file_list):
            if i == 0:
                with open(file, 'r', encoding='cp949') as f2:
                    line = f2.readline()
                    if not line:
                        break

                    f.write(line)

                file_name = file.split('\\')[-1]

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
