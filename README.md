# OpenCV_Exer

Exercise 1:

A program reads the cvMat object with the inputs of rows, columns, and type, which creates a new two-dimensional matrix. It also consists a pointer to the Matrix containing the pixel values, which is being represented by multiple color channels. In order to get the pixel intensity value, you have to know the type of an image and the number of channels. 

Exercise 2:

ColorImage.cpp takes in an image and output the same image with 10 different color conversions. The first 3 RGB images converted the image to individual values for red, green and blue. The red image has the lightest color and green image has the darkest color. The next 3 images are converted to the YCbCr category, which is used widely in video and image compression schemes. The Y image has a similar color compared to the green image but a little bit lighter in color. The Cr image seems to be a darker version of the Cb image. The last 3 images are converted to the HSV colorspace. These images are hue, saturation, and value. The value image has a similar color compared to the red image. The hue image is the most interesting one because the darkest color in the image is the lightest color in other converted images. 

Pixel Values at (20,25):
Red : 235
Green : 138
Blue : 106
Y : 163
Cb : 179
Cr : 96
Hue : 7
Saturation : 140
Value : 235

Exercise 3:

There seems to be little changes when the kernel size is changed. However, it seems like as you increase the kernel size, it will find any white pixel and then turn the neighboring pixels to white. Kernel size of 5 by 5 seems to work "better" for the gaussian noise and salt-and-pepper noise.

Exercise 4:

For binary threshold, it converts the image into black and white. Basically, if the intensity of the pixel is higher than a certain threshold, then the new pixel is set to the maximum value, otherwise the pixels are set to 0. The disadvantage of this threhold is that it is not that usefl for images with strong illumination and also there are limitations in the way it categorize the pixels. It only takes into 2 conditions to make the final decision about the pixels in an image. Band threshold is the opposite of the binary threshold. If the intensity of the pixel is higher than a certain threshold, then the new pixel is set to 0, otherwise the pixels are set to maximum value. For the semi-threshold case, the image goes completely dark. In this case, the pixels that are below the threshold have been considered as object pixels, which makes the background brighter than the foreground. Adaptive threshold seems to calculate the threshold for a small regions of the image and get different thresholds for different regions of the same image. It is useful when we use it on images with varying or strong illumination. 

