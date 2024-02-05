#gst-launch-1.0 rtspsrc location=rtsp://admin:yualta123@192.168.68.69:554/h264Preview_01_main latency=0 ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink

import cv2
import mediapipe as mp 

#print(cv2.getBuildInformation())

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

'''username = "admin"
password = "yualta123"
ip = "192.168.0.3"
port = "554"
protocol = "h264"
stream_type = "main"
options = ""

rtsp_url = f"rtsp://{username}:{password}@{ip}:{port}/{protocol}Preview_01_{stream_type}{options}"

gstreamer_pipeline = (
    f"rtspsrc location={rtsp_url} latency=0 ! "
    "rtph264depay ! avdec_h264 ! "
    "videoconvert ! appsink drop=true"
)
#appsink drop=true
print("pruebas: ",gstreamer_pipeline)
cap = cv2.VideoCapture(gstreamer_pipeline, cv2.CAP_GSTREAMER)
'''
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    static_image_mode =False,
    max_num_hands = 4,
    min_detection_confidence=0.5) as hands:

    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        
        height, width, _ = frame.shape
        frame = cv2.flip(frame,1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)    

        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )

        cv2.imshow("Frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()