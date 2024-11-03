import multiprocessing
from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            file.readline()
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

time_start = datetime.now()

for file in filenames:
    read_info(file)

time_stop = datetime.now()
time_res = time_stop - time_start
print(time_res)

time_start2 = datetime.now()

if __name__ == '__main__':


    process1 = multiprocessing.Process(target=read_info, args='file 1.txt')
    process1.start()

time_stop2 = datetime.now()
time_res2 = time_stop2 - time_start2
print(time_res2)