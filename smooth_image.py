import cv2
import numpy as np


def smooth_filter(image, kernel):
    # Create an empty output image
    smoothed_image = np.zeros_like(image)

    # Get image dimensions
    h, w = image.shape[:2]

    # Calculate p kernel based on kernel kernel
    p = kernel // 2

    # Iterate over each pixel in the image (excluding border pixels)
    for y in range(p, h - p):
        for x in range(p, w - p):
            # Apply the smoothing operation
            tot = 0

            # Iterate over the neighborhood around the current pixel
            for j in range(-p, p + 1):
                for i in range(-p, p + 1):
                    # Accumulate the pixel values
                    tot += image[y + j, x + i]

            # Calculate the average and assign it to the output image
            smoothed_image[y, x] = tot // (kernel ** 2)

    return smoothed_image

img = input("please enter image path: ")
# Load the image
print("please want it needs some seconds")
image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

# Define the kernel kernel for the smoothing filter
kernel = 5

# Apply the smooth filter
smoothed_image = smooth_filter(image, kernel)

cv2.imshow('Smoothed Image', smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
