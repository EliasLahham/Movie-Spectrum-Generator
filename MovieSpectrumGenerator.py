from __future__ import print_function

import binascii
import os
import shutil
import struct
import tkinter as tk
from tkinter import filedialog

import cv2
import imutils
import numpy as np
import scipy
import scipy.cluster
import scipy.misc
from PIL import Image, ImageColor
from colorthief import ColorThief


class FilePaths:
	def __init__(self, video_path, save_path, tmp_frame_folder_path):
		self.video_path = video_path
		self.save_path = save_path
		self.tmp_frame_folder_path = tmp_frame_folder_path


class SpectrumImageParameters:
	def __init__(self, image_name, width, height):
		self.image_name = image_name
		self.width = width
		self.height = height
		self.spectrum_image = Image.new('RGB', (width, height))


class VideoMetadata:
	def __init__(self, fps, total_frames, width):
		self.fps = fps
		self.total_frames = total_frames
		self.frame_offset = round(total_frames / width)


def main():
	file_paths = get_file_paths()
	spectrum_image_parameters = get_spectrum_image_parameters()
	process_video(file_paths, spectrum_image_parameters)
	print('Deleting tmpFrame folder...')
	shutil.rmtree(file_paths.tmp_frame_folder_path)


def get_file_paths():
	print('Select video ...')
	video_path = filedialog.askopenfilename()
	print(f'video_path: {video_path}')
	if not video_path:
		print('Exitting')
		exit()
	print('Select folder to save Movie Spectrum Image ...')
	save_path = filedialog.askdirectory()
	if not save_path:
		print('Exitting')
		exit()
	tmp_frame_folder_path = save_path + '/tmpFrames/'
	os.mkdir(tmp_frame_folder_path)  # Holds frames to be processed, deleted later
	return FilePaths(video_path, save_path, tmp_frame_folder_path)


def get_spectrum_image_parameters():
	image_name = input('Name of spectrum image ...\n> ')
	width = int(input('Desired width of spectrum image (Bar count) ...\n> '))
	height = int(input('Desired height of spectrum image ...\n> '))
	return SpectrumImageParameters(image_name, width, height)


def process_video(file_paths, spectrum_image_parameters):
	video = cv2.VideoCapture(file_paths.video_path)
	video_metadata = get_video_fps_and_total_frames(video, spectrum_image_parameters.width)
	spectrum_image_parameters = iterate_frames(video, video_metadata, file_paths, spectrum_image_parameters)
	save_image(spectrum_image_parameters, file_paths.save_path)


def get_video_fps_and_total_frames(video, width):
	(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
	if int(major_ver) < 3:
		fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
		total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
		print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
		print("Total Frames using video.get(cv2.CAP_PROP_FRAME_COUNT): {0}".format(total_frames))
	else:
		fps = video.get(cv2.CAP_PROP_FPS)
		total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
		print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
		print("Total Frames using video.get(cv2.CAP_PROP_FRAME_COUNT): {0}".format(total_frames))
	return VideoMetadata(fps, total_frames, width)


def iterate_frames(video, video_metadata, file_paths, spectrum_image_parameters):
	# Process first frame seperately
	spectrum_image_parameters, should_continue = process_video_frame(
		video, file_paths, 0, spectrum_image_parameters
	)

	has_frames_left = True
	bar_count = 1
	set_frame = 1
	while has_frames_left:
		set_frame = set_frame + video_metadata.frame_offset
		if set_frame <= video_metadata.total_frames:
			video.set(cv2.CAP_PROP_POS_FRAMES, set_frame)
			spectrum_image_parameters, should_continue = process_video_frame(
				video, file_paths, bar_count, spectrum_image_parameters
			)
			print(f'bar_count: {bar_count}')
			bar_count += 1
			if not should_continue:
				has_frames_left = False
				video.release()
		else:
			has_frames_left = False
			video.release()
	return spectrum_image_parameters


def process_video_frame(video, file_paths, bar_count, spectrum_image_parameters):
	success, image = video.read()
	image = imutils.resize(image, width=160, height=100)
	cv2.imwrite(file_paths.tmp_frame_folder_path + '%d.png' % bar_count, image)
	dominant_color = get_dominant_hex_color_of_image(file_paths.tmp_frame_folder_path + '%d.png' % bar_count)
	spectrum_image_parameters.spectrum_image, should_continue = draw_bar_on_spectrum(
		spectrum_image_parameters, dominant_color, bar_count
	)
	return spectrum_image_parameters, should_continue


def get_dominant_hex_color_of_image(image_path):
	color_thief = ColorThief(image_path)
	dominant_color = color_thief.get_color(quality=2)
	return rgb_to_hex(dominant_color)


def rgb_to_hex(dominant_color):
	return "#{:02x}{:02x}{:02x}".format(int(dominant_color[0]), int(dominant_color[1]), int(dominant_color[2]))


def draw_bar_on_spectrum(spectrum_image_parameters, dominant_color, bar_count):
	print('Drawing bar')
	y = 0
	while spectrum_image_parameters.height > y:
		if bar_count >= spectrum_image_parameters.width:
			return spectrum_image_parameters.spectrum_image, False
		else:
			spectrum_image_parameters.spectrum_image.putpixel((bar_count, y), ImageColor.getrgb(dominant_color))
			y += 1
	y = 0
	return spectrum_image_parameters.spectrum_image, True


def save_image(spectrum_image_parameters, save_path):
	save_path_formatted = save_path + '/' + spectrum_image_parameters.image_name + '.png'
	spectrum_image_parameters.spectrum_image.save(save_path_formatted, 'PNG')
	os.startfile(save_path_formatted)


print('Executing')
root = tk.Tk()
root.withdraw()
main()
