import cv2
import mediapipe as mp
import time
import handTrackingModule as htm

pTime = 0
cap = cv2.VideoCapture(0)

detector = htm.HandTrackingModule()

while cap.isOpened():
        success, img = cap.read()
        if not success:
            print("Failed to grab frame")
            break

        img = detector.findHands(img)
        lmList=detector.findPosition(img)

        if len(lmList)!=0:
            print(lmList[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime) 
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        # Show the image with detected hands
        cv2.imshow("Hand Tracking", img)

        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()