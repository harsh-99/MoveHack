import pandas as pd
import tensorflow as tf
import model
from road import road_damage as rd
import os
import cv2
import numpy as np

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string('testing', '', """ checkpoint file """)
tf.app.flags.DEFINE_string('finetune', '', """ finetune checkpoint file """)
tf.app.flags.DEFINE_integer('batch_size', "5", """ batch_size """)
tf.app.flags.DEFINE_float('learning_rate', "1e-3", """ initial lr """)
tf.app.flags.DEFINE_string('log_dir', "/tmp3/first350/TensorFlow/Logs", """ dir to store ckpt """)
tf.app.flags.DEFINE_string('image_dir', "/tmp3/first350/SegNet-Tutorial/CamVid/train.txt", """ path to CamVid image """)
tf.app.flags.DEFINE_string('test_dir', "/tmp3/first350/SegNet-Tutorial/CamVid/test.txt", """ path to CamVid test image """)
tf.app.flags.DEFINE_string('val_dir', "/tmp3/first350/SegNet-Tutorial/CamVid/val.txt", """ path to CamVid val image """)
tf.app.flags.DEFINE_integer('max_steps', "2000", """ max_steps """)
tf.app.flags.DEFINE_integer('image_h', "360", """ image height """)
tf.app.flags.DEFINE_integer('image_w', "480", """ image width """)
tf.app.flags.DEFINE_integer('image_c', "3", """ image channel (RGB) """)
tf.app.flags.DEFINE_integer('num_class', "13", """ total class number """)
tf.app.flags.DEFINE_boolean('save_image', True, """ whether to save predicted image """)

def checkArgs():
    if FLAGS.testing != '':
        print('The model is set to Testing')
        print("check point file: %s"%FLAGS.testing)
        print("CamVid testing dir: %s"%FLAGS.test_dir)
    elif FLAGS.finetune != '':
        print('The model is set to Finetune from ckpt')
        print("check point file: %s"%FLAGS.finetune)
        print("CamVid Image dir: %s"%FLAGS.image_dir)
        print("CamVid Val dir: %s"%FLAGS.val_dir)
    else:
        print('The model is set to Training')
        print("Max training Iteration: %d"%FLAGS.max_steps)
        print("Initial lr: %f"%FLAGS.learning_rate)
        print("CamVid Image dir: %s"%FLAGS.image_dir)
        print("CamVid Val dir: %s"%FLAGS.val_dir)

    print("Batch Size: %d"%FLAGS.batch_size)
    print("Log dir: %s"%FLAGS.log_dir)


def main(args):
    checkArgs()
    if FLAGS.testing:
        model.test(FLAGS)
    elif FLAGS.finetune:
        model.training(FLAGS, is_finetune=True)
    else:
        model.training(FLAGS, is_finetune=False)

    if FLAGS.testing:
        path = FLAGS.test_dir
        fd = open(path)
        image_filenames = []
        filenames = []
        for i in fd:
            i = i.strip().split(" ")
            image_filenames.append(i[0])
        count = 0
        for image_path in image_filenames:
            orig_image = cv2.imread(image_path)
            
            img_seg = cv2.imread(os.getcwd() + "/out_image/" + str(image_filenames[count]).split('/')[-1])
            img_seg = cv2.resize(img_seg, (orig_image.shape[1], orig_image.shape[0]))
            img_seg = np.array(img_seg)
            cv2.imwrite("/out_image/" + str(image_filenames[count]).split('/')[-1], img_seg)
            #cv2.imshow("segmented resized", img_seg)
            #cv2.waitKey(0)
            points = []
            for i in range(img_seg.shape[0]):
                for j in range(img_seg.shape[1]):
                    if((img_seg[i,j,0] == 0 and img_seg[i,j,1] == 255 and img_seg[i,j,2] == 0) or (img_seg[i,j,0] == 0 and img_seg[i,j,1] == 0 and img_seg[i,j,2] == 255)):
                        points.append([j,i])

            points = np.array(points)           
            x, y, w, h = cv2.boundingRect(points)
            
            modified_image = orig_image[y:y+j,x:x+w]            
            #modified_image = cv2.resize(modified_image, Size(960, 720))
            #cv2.imshow("cropped", modified_image)
            #cv2.waitKey(0)
            cv2.imwrite("modified_image.jpg", modified_image)
            rd.pothole_detect(os.getcwd()+ "/modified_image.jpg", count)
            count = count + 1

if __name__ == '__main__':
  tf.app.run()
