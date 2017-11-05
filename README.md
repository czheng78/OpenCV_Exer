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

