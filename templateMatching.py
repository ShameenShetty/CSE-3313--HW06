"""
    Name:   Shameen Shetty
    ID:     1001429743
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import skimage.feature as ski

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def findImage(mainImage, template) :
    colorImg_GreyScale = rgb2gray(mpimg.imread(mainImage))
    templateImg_GreyScale = rgb2gray(mpimg.imread(template))
    
    templateMatching_result = ski.match_template(colorImg_GreyScale, templateImg_GreyScale)
    
    fig1, axs1 = plt.subplots(1)
    fig2, axs2 = plt.subplots(1)
    
    axs1.set_title("Original Color Image")
    axs1.imshow(mpimg.imread(mainImage))
    
    axs2.set_title("Original Template Image")
    axs2.imshow(mpimg.imread(template))


    # getting the highest normalized cross-correlation value in x and y coordinates
    rowCoord = np.argmax(np.max(templateMatching_result, axis=0))
    colCoord = np.argmax(np.max(templateMatching_result, axis=1))
    image = mpimg.imread(mainImage).copy()

    tempImg = mpimg.imread(template)
    x, y, z = tempImg.shape

    # replacing the pixels with zeros
    for row in range(x):
        for col in range(y):
            image[rowCoord + x, colCoord + y] = np.array([0, 0, 0])
            image[rowCoord + x, colCoord - y] = np.array([0, 0, 0])
            image[rowCoord - x, colCoord + y] = np.array([0, 0, 0])
            image[rowCoord - x, colCoord - y] = np.array([0, 0, 0])

    

    fig3, axs3 = plt.subplots(1)
    axs3.set_title("Replacing pixels")
    axs3.imshow(image)
    
    plt.show()

    return rowCoord, colCoord
    
    
#############  main  #############
# this function should be how your code knows the names of
#   the images to process
# it will return the coordinates of where the template best fits

if __name__ == "__main__":
    mainImage = "ERBwideColorSmall.jpg"
    template = "ERBwideTemplate.jpg"
    r, c = findImage(mainImage, template)

    print("coordinates of match = (%d, %d)" % (r, c))