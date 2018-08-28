import argparse
import sys
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--folder', dest='folder', action='store_const',
                    help='folder input')

args = parser.parse_args()
f = open('test.txt','w')
for i in os.listdir(args.folder):
	f.write(os.getcwd()+'/'+args.folder+'/'+i+'\n')
f.close()

os.system('python main.py --testing=logs/model.ckpt-27000  --log_dir=logs/ --test_dir=test.txt --batch_size=5 --save_image=True')
