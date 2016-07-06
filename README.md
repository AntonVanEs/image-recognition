# image-recognition
I am trying to create image recognition software using Python (hopefully the end product will not even require any external libraries), and will be using a 'haar cascade'  to do so. It is not yet working.

### Theory
##### Haars
The way it will work is called haar cascade. To my knowlege, this means that a numbers of haars will be generated to check if a certain part of an image is, for example, an eye. 
A haar is a matix that is smaller than the original image. For all possile positions in the image, it will compare the colors (I use black and white images) under the matrix to the values inside it. This returns a value: the sum of (colour of pixel in image) x (value of pixel in haar).
The values returned by haars for a few differend eyes are combined to form an average value and a standard deviation.
95% of the eyes should be at most 2 standerd deviations away from the mean. Similarly, the mean value and standard deviation are determied for a range of non-eye images. The score a haar gets, is the percentage of non-eye images that are between those values as well. This can be estimated using the mean values and the standard deviations. The score, after runnign the learning program, will range from 5% to 20%.

##### Cascade
The 'cascade' part of 'haar cascade' means that we wont't use just one haar, but multiple. In my case, five or six seem to work great.
About 95% of the eye-pictures are within two standard deviations of the mean. If we require them to be within this range for 5 haars, we are left with still 77% of eyes. However, in realety the odds apear to be a lot better. This is due to the fact that a small area around the eye will all count as 'eye'. The optimal location often is almost the same for most haars.
Almost 17% of non-eye images are within the same perimeter, on average (for my haars). However, after running 5 haars, only 0.013% of non-eye images will pass.

NOTE: all pictures included are of myself. In real-life testing I will use more images of different people, but I can't put them on-line. 

