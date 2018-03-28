import cv2
import torch
from time import time

from darknet import Darknet
from utils import *


def demo(cfgfile, weightfile, use_cuda=torch.cuda.is_available()):
    m = Darknet(cfgfile)
    m.print_network()
    m.load_weights(weightfile)
    print('Loading weights from %s... Done!' % (weightfile))

    if m.num_classes == 20:
        namesfile = 'data/voc.names'
    elif m.num_classes == 80:
        namesfile = 'data/coco.names'
	## This is the quick and dirty
    elif m.num_classes == 1:
        namesfile = 'data/skellington.names'
    else:
        namesfile = 'data/names'
    class_names = load_class_names(namesfile)

    if use_cuda:
        m.cuda()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Unable to open camera")
        exit(-1)

    timer = 0

    while True:
        res, img = cap.read()
        if res:
            sized = cv2.resize(img, (m.width, m.height))
            start = time.time()
			## Changed the threshold from Yolo's 0.5 to Tiny Yolo 0.24
            bboxes = do_detect(m, sized, 0.24, 0.4, use_cuda)
            print('------')
            draw_img = plot_boxes_cv2(img, bboxes, None, class_names)
            cv2.imshow(cfgfile, draw_img)
            timer += time.time() - start
            print('fps: ', (1 / timer))
            timer = 0
            cv2.waitKey(1)
        else:
             print("Unable to read image")
             exit(-1)

############################################
if __name__ == '__main__':
    if len(sys.argv) == 3:
        cfgfile = sys.argv[1]
        weightfile = sys.argv[2]
        demo(cfgfile, weightfile)
        #demo('cfg/tiny-yolo-voc.cfg', 'tiny-yolo-voc.weights')
    else:
        print('Usage:')
        print('    python demo.py cfgfile weightfile')
        print('')
        print('    perform detection on camera')
