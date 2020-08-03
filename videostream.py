from roi_class import roi
import numpy as np
import cv2


def remove_background(frame, bgModel, learningRate):
    fgmask = bgModel.apply(frame, learningRate=learningRate)
    kernel = np.ones((2, 2), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=2)
    fgmask = cv2.dilate(fgmask, None, iterations=2)

    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res


def videostream_initialize(roi, frame, isBgCaptured, bgModel,learningRate):
    frame = cv2.flip(frame, 1)
    # create vertices in form of tuples for cv2.rectangle
    A, C = roi.create_box()
    #display initial values of ROI box
    values = roi.display_val()
    # draw the rectangle on screen
    cv2.rectangle(frame, A, C, (0, 255, 0), 2)
    # draw the coordinates on screen
    cv2.putText(frame, values, (50, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (10, 240, 50))
    #display the frame
    cv2.imshow('Camera', frame)
    # check if movement of ROI is out of bounds. If yes, bring it back to previous state.
    roi.check_all()
    # slice of the ROI from frame.
    roi_zone = roi.create_roi_zone()
    img_orig_roi = frame[roi_zone[0]:roi_zone[1], roi_zone[2]:roi_zone[3]]


    if isBgCaptured == 1:
        img = img_orig_roi
        img = remove_background(img, bgModel, learningRate)
        #cv2.imshow('orig_no_Bg', img)

        # convert to binary image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('grayscale', gray)
        blur = cv2.GaussianBlur(gray, (11, 11), 0)

        ret, thresh = cv2.threshold(
            blur, 60, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cv2.imshow('mask', thresh)

        return thresh, gray, img, img_orig_roi

    else:
        return np.array(0), np.array(0), np.array(0), img_orig_roi
    #cv2.waitkey(0)
    #cv2.destroyAllWindows()
