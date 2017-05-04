import numpy as np
import math
import matplotlib as plt
import pdb

# Class grid to describe all important info of each grid
# including path loss model, data generation etc.
class grid:
	def __init__(self, i, j, trans, k, std):
		self.x = j
		self.y = i
		self.coor_x = self.x * k + 0.5 * k    # actual coordinate of the grid center
		self.coor_y = self.y * k + 0.5 * k
		self.gaussian_set = []    # gaussian distribution of RSS from each transmitter in this grid
		self.train = []    # training data set
		self.test = []		# testing data set
		self.usable = True 		# True if this grid is not the grid of transmitters
		self.trained_gaussian_set = []		# trained gaussian distribution from training data set

		for trans_xy in trans:		# loop to get the gaussian distributions
			trans_x = trans_xy[1]
			trans_y = trans_xy[0]
			# pdb.set_trace()
			d = math.sqrt((trans_x * k + 0.5 * k - self.coor_x) ** 2 + (trans_y * k + 0.5 * k - self.coor_y) ** 2)
			if d == 0:
				self.usable = False
				return
			mean = 10 * 2.5 * math.log10(d)
			self.gaussian_set.append([mean, std])


		def data_generate(self, num_data, trans):		# randomly generate training data and testing data
			for i in range(num_data):
				feature = []
				for j in range(len(trans)):
					mean = self.gaussian_set[j][0]
					std = self.gaussian_set[j][1]
					sample = np.random.normal(mean, std, 1)
					feature.append(sample[0])
				rd = np.random.random()
				if rd < 0.9:
					self.train.append(feature)
				else:
					self.test.append(feature)


		data_generate(self, 20, trans)

		for i in range(len(trans)):		# loop to get the trained gaussian distributions
			trans_data = [x[i] for x in self.train]
			mean = float(sum(trans_data)) / len(trans_data)
			dif = [(x - mean) ** 2 for x in trans_data]
			sigma = math.sqrt(float(sum(dif)) / len(dif))
			self.trained_gaussian_set.append([mean, sigma])




class locator:		# main locator class
	def __init__(self, num_trans, k, std):		# user initiate number of transmitters, resoulution k, and standard deviation
		self.num_trans = num_trans
		self.k = k
		self.std = std
		self.errors = []		# record the total error for given num_trans, k and std

	def run_simulation(self, num_runs):
		grids = []		# records all grids' information
		trans = []		# location of transmitters
		count = 0
		while not count == self.num_trans:		# loop to assign locations to transmitters
			i = math.floor((200 / self.k) * np.random.random())
			j = math.floor((200 / self.k) * np.random.random())
			if not [i, j] in trans:
				trans.append([i, j])
				count += 1

		def bayes_classify(self, grids, vector):		# bayes classification algorithm
			max_posterior = -1
			max_i = -1
			max_j = -1
			for i in range(200 / self.k):
				row = []
				for j in range(200 / self.k):
					myGrid = grids[i][j]
					if myGrid.usable == False:
						continue
					prob = 1
					for k in range(len(vector)):
						mean = myGrid.trained_gaussian_set[k][0]
						sigma = myGrid.trained_gaussian_set[k][1]
						rssi = vector[k]
						pdf = (1 / (sigma * math.sqrt(2 * math.pi))) * math.e ** ((-(rssi - mean) ** 2) / (2 * sigma ** 2))
						prob = prob * pdf
					if prob > max_posterior:
						max_posterior = prob
						max_i = i
						max_j = j

			return [max_i, max_j]

		for run in range(num_runs):		# assign value to all grids
			for i in range(200 / self.k):
				row = []
				for j in range(200 / self.k):
					oneGrid = grid(i, j, trans, self.k, self.std)
					row.append(oneGrid)
				grids.append(row)

			for i in range(200 / self.k):		# do bayes classification and calculate errors
				print i
				for j in range(200 / self.k):
					oneGrid = grids[i][j]
					if oneGrid.usable == False:
						continue
					test_set = oneGrid.test
					for test_sample in test_set:
						label = bayes_classify(self, grids, test_sample)
						label_coor_x = label[1] * self.k + 0.5 * self.k
						label_coor_y = label[0] * self.k + 0.5 * self.k
						ground_truth_x = oneGrid.coor_x
						ground_truth_y = oneGrid.coor_y
						error = math.sqrt((label_coor_x - ground_truth_x) ** 2 + (label_coor_y - ground_truth_y) ** 2)
						self.errors.append(error)

		














