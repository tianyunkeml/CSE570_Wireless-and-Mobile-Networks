import numpy as np
import matplotlib.image as mpimg
import localization as lc
import math
import pdb

heatmap = np.zeros((60, 100, 3))
reso_set = [5, 10, 15, 20]		# resolutions. There's no '1' because it takes too much time to run
num_trans_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]		# number of transmitters
std_set = [1, 2, 3, 4, 5, 10]		# standard deviations

def get_color(min_blue, max_blue, min_acc, max_acc, acc):		# given accuracy, get its color
	blue = max_blue - ((acc - min_acc) / (max_acc - min_acc)) * (max_blue - min_blue)
	blue = math.floor(blue)
	red = 220 - ((acc - min_acc) / (max_acc - min_acc)) * (220 - 20)
	red = 255 - red
	green = red
	blue = 255 - blue
	red = int(red)
	green = int(green)
	blue = int(blue)
	return (red, green, blue)

for reso in reso_set:
	accuracyDict = {}
	colorDict = {}
	max_accu = -1000
	min_accu = 1000
	for std in std_set:		# loop to get accuracy for each configuration
		for num_trans in num_trans_set:
			myLocator = lc.locator(num_trans, reso, std)
			if reso == 1:
				myLocator.run_simulation(1)
			else:
				myLocator.run_simulation(10) #XXXXXXXXXXXX
			error = myLocator.errors
			mean_err = sum(error) / len(error)
			accuracy = max(120 - mean_err, 0)
			if accuracy > max_accu:
				max_accu = accuracy
			if accuracy < min_accu:
				min_accu = accuracy
			dictKey = (std, num_trans)
			accuracyDict[dictKey] = accuracy
	for k, v in accuracyDict.items():		# loop to get color for each configuratjion
		color = get_color(225, 255, 0, 120, v)
		colorDict[k] = color

	for k, v in colorDict.items():		# draw heatmap
		std = k[0]
		num_trans = k[1]
		ind_i = std_set.index(std)
		ind_j = num_trans_set.index(num_trans)
		for i in range(10):
			for j in range(10):
				heatmap[ind_i * 10 + i][ind_j * 10 + j] = v

	mpimg.imsave('heatmap_reso_' + str(reso) + '.png', heatmap)
