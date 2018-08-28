import os
import cv2
import numpy as np

filename = 'train/result/train'
path = os.path.abspath(filename)
directory = os.listdir(path)

for fold in directory:
	addr = os.listdir(path + '/' + fold)
	for address in addr:
		abs_addr = path + '/' + fold + '/' + address
		image = cv2.imread(abs_addr,1)
		rows = np.size(image, 0)
		cols = np.size(image, 1)
		blank_image = np.zeros((rows,cols,1), np.uint8)
		for i in range(rows):
			for j in range(cols):
				#print type(image[i,j])
				if image[i,j,0] == 10 and image[i,j,1] == 10 and image[i,j,2] == 10:
					blank_image[i,j] = 0
				elif image[i,j,0] == 255 and image[i,j,1] == 0 and image[i,j,2] == 0:
					blank_image[i,j] = 1
				elif image[i,j,0] == 0 and image[i,j,1] == 255 and image[i,j,2] == 0:
					blank_image[i,j] = 2
				elif image[i,j,0] == 100 and image[i,j,1] == 100 and image[i,j,2] == 0:
					blank_image[i,j] = 3
				elif image[i,j,0] == 255 and image[i,j,1] == 255 and image[i,j,2] == 0:
					blank_image[i,j] = 4
				elif image[i,j,0] == 0 and image[i,j,1] == 100 and image[i,j,2] == 200:
					blank_image[i,j] = 5
				elif image[i,j,0] == 0 and image[i,j,1] == 255 and image[i,j,2] == 255:
					blank_image[i,j] = 6
				elif image[i,j,0] == 255 and image[i,j,1] == 0 and image[i,j,2] == 255:
					blank_image[i,j] = 7
				elif image[i,j,0] == 0 and image[i,j,1] == 100 and image[i,j,2] == 100:
					blank_image[i,j] = 8
				elif image[i,j,0] == 0 and image[i,j,1] == 0 and image[i,j,2] == 255:
					blank_image[i,j] = 9
				elif image[i,j,0] == 0 and image[i,j,1] == 128 and image[i,j,2] == 255:
					blank_image[i,j] = 10
				elif image[i,j,0] == 200 and image[i,j,1] == 100 and image[i,j,2] == 0:
					blank_image[i,j] = 11
				elif image[i,j,0] == 100 and image[i,j,1] == 0 and image[i,j,2] == 200:
					blank_image[i,j] = 12
				elif image[i,j,0] == 0 and image[i,j,1] == 0 and image[i,j,2] == 0:
					blank_image[i,j] = 13

		cv2.imwrite(abs_addr, blank_image)
		print abs_addr