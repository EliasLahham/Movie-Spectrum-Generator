# Movie-Spectrum-Generator v1.0

Movie Spectrum Generator is a Python script that takes in a video file and generates a movie spectrum/barcode like image by scanning video frames. Each vertical bar in the output image is made up of the dominant color of that particular frame. The script takes in various user parameters before saving the image to the user's desired file directory.

## Table of Contents
1. [Instructions](https://github.com/EliasLahham/Movie-Spectrum-Generator/blob/main/README.md#instructions)
2. [How it works](https://github.com/EliasLahham/Movie-Spectrum-Generator/blob/main/README.md#how-it-works)
3. [Examples](https://github.com/EliasLahham/Movie-Spectrum-Generator/blob/main/README.md#examples)
4. [Libraries used](https://github.com/EliasLahham/Movie-Spectrum-Generator/blob/main/README.md#libraries-used)
5. [Future plans](https://github.com/EliasLahham/Movie-Spectrum-Generator/blob/main/README.md#future-plans)

## Instructions

1. Have these [libraries](https://github.com/EliasLahham/Movie-Spectrum-Generator/blob/main/README.md#libraries-used) installed and execute the script
2. Select a video file. Most formats are accepted (.mp4 and .mkv have been tested and work)
3. Select a location to save the movie spectrum image
4. Create a name for the movie spectrum image
5. Input desired width of movie spectrum image (vertical bar count)
   - **Each bar is 1 PIXEL WIDE**
6. Input desired height of movie spectrum image
7. The script should now be running...
   - **Typical runtime for 2000x by 200y images is around 3-5 minutes**

## How it works

After user parameters are entered, these steps will execute:

1. OpenCV will start a VideoCapture
2. Script will record video metadata:
   - fps
   - total_frames
   - frame_offset (total_frames/user specified width)
3. Begin processing video frames
   - Any frame being processed will run through colorthief and return the dominant_color of that frame
   - Any frame being processed is also temporarily stored in a temp folder that will be deleted after the script finishes
   - After a dominant_color is returned, a 1 x (height specified by user) is drawn with that dominant_color
   - The next frame is determined by the frame_offset variable

## Examples

**The Lord of the Rings: The Two Towers**
![Lord of the rings: The Two Towers](https://i.imgur.com/hUqs4mV.png)

**Dunkirk**
![Dunkirk](https://i.imgur.com/Nye9ODm.png)

**Avatar the Last Airbender S1 Ep1**
![ATLA: S1 EP1](https://i.imgur.com/nZcqWbf.png)

**Avatar the Last Airbender S3 Ep60**
![ATLA: S3 EP60](https://i.imgur.com/pClOmud.png)

## Libraries used
- binascii
- tkinter
- cv2
- imutils
- scipy
- PIL
- colorthief
- struct
- shutil

## Future plans

- GUI for user to input file paths and image parameters
- Improve speed of image generation
- Make this script into an executable
