def apply_clahe(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_img = clahe.apply(img)
    return enhanced_img

#use the function to get images applied CLAHE(contrast_limited_adaptive_histogram_equalization)
#You can also change the parameters in the createCLAHE() function according to your requirements
#refer to this documentation to know more about CLAHE : https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
