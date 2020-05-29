import cv2
import numpy as np

drawing = False
point1 = ()
point2 = ()

canvas_height = 977
canvas_width = 1440

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
    canvas = np.ones((canvas_height, canvas_width, 3), dtype=np.uint8)
    canvas = canvas * 255

    if point1 and point2:
        mid_point_x = int((point1[0] + point2[0])/2)
        mid_point_y = int((point1[1] + point2[1])/2)
        cv2.rectangle(canvas, point1, point2, (0, 0, 0))
        text_height = (point2[1] - point1[1])/100
        cv2.putText(canvas, "Textbox", (mid_point_x-50, mid_point_y), cv2.FONT_HERSHEY_DUPLEX, text_height, (0, 0, 0), 2)

        
    cv2.imshow("canvas", canvas)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()

margin_top = str(point1[1]) + "px"
margin_left = str(point1[0]) + "px"
height = str(point2[1] - point1[1]) + "px"
width = str(point2[0] - point1[0]) + "px"

f = open("index.html", "w")
f.write("<!DOCTYPE html>\n")
f.write("<html>\n")
f.write("<body>\n")
f.write("<input type=\"text\" id=\"fname\" name=\"fname\" placeholder=\"Textbox\" style=\"margin-top:"+margin_top+"; margin-left: "+margin_left+"; height: "+height+"; width: "+width+";font-size:"+height+"; text-align:center;\">\n")
f.write("</body>\n")
f.write("</html>")
f.close()


























