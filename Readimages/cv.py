import cv2

# Load the image
image = cv2.imread("image.jpg.png")  # Replace with your actual image filename

# Check if image is loaded successfully
if image is None:
    print("Error: Could not read the image.")
else:
    # Display the image
    cv2.imshow("Displayed Image", image)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
