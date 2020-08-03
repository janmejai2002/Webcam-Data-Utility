import numpy as np
import cv2
import os


def check_and_create(save_dir, type_save):
    if not os.path.exists(os.path.join(save_dir, type_save)):
        os.mkdir(os.path.join(save_dir, type_save))
    return os.path.join(save_dir, type_save)

def create_dir(n, save_dir):
    orig_roi = check_and_create(save_dir, 'orig_roi')
    if n == 1:
        mask_dir = check_and_create(save_dir, 'mask')
        return mask_dir, 'Nil', 'Nil', orig_roi

    if n==2:
        grayscale_dir = check_and_create(save_dir, 'grayscale')
        return 'Nil', grayscale_dir, 'Nil', orig_roi

    if n==3:
        orig_no_Bg = check_and_create(save_dir, 'orig_no_Bg')
        return 'Nil', 'Nil', orig_no_Bg, orig_roi

    if n == 12 or n==21:
        mask_dir = check_and_create(save_dir, 'mask')
        grayscale_dir = check_and_create(save_dir, 'grayscale')
        return mask_dir, grayscale_dir, 'Nil', orig_roi


    if n == 13 or n == 31:
        mask_dir = check_and_create(save_dir, 'mask')
        orig_no_Bg = check_and_create(save_dir, 'orig_no_Bg')
        return mask_dir, 'Nil', orig_no_Bg, orig_roi

    if n ==23 or n == 32:
        grayscale_dir = check_and_create(save_dir, 'grayscale')
        orig_no_Bg = check_and_create(save_dir, 'orig_no_Bg')
        return 'Nil', grayscale_dir, orig_no_Bg, orig_roi

    if n ==123 or n==132 or n ==231 or n==213 or n == 321 or n==312:
        mask_dir = check_and_create(save_dir, 'mask')
        grayscale_dir = check_and_create(save_dir, 'grayscale')
        orig_no_Bg = check_and_create(save_dir, 'orig_no_Bg')
        return mask_dir, grayscale_dir, orig_no_Bg, orig_roi



def save_files(save_types, class_save_dir, save_num, isBgCaptured):
    if isBgCaptured == 0:
        img_save_name = os.path.join(class_save_dir[3], str(save_num)+'.jpg')
        cv2.imwrite(img_save_name, save_types[3])
        print(f"Saved at {img_save_name}")

    else:
        for i in range(4):
            if class_save_dir[i] != "Nil" and np.sum(save_types[i]) != 0:
                img_save_name = os.path.join(class_save_dir[i], str(save_num) + '.jpg')
                cv2.imwrite(img_save_name, save_types[i])
                print(f"Saved at {img_save_name}")
