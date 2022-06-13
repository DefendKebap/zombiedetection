import mss
import numpy as np
import cv2
import pyautogui
import time
import keyboard
import torch


model = torch.hub.load(r'D:\yolov5-master', 'custom', path=r'D:\yolov5-master\zombibest.pt', source='local')
with mss.mss() as sct:
    monitor = {'top':10, 'left':0, 'width': 1920, 'height': 1080}
while True:
    img = np.array(sct.grab(monitor))
    results = model(img)
    r1 = results.xyxy[0].tolist()
    print(r1)
	

    if len(r1) > 0:
        if r1[0][4] > .35:
            if r1[0][5] == 0 or r1 [0][5] == 1:
                x= int(r1[0][2])
                y= int(r1[0][3])
                width = int(r1[0][2] - r1[0][0])
                print('width', width)
                height = int(r1[0][3] - r1[0][1])
                print('height', height)
                xpos = int(.37 * ((x-(width/2))- pyautogui.position()[0]))
                ypos = int(.30 * ((x-(width/2))- pyautogui.position()[1]))
                pyautogui.moveRel(xpos,ypos)
                pyautogui.click()
                pyautogui.moveRel(-xpos, -ypos)
    cv2.imshow('s', np.squeeze(results.render()))
    cv2.waitKey(1)
    if keyboard.is_pressed('q'):
        break

cv2.destroyAllWindows()


