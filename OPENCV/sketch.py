import cv2

img = cv2.imread('image.jpeg')

if img is None:
    print("Error: image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    invert = cv2.bitwise_not(gray)

    blur = cv2.GaussianBlur(invert, (21, 21), 0)

    invert_blur = cv2.bitwise_not(blur)

    sketch = cv2.divide(gray, invert_blur, scale=256.0)

    # Apply color map
    color_sketch = cv2.applyColorMap(sketch, cv2.COLORMAP_JET)

    cv2.imshow('Colored Sketch', color_sketch)

    cv2.waitKey(0)

    cv2.destroyAllWindows()