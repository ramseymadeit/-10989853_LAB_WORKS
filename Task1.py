import cv2
from google.colab.patches import cv2_imshow

#Load the image
image = cv2.imread('cars.jpeg')

# Check if the image loaded successfully
if image is None:
    print("Error: Could not load image 'cars.jpeg'. Make sure the file exists in the current directory.")
else:
    #Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Display original and grayscale images
    cv2_imshow(image)
    cv2_imshow(gray_image)

    # Save the grayscale image
    cv2.imwrite('photo_gray.jpg', gray_image)
    print("Grayscale image saved as 'photo_gray.jpg'.")

    # Wait until a key is pressed and close the image windows
    # cv2.waitKey(0) # waitKey is not needed with cv2_imshow
    # cv2.destroyAllWindows() # destroyAllWindows is not needed with cv2_imshow
