import cv2
import numpy as np
import pyautogui as pgi

screen_size=(1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("myvideo.avi", fourcc, 20.0, (screen_size))

while True:
    # make a screenshot
    img = pgi.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    output.write(frame)
    # show the frame
    cv2.imshow("show",frame)
    # if the user clicks q, it exits
    if cv2.waitKey(1)==ord("q"):
        break
    
# make sure everything is closed when exited
cv2.destroyAllWindows()
output.release()
