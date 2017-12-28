# @uthor and Intructor - Ayush Pareek
# Gradient Descent Tutorial - Deep Learning Series - CybrosX Lectures
from numpy import *

def compute_errror_for_given_points(b,m,points):
	totalError = 0
	for i in range(0,len(points)):
		x = points[i,0]
		y = points[0,1]
		totalError += (y-(m*x+b)) ** 2
	return totalError


def step_gradient (b_current, m_current,)

def gradient_descent_runner(points, initial_b, initial_m, learning_rate ,num_iterations):
	b = starting_b
	m=  starting_m

	for i in range(num_iterations):
		b, m = step_gradient (b,m, array(b,m), learning_rate)
	return [b,m]
		

def run():
	points= genfromtext('data.csv',delimiter=',')
	#hyperparameters
	learning_rate= 0.0001
	#y=mx+b (slope formula)
	initial_b = 0
	initial_m = 0
	num_iterations=1000
	[b,m]=gradient_descent_runner(points, initial_b, initial_m, learning_rate ,num_iterations)
	print b
	print m



if _name_ = '_main_':
	run()