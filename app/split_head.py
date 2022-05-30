import os
import shutil

fs = os.listdir("heads1")

total = int(len(fs) / 2)
max_num = int(total / 20)
print(total, max_num)
fnum = 0
cnt = 0
for f in range(total):
	if f % 1000 == 0:
		print(f)
	tmp_path = "split_head_"+str(fnum)
	if cnt == 0:
		print("move to new folder...", tmp_path)
		shutil.rmtree(tmp_path, ignore_errors=True)
		os.makedirs(tmp_path, exist_ok=True)

	shutil.copyfile("heads1/" + str(f) + ".jpg", tmp_path + "/" + str(f) + ".jpg")
	shutil.copyfile("heads1/" + str(f) + ".xml", tmp_path + "/" + str(f) + ".xml")
		
	cnt+=1
	if cnt == max_num:
		cnt = 0
		fnum += 1 
	
	
