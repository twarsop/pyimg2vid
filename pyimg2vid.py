from os import listdir
from os.path import isfile, join
import cv2
import numpy as np
import math
import argparse

parser = argparse.ArgumentParser()

# required command line arguments
parser.add_argument('input_img_folder', help='the folder containing the images to construct the video from, images will be used in alphabetical order to create the video')

# optional command line arguments
parser.add_argument('-ofw', '--output_frame_width', help='the width of the video frames, that will be constructed (default = 1024)', default=1024, type=int, nargs='?')
parser.add_argument('-ofh', '--output_frame_height', help='the height of the video frames, that will be constructed (default = 1024)', default=1024, type=int, nargs='?')
parser.add_argument('-ofbc', '--output_frame_background_colour', help='hex code for the background video frame colour without the leading hash (default = \'000000\', black)', default='000000', type=str, nargs='?')
parser.add_argument('-oinitfd', '--output_initial_frame_delay', help='the number of frames to delay the initial frame for, use to extend the length of time the initial frame will show for (default = 3)', default=3, type=int, nargs='?')
parser.add_argument('-oinbetfd', '--output_inbetween_frame_delay', help='the number of frames to delay the inbetween frames for (not the initial frame and not the final frame), use to extend the length of time each frame will show for (default = 1)', default=1, type=int, nargs='?')
parser.add_argument('-ofinfd', '--output_final_frame_delay', help='the number of frames to delay the final frame for, use to extend the length of time the final frame will show for (default = 3)', default=3, type=int, nargs='?')
parser.add_argument('-ovformat', '--output_video_format', help='the output format of the video (default = \'mp4v\')', default='mp4v', type=str, nargs='?')
parser.add_argument('-ovfile', '--output_video_filename', help='the output filename for the video (default = \'video.avi\')', default='video.avi', type=str, nargs='?')
parser.add_argument('-ovfps', '--output_video_fps', help='fps of the output video (default = 2)', default=2, type=int, nargs='?')

args = parser.parse_args()

# setup variables from comman line arguments
input_img_folder = args.input_img_folder

output_frame_width = args.output_frame_width
output_frame_height = args.output_frame_height
output_frame_background_colour = args.output_frame_background_colour

output_initial_frame_delay = args.output_initial_frame_delay
output_inbetween_frame_delay = args.output_inbetween_frame_delay
output_final_frame_delay = args.output_final_frame_delay

output_video_format = args.output_video_format
output_video_filename = args.output_video_filename
output_video_fps = args.output_video_fps

print('Constructing video ...')

# get the images and sort into order
imgs = [f for f in listdir(input_img_folder) if isfile(join(input_img_folder, f))]
imgs.sort()

# setup the video write
fourcc = cv2.VideoWriter_fourcc(*output_video_format) 
video = cv2.VideoWriter(output_video_filename, fourcc, output_video_fps, (output_frame_width, output_frame_height))

# setup for telling the user what the nearest 10% of the video construction is done - 10%, 20% etc
percent_marks_used = dict()
for pm in np.linspace(10, 100, 10):
    percent_marks_used[int(pm)] = 0

for img_counter in range(len(imgs)):
    # 'ui' for telling the user what the nearest 10% of the video construction is done - 10%, 20% etc
    percent_done = (float(img_counter+1) / float(len(imgs))) * 100
    ten_percent_floor = int(math.floor(percent_done / 10))*10
    if ten_percent_floor in percent_marks_used and percent_marks_used[ten_percent_floor] == 0:
        print(str(ten_percent_floor) + '%')
        percent_marks_used[ten_percent_floor] = 1

    # read the next image to create a new frame
    img = cv2.imread(input_img_folder + '\\' + imgs[img_counter],1)
    img_height, img_width, c = img.shape

    # find the image's largest dimension size (either width or height)
    # and the corresponding dimensions size for the frame that's about to be constructed from the image
    img_largest_dimension_size = img_width
    output_frame_corresponding_dimension_size = output_frame_width
    if img_height > img_width:
        img_largest_dimension_size = img_height
        output_frame_corresponding_dimension_size = output_frame_height

    # determine the ratio between these two sizes and use the ratio to resize the original image 
    # so that it will fit inside the frame
    ratio = (float(img_largest_dimension_size) / float(output_frame_corresponding_dimension_size))
    img_new_width = math.floor(float(img_width) / float(ratio))
    img_new_height = math.floor(float(img_height) / float(ratio))
    img_resize = cv2.resize(img, (img_new_width, img_new_height)) 
    
    # create a blank frame and fill with whatever frame background colour as been provided
    frame = np.zeros(shape=[output_frame_width, output_frame_height, 3], dtype=np.uint8)
    rgb = tuple(int(output_frame_background_colour[i:i+2], 16) for i in (0, 2, 4))
    frame[:,:] = (rgb[2], rgb[1], rgb[0]) # B G R

    # the resized image may not fit perfectly inside the video frame
    # work out the x and y offsets that are needed to centre the resized image within the frame
    img_resize_offset_x = int(math.floor(float(output_frame_width) / float(2)) - (float(img_resize.shape[1]) / float(2)))
    img_resize_offset_y = int(math.floor(float(output_frame_height) / float(2)) - (float(img_resize.shape[0]) / float(2)))

    # copy the resized image into the frame, using the offsets to centre
    frame[img_resize_offset_y:img_resize.shape[0]+img_resize_offset_y, img_resize_offset_x:img_resize.shape[1]+img_resize_offset_x] = img_resize[:,:]
    
    # fake any of the delays by just writing the frame multiple times to the video
    if img_counter == 0:
        for i in range(0, output_initial_frame_delay):
            video.write(frame)
    elif img_counter == len(imgs) - 1:
        for i in range(0, output_final_frame_delay):
            video.write(frame)
    else:
        for i in range(0, output_inbetween_frame_delay):
            video.write(frame)

# tidy the video and output
cv2.destroyAllWindows()
video.release()

print('... completed')