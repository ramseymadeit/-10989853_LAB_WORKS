import cv2
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

# Step 1: Load the color image
image = cv2.imread('nice house.jpeg')

# Check if the image loaded successfully
if image is None:
    print("Error: Could not load image 'nice house.jpeg'. Make sure it's in the same directory.")
    # Exit the script gracefully
    exit()

# Step 2: Convert to Grayscale, HSV, and LAB
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Step 3: Display all converted images
cv2_imshow(image)
cv2_imshow(gray)
cv2_imshow(hsv)
cv2_imshow(lab)

# Step 4: Save converted images
cv2.imwrite('photo_grayscale.jpg', gray)
cv2.imwrite('photo_hsv.jpg', hsv)
cv2.imwrite('photo_lab.jpg', lab)
print("Images saved: photo_grayscale.jpg, photo_hsv.jpg, photo_lab.jpg")

# Step 5: Plot histogram of grayscale image
plt.figure(figsize=(8, 4))
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.hist(gray.ravel(), bins=256, range=[0, 256], color='gray')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 6: Wait for key press and close windows
# cv2.waitKey(0) # waitKey is not needed when using cv2_imshow
# cv2.destroyAllWindows() # destroyAllWindows is not needed when using cv2_imshow
