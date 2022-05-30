import os
import shutil

filePath = r'E:\code\gitCode\wlj\code\Auto\app\guitai_output_0524'
listFilesName = os.listdir(filePath)
print(len(listFilesName))
for name in listFilesName:
    a = name.split('.')
    print(type(len(a[0])))
    s = a[0]
    if int(s) < 500:
        fileSrc = os.path.join(filePath, name)
        fileDst = os.path.join(r'E:\code\gitCode\wlj\code\Auto\app\other', name)
        shutil.copy(fileSrc, fileDst)
    print(name)
