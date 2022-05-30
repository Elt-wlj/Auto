import os
import shutil

filePath = r'E:\code\gitCode\wlj\code\Auto\app\guitai_output_0524'
listFilesName = os.listdir(filePath)
max_num = 200
file_times = 1
time = 1

# print(listFilesName)
for name in listFilesName:
    a = name.split('.')
    # print(type(len(a[0])))
    s = a[0]
    if time > max_num:
        time = 1
        file_times += 1
    folder = r'E:\code\gitCode\wlj\code\Auto\app\other\{}'.format(file_times)
    if not os.path.exists(folder):
        os.mkdir(folder)
    fileSrc = os.path.join(filePath, name)
    fileDst = os.path.join(folder, name)
    print(time, fileSrc, fileDst)
    shutil.copy(fileSrc, fileDst)
    time += 1
    print(name)
