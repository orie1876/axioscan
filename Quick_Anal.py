#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 08:53:40 2020

@author: Mathew
"""
# These are the packages we are using. 

from skimage.io import imread
import matplotlib.pyplot as plt
from skimage import filters,measure



image=imread("/Users/Mathew/Desktop/Axioscan/apt.tif")


# This is just to show a small region of the image, since it's difficult to see what's happening with the full image. 
region=image[500:1000,500:1000]
plt.imshow(region,cmap="Blues")
plt.show()


# Determine a threshold using the Otsu method - Note, if I was comparing cases etc., I'd keep the threhsold constant, and not use Otsu for all of them. 
threshold=filters.threshold_otsu(image)
print(threshold)            # This prints the threshold that Otsu has determined.   
    
filtered=image>threshold    # Apply the threshold to the image. If going for constant threshold for all images, could just replace this with a number.

region_filtered=filtered[:,:]   # Can set a region to look at.
plt.imshow(region_filtered,cmap="Blues")    
plt.show()

# Now find the different features in the thresholded image. 
label_image=measure.label(region_filtered)
plt.imshow(label_image)
plt.show()

# Measure parameters of labelled regions. 
table=measure.regionprops_table(label_image,properties=('area','centroid','orientation','major_axis_length','minor_axis_length'))


# Get the area and length data. 
areas=table['area']
lengths=table['major_axis_length']

number=len(areas)  # Count the number of features detected. 

print(number)

# Plot some histograms. 

plt.hist(areas, bins = 50,range=[0,100], rwidth=0.9,color='#607c8e')
plt.xlabel('Area (pixels)')
plt.ylabel('Number of Features')
plt.title('Area of features')
plt.show()

plt.hist(lengths, bins = 50,range=[0,200], rwidth=0.9,color='#607c8e')
plt.xlabel('Length (pixels)')
plt.ylabel('Number of Features')
plt.title('Length')
plt.show()



# For control:
    
    
imagecont=imread("/Users/Mathew/Desktop/Axioscan/noapt.tif")

filteredcont=imagecont>threshold    # Apply the threshold to the image. If going for constant threshold for all images, could just replace this with a number.




label_image_cont=measure.label(filteredcont)


# Measure parameters of labelled regions. 
tablecont=measure.regionprops_table(label_image_cont,properties=('area','centroid','orientation','major_axis_length','minor_axis_length'))


# Get the area and length data. 
areascont=tablecont['area']
lengthscont=tablecont['major_axis_length']

numbercont=len(areascont)  # Count the number of features detected. 

print(numbercont)

# Plot some histograms. 

plt.hist(areascont, bins = 50,range=[0,100], rwidth=0.9,color='#607c8e')
plt.xlabel('Area (pixels)')
plt.ylabel('Number of Features')
plt.title('Area of features (control)')
plt.show()

plt.hist(lengthscont, bins = 50,range=[0,200], rwidth=0.9,color='#607c8e')
plt.xlabel('Length (pixels)')
plt.ylabel('Number of Features (control)')
plt.title('Length')
plt.show()