# importing the required packages 
import cv2 
import numpy as np 
import pyautogui 
  
# Specify resolution 
# resolution = (1920, 1080) 
# codec = cv2.VideoWriter_fourcc(*"XVID") 
# filename = "soom.avi"
# fps = 20.0

# out = cv2.VideoWriter(filename, codec, fps, resolution) 
screen_size = (500, 600)
# pyautogui.size () 
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("out.avi",fourcc,60.0, (screen_size))

cv2.namedWindow("Live", cv2.WINDOW_NORMAL) 

cv2.resizeWindow("Live", 0.1, 0.1) 
  
while True: 
    img = pyautogui.screenshot(region=(0, 500, 500, 600))  
    frame = np.array(img) 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    out.write(frame) 
    cv2.imshow("Live", frame) 
    if cv2.waitKey(1) == ord("q"): 
        break
  
# Release the Video writer 
out.release() 
  
# Destroy all windows 
cv2.destroyAllWindows()