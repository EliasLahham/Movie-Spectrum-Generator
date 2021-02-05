# Movie-Spectrum-Generator v1.0

Movie Spectrum Generator is a Python script that takes in a video file and produces a movie spectrum/barcode like image by scanning video frames. Each vertical bar in the output image is made up of the dominant color of that particular frame. The script takes in various user parameters before saving the image to the user's desired file directory.

## Table of Contents
1. [Instructions](https://github.com/EliasLahham/Movie-Spectrum-Generator/blob/main/README.md#instructions)
2. [How it works](https://github.com/EliasLahham/Movie-Spectrum-Generator/blob/main/README.md#how-it-works)
3. [Examples](https://github.com/EliasLahham/Movie-Spectrum-Generator/blob/main/README.md#examples)
4. [Libraries used](https://github.com/EliasLahham/Movie-Spectrum-Generator/blob/main/README.md#libraries-used)
5. [Future plans](https://github.com/EliasLahham/Movie-Spectrum-Generator/blob/main/README.md#future-plans)

## Instructions

1. Have [libraries](https://github.com/EliasLahham/Movie-Spectrum-Generator/blob/main/README.md#libraries-used) installed and execute the script
2. Select a video file. Most formats are accepted (.mp4 and .mkv have been tested and work)
3. Select a location to save the movie spectrum image
4. Create a name for the movie spectrum image
5. Input desired width of movie spectrum image (vertical bar count)
  - **Each bar is 1 PIXEL WIDE**
6. Input desired height of movie spectrum image
7. The script should now be running...
  - **Typical runtime for 2000x by 200y images is around 3-5 minutes**

## How it works

- Magic

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
