from add_two_array_values import add_two_array_values
from add_values import add_values
from array_calc1 import array_calc1
from array_copy import array_copy
from autoCorrelation import autoCorrelation
from average import average
from binarySearchFomTo import binarySearchFromTo
from bubble import bubble
from calculateAbsoluteDifferences import calculateAbsoluteDifferences
from calculateDifferences import calculateDifferences
from chebyshevDistance import chebyshevDistance
from check_equal import check_equal
from check_equal_tolerance import check_equal_tolerance
from checkNonNegative import checkNonNegative
from checkPositive import checkPositive
from chiSquare import chiSquare
from clip import clip
from cnt_zeroes import cnt_zeros
from computeCanberraDistance import computeCanberraDistance
from cosineDistance import consineDistance
from count_k import count_k
from count_non_zeroes import count_non_zeroes
from covariance import covariance
from dec_array import dec_array
from distance1 import distance1
from distanceInf import distanceInf
from dot_product import dot_product
from durbinWatson import durbinWatson
from ebeAdd import ebeAdd
from ebeDivide import ebeDivide
from ebeMultiply import ebeMultiply
from ebeSubtract import ebeSubtract
from elementwise_equal import elementwise_equal
from elementwise_max import elementwise_max
from elementwise_min import elementwise_min
from elementwise_not_equal import elementwise_not_equal
from entropy import entropy
from equals import equals
from errorRate import errorRate
from evaluateHoners import evaluateHoners
from evaluateInternal import evaluateInternal
from evaluateNewton import evaluateNewton
from evaluateWeightedProduct import evaluateWeightedProduct
from find_diff import find_diff
from find_euc_dist import find_euc_dist
from find_magnitude import find_magnitude
from find_max import find_max
from find_max2 import find_max1
from find_median import find_median
from find_min import find_min
from g import g
from geometric_mean import geometric_mean
from get_array_value import get_array_value
from hamming_dist import hamming_dist
from harmonicMean import harmonicMean
from insertion_sort import insertion_sort
from kurtosis import kurtosis
from lag1 import lag1
from manhattan_dist import manhattan_dist
from manhattanDistance import manhattanDistance
from max import max
from mean_absolute_error import mean_absolute_error
from meanDeviation import meanDeviation
from meanDifference import meanDifference
from min import min
from partition import partition
from polevl import polevl
from pooledMean import pooledMean
from pooledVariance import pooledVariance
from power import power
from product import product
from quantile import quantile
from reverse import reverse
from safeNorm import safeNorm
from sampleKurtosis import sampleKurtosis
from sampleSkew import sampleSkew
from sampleVariance import sampleVariance
from sampleWeightedVariance import sampleWeightedVariance
from scale import scale
from selection_sort import selection_sort
from sequential_search import sequential_search
from set_min_val import set_min_val
from shell_sort import shell_sort
from skew import skew
from square import square
from standardize import standardize
from sum import sum
from sumOfLogarithms import sumOfLogarithms
from sumOfPowerOfDeviations import  sumOfPowerOfDeviations
from tanimotoDistance import tanimotoDistance
from variance import variance
from varianceDifference import varianceDifference
from weighted_average import weighted_average
from weightedMean import weightedMean
from weightedRMS import weightedRMS
from winsorizedMean import winsorizedMean


import numpy as np

a = [1, 2, 1, 2]

# array = np.arange(10)
# np.random.shuffle(array)
# print(array)

r_add_values = add_values(a)
# print(r_add_values)

r_array_calc1 = array_calc1(a, 2)
# print(r_array_calc1)

autocorrelation1 = np.correlate(a, a, mode="full")
# print(autocorrelation1)
mean = np.mean(a)
variance = np.var(a)
r_autoCorrelation = autoCorrelation(a, 2, mean, variance)
# print(r_autoCorrelation)

our_list = [19, -13, -6, 2, -18, 8]
our_list2 = [19, -13, -6, 2, -18, 8]
# our_list2= [18, 14, 5, 1, 9, 2]
# a = bubble(our_list)
# print(a)

# r_calculateAbsoluteDifferences = calculateAbsoluteDifferences(our_list)

# r_calculateDifferences = calculateDifferences(our_list, our_list2)
r_check_equal = check_equal(our_list, our_list2)
a = [1, 0, 0]
b = [0, 1, 0]
# r_computeCanberraDistance = computeCanberraDistance(a, b)
# print(r_computeCanberraDistance)

a = [5, 1, 12, 6, 4]
# for i in range( len(a)-2, -1, -1):
for i in range(len(a) - 1, -1, -1):
    print(a[i])
