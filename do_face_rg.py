

import cv2
import face_recognition
import matplotlib.pyplot as plt
# %matplotlib inline # 在 jupyter 中使用的时候，去掉注释

cap = cv2.VideoCapture('cut.mp4')
ret, frame = cap.read()
if ret:
    face_locations = face_recognition.face_locations(frame)
    for (top_right_y, top_right_x, left_bottom_y,left_bottom_x) in face_locations:
        cv2.rectangle(frame, (left_bottom_x,top_right_y), (top_right_x, left_bottom_y), (0, 0, 255), 10)
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    plt.show()
