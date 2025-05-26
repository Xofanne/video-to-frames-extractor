# If you want to run from command line

## pre requisites (libraries)

numpy
opencv-python

## instructions

place the extractor.py file in any folder you want and run it with `python extractor.py` or `python3 extractor.py`.


# If you prefer to use the executable

Download the exe file from [Release](https://github.com/Xofanne/video-to-frames-extractor/releases/tag/v1.0test) and place it anywhere you want.
run it and a terminal window will open to feed the arguments.

# The arguments:

### insert the video path
absolute path of the video file or the name if the video is in the same folder as the extractor file.

e.g. `C:\Users\username\Downloads\video.mp4` if you want to pass the absolute path
e.g. `video.mp4` if the video is in the same folder as the extractor program.

### insert dir name to extract the frames
absolute path or the name of the folder to extract the frames to.

e.g `C:\Users\username\Downloads\extracted_dir` if you want to pass the absolute path
e.g. `extracted_dir` if you want to create a new folder in the same folder where the extractor program is.

### Add noise to frames?
`y` if you want to add noise to the extracted frames, `n` otherwise

### Convert extracted frames to grayscale? 
`y` if you want to convert the frames to grayscale, `n` otherwise

### overwrite files if already exists?
`y` if you want to overwrite files (has effect only if files in destination already exists), `n` otherwise.

### Select the noise intensity from 1 to 3 
select 1, 2 or 3 to select noise intensity.


# For reference

a 5 minute video at 720p with ~7500 frames took around 8 minutes to add noise to all of them.