from imutils.video import VideoStream
from save_options import *
from videostream import *
from roi_class import *
import numpy as np
import argparse
import imutils
import time
import copy
import time
import cv2
import os


ap = argparse.ArgumentParser()

ap.add_argument("-c", "--class", type=str, default = "testing" , help="Name class directory to save images to")

ap.add_argument("-w", "--webcam", type=int, default=0, help ="Webcam source, if 0 does not work try changing \
    to 1, external webcams might register on 1")

ap.add_argument("-s", "--saveoptions", type=int, default=1, help="\
    1 : for saving mask,\
    2 : grayscale hand image without background , \
    3 : original roi without background ,\
    Combinations are also allowed e.g. 12 or 21 for mask and grayscale \
        ,123 for saving all and so on ...")

ap.add_argument("-n", "--savenum", type=int, default=0, help="Change it to maximum integer present in file names, \
    in the dir you want to save. This helps in resuming the collection or else all present files will be overwritten")

args = vars(ap.parse_args())


if not os.path.exists(os.path.join(os.getcwd(), args["class"])):
    os.mkdir(os.path.join(os.getcwd(), args["class"]))

save_dir = os.path.join(os.getcwd(), args["class"])

mask_dir, grayscale_dir, orig_no_Bg, orig_roi = create_dir(args["saveoptions"], save_dir)
class_save_dir = [mask_dir, grayscale_dir, orig_no_Bg, orig_roi]
print(f"[INFO] Directories created/existed : {class_save_dir}")

# # Capture the frame by initializing the webcam once
# and capturing the image as a numpy array
print("[INFO] Initializing webcam ...")
vs = VideoStream(src=args["webcam"]).start()
time.sleep(1)
frame_base = vs.read()
print(f"Frame dimensions : {frame_base.shape[1]}x{frame_base.shape[0]}")

# Continue saivng from last image in dir
save_num = args["savenum"]

# defining initial boundaries and size for roi box
roi_x = frame_base.shape[1]//2
roi_y = frame_base.shape[0]//2
roi_h = frame_base.shape[1]//5
roi_w = frame_base.shape[1]//5
# defining movements and size change steps
movement_steps = 5
size_change_steps = 1
isBgCaptured = 0
bgSubThreshold = 60
learningRate = 0
bgModel = None

# using roi class
roi = roi(roi_x, roi_y, roi_h, roi_w, frame_base,
          movement_steps, size_change_steps)

print(f"[INFO] initial roi values are : {roi.display_val()}")

while True:
    frame = vs.read()
    thresh, blur, img_no_Bg, img_orig_roi = videostream_initialize(roi, frame, isBgCaptured,
                           bgModel,learningRate)

    save_types = [thresh, blur, img_no_Bg, img_orig_roi]

    key = cv2.waitKey(10) & 0xFF
    if key == ord('q'):
        break

    if key == ord('b'):
        bgModel = cv2.createBackgroundSubtractorMOG2(0, bgSubThreshold)
        time.sleep(0.5)
        isBgCaptured = 1
        print('Background Captured')


    if key == ord('v'):
        save_files(save_types, class_save_dir, save_num, isBgCaptured)
        save_num += 1

    roi.action_control(key)
