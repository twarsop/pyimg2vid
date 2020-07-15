# pyimg2vid
A python script for stitching a folder of images into a video

# Usage and Arguments
pyimg2vid.py
- [-h] [-ofw [OUTPUT_FRAME_WIDTH]]
- [-ofh [OUTPUT_FRAME_HEIGHT]]
- [-ofbc [OUTPUT_FRAME_BACKGROUND_COLOUR]]
- [-oinitfd [OUTPUT_INITIAL_FRAME_DELAY]]
- [-oinbetfd [OUTPUT_INBETWEEN_FRAME_DELAY]]
- [-ofinfd [OUTPUT_FINAL_FRAME_DELAY]]
- [-ovformat [OUTPUT_VIDEO_FORMAT]]
- [-ovfile [OUTPUT_VIDEO_FILENAME]]
- [-ovfps [OUTPUT_VIDEO_FPS]]
- input_img_folder

positional arguments:
- input_img_folder: the folder containing the images to construct the video from, images will be used in alphabetical order to create the video

optional arguments:
- -h, --help: show this help message and exit
- -ofw [OUTPUT_FRAME_WIDTH], --output_frame_width [OUTPUT_FRAME_WIDTH]: the width of the video frames, that will be constructed (default = 1024)
- -ofh [OUTPUT_FRAME_HEIGHT], --output_frame_height [OUTPUT_FRAME_HEIGHT]: the height of the video frames, that will be constructed (default = 1024)
- -ofbc [OUTPUT_FRAME_BACKGROUND_COLOUR], --output_frame_background_colour [OUTPUT_FRAME_BACKGROUND_COLOUR]: hex code for the background video frame colour without the leading hash (default = '000000', black)
- -oinitfd [OUTPUT_INITIAL_FRAME_DELAY], --output_initial_frame_delay [OUTPUT_INITIAL_FRAME_DELAY]: the number of frames to delay the initial frame for, use to extend the length of time the initial frame will show for (default = 3)
- -oinbetfd [OUTPUT_INBETWEEN_FRAME_DELAY], --output_inbetween_frame_delay [OUTPUT_INBETWEEN_FRAME_DELAY]: the number of frames to delay the inbetween frames for (not the initial frame and not the final frame), use to extend the length of time each frame will show for (default = 1)
- -ofinfd [OUTPUT_FINAL_FRAME_DELAY], --output_final_frame_delay [OUTPUT_FINAL_FRAME_DELAY]: the number of frames to delay the final frame for, use to extend the length of time the final frame will show for (default = 3)
- -ovformat [OUTPUT_VIDEO_FORMAT], --output_video_format [OUTPUT_VIDEO_FORMAT]: the output format of the video (default = 'mp4v')
- -ovfile [OUTPUT_VIDEO_FILENAME], --output_video_filename [OUTPUT_VIDEO_FILENAME]: the output filename for the video (default = 'video.avi')
- -ovfps [OUTPUT_VIDEO_FPS], --output_video_fps [OUTPUT_VIDEO_FPS]: fps of the output video (default = 2)
