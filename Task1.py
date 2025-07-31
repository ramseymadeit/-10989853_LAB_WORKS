import cv2
from google.colab.patches import cv2_imshow
image = cv2.imread('cars.jpeg')

if image is None:
    print("Error: Could not load image 'cars.jpeg'. Make sure the file exists in the current directory.")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2_imshow(image)
    cv2_imshow(gray_image)
    cv2.imwrite('photo_gray.jpg', gray_image)
    print("Grayscale image saved as 'photo_gray.jpg'.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
