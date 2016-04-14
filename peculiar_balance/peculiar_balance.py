# import math
# import time
#
#
# def answer(x):
# 	left = x
# 	right = 0
# 	power = 0
# 	output = []
# 	while left != right:
# 		letter = get_letter(x, power)
# 		if letter == 'L':
# 			left += int(math.pow(3, power))
# 		elif letter == 'R':
# 			right += int(math.pow(3, power))
# 		output.append(letter)
# 		power += 1
# 	return output
#
#
# def find_start(power):
# 	start = 0
# 	for exp in range(power + 1):
# 		start += int(math.pow(3, exp - 1))
# 	return start
#
#
# def get_letter(pos, power):
# 	value = int(math.pow(3, power))
#
#   # Solution works, but runs too long
# 	r_start = find_start(power) + 1
# 	r_end = r_start + value - 1
# 	l_start = r_end + 1
# 	l_end = l_start + value - 1
# 	b_start = l_end + 1
# 	b_end = b_start + value - 1
#
# 	while pos > b_end:
# 		pos -= (value * 3)
#
# 	if r_start <= pos <= r_end:
# 		return 'R'
# 	elif l_start <= pos <= l_end:
# 		return 'L'
# 	return '-'
#
#   # Bad solution (memory issues)
# 	letters_combined = [None] * find_start(power)
# 	letters = ['R'] * value + ['L'] * value + ['-'] * value
# 	letters_combined += letters
# 	while pos > len(letters_combined):
# 		letters_combined += letters
# 	return letters_combined[pos - 1]
#
# i = 1
# while i <= 1000000000:
# 	start_time = time.time()
# 	print(i, answer(i))
# 	print("%.3f" % (time.time() - start_time))
# 	i += 1

from math import log, ceil
from multiprocessing import Pool


def answer(x):
	l = x
	r = 0
	out = []

	# max list size is next power of 3
	level = ceil(log(x, 3))
	weight = 3 ** level

	while weight >= 1:
		# put the weight in the smallest bin, but only if it lessens the gap
		if l < r and l + weight - r < r - l:
			out.insert(0, "L")
			l += weight
		elif r < l and r + weight - l < l - r:
			out.insert(0, "R")
			r += weight

		# Skip the weight, but only leave the skip instruction if it wouldn't be on the end.
		elif out:
			out.insert(0, "-")

		weight /= 3
	return out


def test(x):
	answer_list = answer(x)
	l = x
	r = 0
	for j, side in enumerate(answer_list):
		if side == "L":
			l += 3 ** j
		elif side == "R":
			r += 3 ** j
		elif side == "-":
			pass

	# print("%s: %s: %s" % (i, l == r, answer_list))
	assert (l == r)
	assert (answer_list[-1] != "-")

if __name__ == "__main__":
	pool = Pool()
	# use multiprocessing, but don't keep the results
	for i in pool.imap_unordered(test, xrange(1, 100000), chunksize=1024):
		pass
	print('Done')

print(8, answer(8))
