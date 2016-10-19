import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

# Get image (maybe read image series?)
r_patches = []
r_avgs = []
g_patches = []
b_patches = []

for i in range(1,8):
	orig = cv2.imread('Images/IMG_000%s.JPG' % (str(i)))
	shape = orig.shape
	# cv2.imshow('image', img)
	# cv2.waitKey(0)
	# print shape[0] sanity check

	# Get image patch (try to print all image patches in same fig)

	patch = orig[2500:2550, 2500:2550]
	# patches.append(patch)
	# cv2.imshow('image', patch)
	# cv2.waitKey(0)
	# print "patch shape: " , patch.shape

	# Get patch average
	r_patch = patch[:,:,2]
	r_patches.append(r_patch)
	g_patch = patch[:,:,1]
	b_patch = patch[:,:,0]

	r_sum = 0
	g_sum = 0
	b_sum = 0

	for row in r_patch:
		r_sum += sum(row)
	# print "sum of pixels: " , r_sum
	r_avg = r_sum/(len(r_patch)*len(r_patch[0]))
	r_avgs.append(r_avg)
	# print "total pixels: " , (len(r_patch)*len(r_patch[0]))
	# print "patch average: " , r_avg
print "r_avgs: ", r_avgs

# plot B' with respect to T (remember to do for each channel)
B_r = r_avgs
B_g = []
B_b = []
T = [1/30.0,1/45.0,1/60.0,1/90.0,1/125.0,1/180.0,1/250.0]

plt.plot(T,B_r, 'ro')
plt.xlabel('T(s)')
plt.ylabel("B'")
plt.show()

# plot log(B') with respect to log(T) (remember to do for each channel)
log_B_r = [np.log10(b) for b in B_r]
log_B_g = []
log_B_b = []
log_T = [np.log10(t) for t in T]

plt.plot(log_T,log_B_r, 'ro')
plt.xlabel('log(T(s))')
plt.ylabel("log(B')")
plt.show()

