# image-recognition
I am trying to create image recognition software using Python (hopefully the end product will not even require any external libraries), and will be using a methode of convolutional deep learning to do so, using haars.

### Theory
##### Haars
A haar is a matix that is smaller than the original image. For all possile positions in the image, it will compare the colors (I use black and white images) under the matrix to the values inside it. This returns a value: the sum of (colour of pixel in image) x (value of pixel in haar).

##### Deep learning
Deep learning a way of computer learning that is multiple layers deep. This means that you start with an input (input<sub>0</sub>). input<sub>0</sub>) will pass trough the first layer, wich will send an out an output<sub>1</sub>. output<sub>1</sub> now is an input in the second layer. This carries on over n layers, finaly returing output<sub>n</sub>. This output is the final result of the program, and should be as simple as a boolean value or a integer depending on what the program should do (look for faces, recognise handwiting, estimate weather, etc.)

##### combination
These two concepts can be used together for image recognition. Each of the layers will use a few haars to create differend images. When starting with a A x B image and using a a x b haar, all resulting values can be seen as an image (or matrix) of size (A-a)x(B-b). This means after each layer, the resulting images will be smaller. However, each layer will output multiple matrices (an array of matrices can be seen as a 3D matrix). The haars used in all layers exept layer 1 therefore must be 3D as well. The amount of layer and size of haars will be chosen in such a way that the output<sub>n-1</sub> will be a series of 1x1 martices (also known as numbers): 1D. Finaly layer n will interprite this and return (hopefully) the desired answer. 

NOTE: all pictures included are of myself. In real-life testing I will use more images of different people, but I can't put them on-line. 

