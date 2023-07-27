import cv2 

# specify the path to image (loading image image) 
image1 = cv2.imread("IMG_7275 2.JPG") 
window_name = "Original image" 

# Displaying the original image 
cv2.imshow(window_name, image1) 

# convert the image from one color space to another 
grey_img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) 
invert = cv2.bitwise_not(grey_img) 

# image smoothing 
blur = cv2.GaussianBlur(invert, (21,21), 0) 
invertedblur = cv2.bitwise_not(blur) 
sketch = cv2.divide(grey_img, invertedblur, scale=256.0) 

# save the converted image to specified path 
cv2.imwrite("/Users/shengbincui/Desktop/sketch.png", sketch) 

# Reading an image in default image 
image = cv2.imread("Users/shengbincui/Desktop/sketch.png") 

# Window name in which image is displayed 
window_name = 'Sketch image' 

# Displaying the sketch image 
cv2.imshow(window_name, image) 
# waits for user to press any key 
cv2.waitKey(0) 
# closing all open windows 
cv2.destroyAllWindows() 