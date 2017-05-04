import localization as lc
import numpy as np
import matplotlib.pyplot as plt

parameter_set = [[3, 5, 2], [3, 5, 10], [8, 5, 2], [8, 5, 10]]		# 4 sets of parameters
for param in parameter_set:
	myLocator = lc.locator(param[0], param[1], param[2])
	myLocator.run_simulation(12)
	error = myLocator.errors
	error.sort()
	Y = np.arange(0, 1, 1.0 / len(error))
	lb = 'plot(' + str(param[0]) + ', ' + str(param[1]) + ', ' + str(param[2]) + ')'
	plt.plot(error, Y, label = lb)		# draw CDF
plt.legend()
plt.savefig('fig_prob1.png')
plt.show()

