#!/usr/bin/env python

"""
Usage: extract_frames_cropped_image.py --image_path=<image> --output_dir=<dir> --crop-size=<cs> --step-v=<sv> --step-h=<sh>

python extract_frames_cropped_image.py --image_path=/home/ankit/Downloads/4k-wallpaper-automobile-automotive-1149137.jpg  --output_dir=output_frames/ --crop-size=400 --step-v=200 --step-h=200

The script will extract frames from <image>. For each
frame, it takes multiple crops of size <cs>. Starting in the top-left corner,
each frame is scanned using a crop window of size <cs>, with a slide of <sh>
pixels in the horizontal direction and <sv> pixels in the vertical direction.

"""

import os
import time
from argparse import ArgumentParser, ArgumentTypeError

import cv2
from tqdm import tqdm
from imutils import paths

def isfile(x):
    if not os.path.isfile(x):
        raise ArgumentTypeError('The file {} does not exist!'.format(x))
    else:
        return x

def isdir(x):
    if not os.path.isdir(x):
        raise ArgumentTypeError('Could not find folder {}'.format(x))
    else:
        return x

parser = ArgumentParser()
parser.add_argument('--image_path', required=True, dest='image_path',
                    help='Path to file')
parser.add_argument('--single', required=True, dest='single',
                    help='y for Single file, n for multiple files')
parser.add_argument('--output_dir', required=True, dest='output_dir',
                    help='Path to output frames')
parser.add_argument('--crop-size', required=True, dest='crop_size', type=int,
                    help='Desired size of the output crop', metavar='crop size')
parser.add_argument('--step-v', dest='crop_step_v', required=True, type=int,
                    help='Vertical step of crop in the original image',
                    metavar='crop step vertical')
parser.add_argument('--step-h', dest='crop_step_h', required=True, type=int,
                    help='Horizontal step of crop in the original image',
                    metavar='crop step horizontal')
args = parser.parse_args()



def get_image_name(image_path):
    return os.path.splitext(os.path.basename(image_path))[0]

def extract_frame_from_image(image_path, crop_size, crop_step_v, crop_step_h):
    frame = cv2.imread(image_path)
    height, width = frame.shape[:2]
    number_steps_v = int((height - crop_size) / crop_step_v) + 1
    number_steps_h = int((width - crop_size) / crop_step_h) + 1

    print('Processing Image : {} '.format(os.path.basename(image_path)))

    with tqdm(total=1, unit='frames') as pbar_frames:
        start_height = 0
        for r in range(number_steps_v):
            start_width = 0
            for c in range(number_steps_h):
                crop_id = '_r{}c{}'.format(r, c)
                crop_path = os.path.join(
                    output_dir, get_image_name(image_path) + crop_id + '.jpg')
                crop = frame[start_height:(start_height + crop_size),
                                start_width:(start_width + crop_size)]
                cv2.imwrite(crop_path, crop)
                start_width += crop_step_h
            start_height += crop_step_v

        pbar_frames.update(1)


image_path = args.image_path
l_images = []
if args.single == 'y':
    isfile(image_path)
    n_images = 1
    l_images.append(image_path)
else :
    isdir(image_path)
    l_images = list(paths.list_images(image_path))

for index in range(0, len(l_images)):
    print("Image Path : {}".format(l_images[index]))
    output_dir = args.output_dir
    crop_size = args.crop_size
    crop_step_v = args.crop_step_v
    crop_step_h = args.crop_step_h

    extract_frame_from_image(l_images[index], crop_size, crop_step_v, crop_step_h)