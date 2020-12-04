## Image Fundamentals
Image processing libraries such as OpenCV and scikit-image represent RGB images as multi-
dimensional NumPy arrays with shape (height, width, depth). Readers who are using image
processing libraries for the first time are often confused by this representation – why does the
height come before the width when we normally think of an image in terms of width first then
height?

* ```The answer is due to matrix notation.```

This image has a width of 300 pixels (the number of columns), a height of 248 pixels (the
number of rows), and a depth of 3 (the number of channels). To access an individual pixel value
from our image we use simple NumPy array indexing: