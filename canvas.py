import cv2
import numpy as np

drawing = False
point1 = ()
point2 = ()

def mouse_drawing(event, x, y, flags, params):
    global point1, point2, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing is False:
            drawing = True
            point1 = (x, y)
        else:
            drawing = False

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            point2 = (x, y)

cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", mouse_drawing)

while True:
    canvas = np.ones((460, 814, 3), dtype=np.uint8)
    canvas = canvas * 255

    if point1 and point2:
        cv2.rectangle(canvas, point1, point2, (0, 255, 0))

    cv2.imshow("canvas", canvas)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
