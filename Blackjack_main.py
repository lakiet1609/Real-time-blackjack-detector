from ultralytics import YOLO
import ultralytics
import cv2
import cvzone
import math
import detectxidach


cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4, 720)

model = YOLO('cards.pt')

classNames = ['10C', '10D', '10H', '10S',
              '2C', '2D', '2H', '2S',
              '3C', '3D', '3H', '3S',
              '4C', '4D', '4H', '4S',
              '5C', '5D', '5H', '5S',
              '6C', '6D', '6H', '6S',
              '7C', '7D', '7H', '7S',
              '8C', '8D', '8H', '8S',
              '9C', '9D', '9H', '9S',
              'AC', 'AD', 'AH', 'AS',
              'JC', 'JD', 'JH', 'JS',
              'KC', 'KD', 'KH', 'KS',
              'QC', 'QD', 'QH', 'QS']



player1 = []
while True:
    ret,frame = cap.read()
    results = model(frame,stream=True)
    hand = []
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w,h = x2 - x1, y2 - y1
            cvzone.cornerRect(frame, (x1, y1, w, h))
            #Confidence
            conf = math.ceil((box.conf[0]*100))/100
            #Class names
            cls = int(box.cls[0])
            current_name = classNames[cls]
            cvzone.putTextRect(frame,f'{current_name}', (max(0,x1), max(35, y1)), scale=3, thickness=3)
            if conf > 0.70:
                hand.append(current_name)
    
    hand = list(set(hand))
    print(hand)

        
    if len(hand) >= 2:
        results_xidach, current_scores = detectxidach.findxidachhand(hand) 
        print(results_xidach, current_scores)
        if results_xidach == 'Not enough to check':
            cvzone.putTextRect(frame,'You should push more cards', (500,650), scale=2, thickness=2)
            cvzone.putTextRect(frame,f'Hand status: {results_xidach}', (100,75), scale=2, thickness=2)
            cvzone.putTextRect(frame,f'Current score: {current_scores}', (700,75), scale=2, thickness=2)
        elif results_xidach == 'Enough to check':
            cvzone.putTextRect(frame,'You shouldn not push more cards', (500,650), scale=2, thickness=2)
            cvzone.putTextRect(frame,f'Hand status: {results_xidach}', (100,75), scale=2, thickness=2)
            cvzone.putTextRect(frame,f'Current score: {current_scores}', (700,75), scale=2, thickness=2)
        elif results_xidach == 'BlackJack':
            cvzone.putTextRect(frame,f'Hand status: {results_xidach}', (100,75), scale=2, thickness=2)
        elif results_xidach == 'Double Aces':
            cvzone.putTextRect(frame,f'Hand status: {results_xidach}', (100,75), scale=2, thickness=2)
        else:
            cvzone.putTextRect(frame,f'Hand status: {results_xidach}', (100,75), scale=2, thickness=2)
            cvzone.putTextRect(frame,f'Current score: {current_scores}', (700,75), scale=2, thickness=2)
        
        turn = []
        if hand not in turn:
            if hand == []:
                continue
            turn.append(hand)
            player1.append(hand)   
        print(player1)         

    cv2.imshow('Image',frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()