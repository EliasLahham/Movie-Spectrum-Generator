# Movie-Spectrum-Generator v1.0

Movie Spectrum Generator is a Python script that takes in a video file and produces a movie spectrum/bar code like image by scanning the video's frames and calculating the dominant color of the frame. The script takes in a few user parameters via a terminal, ideally some GUI in the future, and saves the image to the user's directory.

Here's an example output image of Lord of the Ring: The Two Towers.

![Lord of the rings: The Two Towers](https://i.imgur.com/hUqs4mV.png)

## How to use

### Libraries used
- binascii
- tkinter
- cv2
- imutils
- scipy
- PIL
- colorthief
- struct
- shutil
