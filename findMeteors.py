#!/usr/bin/env python

import sys
import os
import subprocess
import shutil

def removeBrightImages(images, threshold):
	#The average graylevel of an image may be found using the string format "%[mean]"
	#convert image -format "%[mean]" info:
	count = 0
	darkFrames = []
	for image in images:
		if count > 0:

			command = 'convert ' + image + ' -format "%[mean]" info:'
			try:
				val = subprocess.check_output(command,shell=True) 

			except subprocess.CalledProcessError as e:

				val = e.output

			if float(val) < threshold:
				print "Adding " + image + ": brightness under threshold, queued for comparison"
				darkFrames.append(image)
			else:
				print "Rejecting " + image + ": brightness exceeds threshold"
		count = count + 1
	print darkFrames
	return darkFrames

def findChanges(images, fuzz, threshold):
	#fuzz is currently hardcoded below
	count = 0
	changedFrames = []
	commandList = []
	for image in images:
		if count > 0:
			#Trying to do this the better way with arguments and no shell=True results in the conversion
			#of the output to an int failing below, and I have not figured out why.

			#print "Comparing " + lastImage + " to " + image

			command = "compare -metric ae -fuzz 15% " +  lastImage + " " + image + " null: 2>&1"
			try:
				val = subprocess.check_output(command,shell=True) 

			#The compare program returns 2 on error otherwise 0 if the images are similar or 1 if they are dissimilar.
			except subprocess.CalledProcessError as e:

				val = e.output

    				if e.returncode == 2:
					print "Error in image comparison routine."
					sys.exit()

			if int(val) > threshold:
				print image + ": " + val + ", item found"
				changedFrames.append(image)
			else:
				print "Checking: " + image 

		lastImage = image
		count = count + 1

	return changedFrames

def saveImages(images):
	for image in images:
		shutil.copy2(image, sys.argv[2]) 



def genImageList():
	imageList = []
	for file in os.listdir(sys.argv[1]):
    		if file.endswith(".jpg"):
        		imageList.append(os.path.join(sys.argv[1], file))
	imageList.sort()
	return imageList


def checkArgs():
	if len(sys.argv) != 3:
		print "Usage: ./findMeteors.py <image dir> <output dir>"
		sys.exit()

	if os.path.isdir(sys.argv[2]):
		print "Output directory exists already, refusing to overwrite it. Exiting."
		sys.exit()
	else:
		print "Creating output directory"
    		os.makedirs(sys.argv[2])



def main():

	#if brightness thresholding is enabled, set threshold. Higher is brighter.
	brightnessThreshold = 2000

	#frame difference comparison senstivity. A higher value reduces sensitivity. 0-100.
	fuzzFactor = 15

	#the number of pixels that must be different between frames in order to flag it as interesting.
	diffThreshold = 100

	checkArgs()
	images = genImageList()
	#if you want to enable brightness thresholding, uncomment the line below
	#images = removeBrightImages(images, float(brightnessThreshold))
	changedFrames = findChanges(images, fuzzFactor, diffThreshold)
	saveImages(changedFrames)

if __name__ == '__main__':
  main()
