import argparse
import os
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--folder', dest='folder', help='folder input')

if not os.path.exists('out_image'):
	os.mkdir('out_image')

if not os.path.exists('road_damage'):
	os.mkdir('road_damage')

args = parser.parse_args()
f = open('test.txt','w')
for i in os.listdir(args.folder):
	line = args.folder.replace(' ','\ ')+'/'+i+' '+args.folder.replace(' ','\ ')+'/'+i+'\n'
	f.write(line)
f.close()

os.system('python main.py --testing=logs/model.ckpt-27000  --log_dir=logs/ --test_dir=test.txt --batch_size=5 --save_image=True')
