import os
import cv2

filename = 'train/newleft/train'
path = os.path.abspath(filename)
directory = os.listdir(path)
text_file = open("my_train.txt", "w")

for fold in directory:
	addr = os.listdir(path + '/' + fold)
	for address in addr:
		abs_addr = path + '/' + fold + '/' + address
		image = cv2.imread(abs_addr,1)
		val_abs_addr = str(abs_addr).replace("newleft", "result")
		temp = (str(abs_addr) + ' ' + str(val_abs_addr) + '\n')
		print(image.shape)
		if image.shape == (360,480,3):
			text_file.write(temp)
text_file.close()
