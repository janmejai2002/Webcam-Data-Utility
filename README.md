# Webcam Data Utility

You can collect your own dataset using your webcam only by the use of this repo. It allows you to define a Region Of Interest on the screen, inside of which will be captured. The features are quite a lot so make sure you read the following carefully.

------------------------------

## Setup

First go into a desired directory and open terminal or git bash, then run

        git clone https://github.com/janmejai2002/Webcam-Data-Utility.git
        
Then change directory to Webcam-Data-Utililty and proceed as follows.

To setup your environment run :

        pip install -r requirements.txt

You might have to use `pip3 ` instead of `pip` based on your settings.

------------------------------

## Have a look

![](https://github.com/janmejai2002/Webcam-Data-Utility/blob/master/assets/gif2.gif)

------------------------------

## Usage `collect_data.py`

`collect_data.py` can be employed for collection of various classes of hand gestures in the form of:
-  Masks
-  Image inside ROI
-  Original image in ROI without background.
-  Image in ROI without background in grayscale.

Let's call these `save_types`.

They can be visualized as :

![](https://github.com/janmejai2002/Hand-Gesture-Control/blob/master/assets/collage.jpg)

------------------------------

#### Keyboard use for box movements

- `W`, `S`, `A` and `D` for up,down,left and right respectively.
- `I` and `K` for resizing.
- `R` to reset the position.
- `B` to capture background.
- `V` to writing ROI in different save types to your directory.
- `Q` to exit.


Note that you cannot capture the anything apart from Original ROI if you have not captured the background by pressing `B`.

Note : In the following commands you might have to replace `python` with `python3` based on your configurations.

To test the script run:

        python collect_data.py

or with complete command line arguments:

        python collect_data.py [-h] [-c CLASS] [-w WEBCAM] [-s SAVEOPTIONS] [-n SAVENUM]
  
        
 You have the following command line arguments at your disposal to make the most out of this repo.

        -h, --help            show this help message and exit

        -c CLASS, --class CLASS
                                Name class directory to save images to
        -w WEBCAM, --webcam WEBCAM
                                Webcam source, if 0 does not work try changing to 1,
                                external webcams might register on 1
        -s SAVEOPTIONS, --saveoptions SAVEOPTIONS
                                 1 : for saving mask, 2 : grayscale hand image without
                                background , 3 : original roi without background ,
                                Combinations are also allowed e.g. 12 or 21 for mask
                                and grayscale ,123 for saving all and so on ...
        -n SAVENUM, --savenum SAVENUM
                                Change it to maximum integer present in file names, in
                                the dir you want to save. This helps in resuming the
                                collection or else all present files will be
                                overwritten


Running the above command(i.e without any arguments) does the following steps:

- Creates a directory titled 'testing'
- creates a directory called 'orig_roi' inside testing.
- Initiates your webcam and closes if after capturing one frame to get the maximum dimensions for defining the initial position of ROI box.
- Starts webcam again and shows you the ROI box on screen along with the coordinates on top.

After this you have the following control:

- Move the ROI box using `W`,`S`,`A` and `D` for up, down, left and right motion.
- `I` and `K` for resizing the ROI. Minimum is `50x50`
- `V` for capturing the ROI as it is.

- Now if you want to initiate the masking of your ROI, you need to first capture the background. Which means your hand(non-static object) should not be inside ROI. To do that press `B` on your keyboard.


   - Once the background had been captured, you will see a window pop up titled `mask`. You can see other save_types by uncommenting them in `videostream.py`.
   - Try moving your hand inside the ROI box and see what happens.
   - Now to capture this you just need to press `V` and as a default it will start capturing masks along with the original ROI.
   - The masks will be saved inside `testing/masks` and the original roi insiden `testing/orig_roi`


The above command has the default features of saving files in a `testing` folder and saving only `masks` and `original ROI`.

------------------------------

#### For example:

You might want to save images of your fist as a class and want to save all types, i.e masks, grayscale, Original ROI and ROI without background. You also want to use a different webcam.

Run the following command

        python collect_data.py --class "fist" --webcam 1 --saveoptions 123

Note that class needs to be a `str`.

This will create a fist directory and create the following directories inside it:
- grayscale
- mask
- orig_no_Bg
- orig_roi

After this the process is same, get the box to desired position using `W`, `S`,`A` and `D`.Resize using `I` and `K`. Then capture the background using `B`. After that you just need to press `V` to save images. Press `Q` to exit.

Suppose you just wanted to capture masks and grayscale along with Original ROI, You need to use `--saveoptions 12`.

        python collect_data.py --class "thumbs_up" --saveoptions 12

To know more about these command line arguments run

        python collect_data.py --help

------------------------------

## IMPORTANT:

If you have already saved images to a directory and want to add more images, change `--savenum` in the command line arguments.

For example:

If I collected some dataset for `fist` and added 200 images to my directory, they are going to be saved as `0.jpg`, `1.jpg`,`2,jpg` ...... `199.jpg` . If I resume collection without adding `--savenum 200` ,  all the images will be overwritten.

I will run:

        python collect_data.py --class "fist" --savenum 200

The script detects the presence of "fist" directory and does not create anything new. All imaged saved further are added to the pre-existing directory.

------------------------------

### Additional help

To get the images I have displayed, I used my phone's camera as my webcam using an application called `Droid Cam`. You can find more details [here](https://www.dev47apps.com/) for setting it up.

Using my laptop's webcaam introduced a lot of noise in the image due to poor quality of webcam.

If you end up using `Droid Cam`, turn on `Exposure Lock` in settings.

To run the script for my phone's webcam I used `--webcam 1` in the command line arguments.

