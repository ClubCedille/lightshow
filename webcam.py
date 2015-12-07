import cv2
import sys
import socket
from subprocess import call

oldValueFace = 0
oldValueEye = 0

def callRasp(MESSAGE) :
    UDP_IP = "192.168.1.102"
    # UDP_IP = "127.0.0.1"
    UDP_PORT = 10001
    sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    return


faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_Cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )


    if  (len(faces) == 0 ) and not (oldValueFace == len(faces)):
        print('FACE DETECTION FAILED')
        oldValueFace = len(faces)
        # call(["ssh","pi@192.168.1.102", "sudo python faceLightDOWN.py", "&"])
        callRasp("00")

    if not (oldValueFace == len(faces)):
        oldValueFace = len(faces)
        print('Face detected successfully')
        # call(["ssh","pi@192.168.1.102", "sudo python faceLightUP.py", "&"])
        callRasp("01")

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # In face, there is eyes
        eyes = eye_Cascade.detectMultiScale(roi_gray)

        # If no eyes
        if  len(eyes) == 0 and not (oldValueEye == len(eyes)):
            oldValueEye = len(eyes)
            print('EYES DETECTION FAILED ')
            # call(["ssh","pi@192.168.1.102", "sudo python eyeLightDOWN.py", "&"])
            callRasp("10")

        # If eyes
        if not (oldValueEye == len(eyes)):
            oldValueEye = len(eyes)
            print('Eyes delected successfully')
            # call(["ssh","pi@192.168.1.102", "sudo python eyeLightUP.py", "&"])
            callRasp("11")

        # Create rectangle over eyes
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255,0, 0), 2)




    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
