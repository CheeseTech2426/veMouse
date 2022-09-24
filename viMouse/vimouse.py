import cv2
import ctypes
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
du = mp.solutions.drawing_utils
detect_hand = mp.solutions.hands.Hands()
title = 'Console'
ctypes.windll.kernel32.SetConsoleTitleW(title)
screenW, screenH = pyautogui.size()
iY = 0
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame,1)
    frameH, frameW, _ = frame.shape
    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out = detect_hand.process(rgbFrame)
    hands = out.multi_hand_landmarks
    if hands:
        for hand in hands:
            du.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frameW)
                y = int(landmark.y * frameH)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(255,0,255))
                    iX = screenW / frameW * x
                    iY = screenH / frameH * y
                    pyautogui.moveTo(iX,iY)
                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(255,0,255))
                    tX = screenW / frameW * x
                    tY = screenH / frameH * y
                    #print('out', abs(iY - tY))
                    if abs(iY - tY) < 30:
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow('viMouse', frame)
    cv2.waitKey(1)

    if cv2.waitKey(10) == ord('q'):
        break