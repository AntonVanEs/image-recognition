# image-recognition
I am trying to create image recognition software using Python (hopefully the end product will not even require any external libraries), and will be using a 'haar cascade'  to do so. It is not yet working.

The way it will work is called haar cascade. To my knowlege, this means that a numbers of haars will be generated to check if a certain part of an image is, for example, an eye. 
A haar is a matix that is smaller than the original image. For all possile positions in the image, it will compare the colors (I use black and white images) under the matrix to the values inside it. This creates a value
Those values of differend eyes are combined to form an average and a standard deviation.
95% of the eyes should be at most 2 standerd deviations away from the mean. The score a haar gets, is the percentage of non-eye images that are between those values as well. This can range from 5% to 20%
The cascade part means that all positions that succeed in the first test, will undergo another to be more certain it is an eye. If it succeds, yet another haar will be overlaid, untill we are almost certain that the position is one of an eye.
This cascade has not yet been propperly programmed, for now I only use one haar.
NOTE: all pictures included are of myself. In real-life testing I will use more images of different people, but I can't put them on-line. 

